import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
#print model.similarity('woman', 'man') 
import wikipedia
import bs4 as bs
import numpy as np

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
        link_dict[link['title']] = k
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

listt = []
new_wordlist=[]
for i in link_dict_final:
    try:
        listt.append(model.similarity('song', i))
        #print model.similarity('song', i)
        #print i
        new_wordlist.append(i)
    except Exception:
        pass
        

        
#print list
len(listt)
len(new_wordlist)
final_word2vec = {k: link_dict_final[k] for k in link_dict_final.viewkeys() & set(new_wordlist)} #to make the list of the word that are comparable in the page with their indexes  
len(final_word2vec)
finalvalues_list = [] #the final values in the code
for i in final_word2vec:
    try:
        finalvalues_list.append(model.similarity('song', i))
        #print model.similarity('song', i)
        #print i
    except Exception:
        pass
        
list1=list(final_word2vec.keys())
list2=list(final_word2vec.values())
list3=list(finalvalues_list)

rows = zip(list1,list2,list3)
import csv

with open("data.csv", "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
#just to clarify finally we have 3 list 1st final_word2vec with has the elements title and keys and finalvalues_list which has all the values
#and use final_word2vec.keys() for the word , final_word2vec.values() for the indexes and finalvalues_list to get the similarity values