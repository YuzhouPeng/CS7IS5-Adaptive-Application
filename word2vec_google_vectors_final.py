import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
print model.similarity('woman', 'man') 
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

list = []
new_wordlist=[]


for i in tlist:
    try:
        print model.similarity('song', i)
    except Exception:
        pass
list = []
new_wordlist=[]
for i in tlist:
    try:
        list.append(model.similarity('song', i))
        print model.similarity('song', i)
        print i
        new_wordlist.append(i)
    except Exception:
        pass
print list
len(list)
len(new_wordlist)