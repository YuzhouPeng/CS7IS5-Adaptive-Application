# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:16:57 2018

@author: Vimanyu
"""

import wikipedia
import io

#wikipedia.summary("art")
test = wikipedia.page("Music")

#test.title
#test.url
#test.content
tlist = test.links

#tlist = [str(s).translate(None,"()") for s in tlist]    
tlist = [s.replace('(', '') for s in tlist]
tlist = [s.replace(')', '') for s in tlist]
tlist = [s.replace(' ', '_') for s in tlist]

with io.open("test_file.txt", "w", encoding="utf-8") as f:
    for item in tlist:
        f.write("%s\n" % item)
f.close()
