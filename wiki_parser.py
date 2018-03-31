import wikipedia
import bs4 as bs
import re
import numpy as np

"""Get the article details such as Name, link, index of link on page, summary
   To store in DB"""


def get_wiki_data(model, topic_keys, page_name):
    # wikipedia.summary("art") -- get summary
    test = wikipedia.page(page_name)
    tlist = test.links
    tcontent = test.content
    tpage = test.html()

    soup = bs.BeautifulSoup(tpage, "html5lib")

    # tlist = [str(s).translate(None,"()") for s in tlist]
    # tlist = [s.replace('(', '') for s in tlist]
    # tlist = [s.replace(')', '') for s in tlist]
    # tlist = [s.replace(' ', '_') for s in tlist]

    links = soup.findAll('a')
    link_dict = {}
    for link in links:
        try:
            print(link['title'], " started")
            search_value = link['title']
            search_value = search_value.replace("(", "").replace(")", "").title().replace(" ", "_")
            similarity = 0
            print(search_value)
            for topic_key in topic_keys:
                similarity = max(similarity, model.similarity(topic_key, search_value))
            # if link.string == "study of the history of music":
            # k = tcontent.find(link.string)
            word = re.search('\\b' + link.string + '\\b', tcontent)
            if word:
                k = word.start()
                # val = link['href'].replace("/wiki/", "").replace("(", "").replace(")", "") + "   " + str(k)
                link_dict[link['title']] = {'index_start': k,
                                            'index_end': k+len(link.string),
                                            'summary': wikipedia.summary(link['title']),
                                            'similarity': similarity}
                print(link['title'], " done, found in text")
            else:
                print(link['title'], " not found in text")
        except Exception:
            print("fail")

    link_dict_final = {}
    for item in tlist:
        try:
            link_dict_final[item] = link_dict[item]
        except KeyError:
            print(item + " not found")
            pass

    return link_dict_final, tcontent
