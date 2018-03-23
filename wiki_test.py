# -*- coding: utf-8 -*-
import wikipedia
import bs4 as bs

"""Get the article details such as Name, link, index of link on page, summary
   To store in DB"""

# wikipedia.summary("art") -- get summary
test = wikipedia.page("Music")

tlist = test.links
tcontent = test.content
tpage = test.html()

soup = bs.BeautifulSoup(tpage, "html5lib")
        
# tlist = [str(s).translate(None,"()") for s in tlist]
tlist = [s.replace('(', '') for s in tlist]
tlist = [s.replace(')', '') for s in tlist]
tlist = [s.replace(' ', '_') for s in tlist]
        
links = soup.findAll('a')        
link_dict = {}
for link in links:
    try:
        k = tcontent.lower().find(link.string.lower())
        # if link.string == "study of the history of music":
        val = link['href'].replace("/wiki/", "").replace("(", "").replace(")", "") + "   " + str(k) 
        link_dict[link['title']] = val
    except ValueError:
        pass
    except TypeError:
        pass
    except KeyError:
        pass
    except AttributeError:
        pass

link_dict_final = {}
for item in tlist:
    try:
        link_dict_final[item] = link_dict[item]
    except KeyError:
        pass
    
# Next, write to database
