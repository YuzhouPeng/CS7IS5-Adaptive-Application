# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:16:57 2018

@author: Vimanyu
"""

import wikipedia
import io
import bs4 as bs

#wikipedia.summary("art")
test = wikipedia.page("Music")

#test.title
#test.url
#test.content
tlist = test.links
tcontent = test.content
tpage = test.html()

soup = bs.BeautifulSoup(tpage, "html5lib")


links = soup.findAll('a')        
link_strings = []
for link in links:
    if link.string == "study of the history of music":
        print(link)
        print(link['title'])
    if link.string == "aesthetic examination of music":
        print(link)
        
        
links = soup.findAll('a')        
link_dict = {}
for link in links:
    try:
        k = tcontent.lower().find(link.string.lower())
        #if link.string == "study of the history of music":
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
        

#tlist = [str(s).translate(None,"()") for s in tlist]    
tlist = [s.replace('(', '') for s in tlist]
tlist = [s.replace(')', '') for s in tlist]
tlist = [s.replace(' ', '_') for s in tlist]

with io.open("test_file.txt", "w", encoding="utf-8") as f:
    for item in tlist:
        f.write("%s\n" % item)
f.close()

with io.open("output.txt", "w", encoding="utf-8") as k:
    for key, value in link_dict.items():
        k.write([key, val])
k.close()
