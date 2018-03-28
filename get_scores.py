import gensim

# print model.similarity('woman', 'man')


model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
listt = []
new_wordlist = []
for i in link_dict_final:
    try:
        listt.append(model.similarity('song', i))
        # print model.similarity('song', i)
        # print i
        new_wordlist.append(i)
    except Exception:
        pass

# print list
len(listt)
len(new_wordlist)
final_word2vec = {k: link_dict_final[k] for k in link_dict_final.viewkeys() & set(
    new_wordlist)}  # to make the list of the word that are comparable in the page with their indexes
len(final_word2vec)
finalvalues_list = []  # the final values in the code
for i in final_word2vec:
    try:
        finalvalues_list.append(model.similarity('song', i))
        # print model.similarity('song', i)
        # print i
    except Exception:
        pass

list1 = list(final_word2vec.keys())
list2 = list(final_word2vec.values())
list3 = list(finalvalues_list)

rows = zip(list1, list2, list3)
import csv

with open("data.csv", "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
# just to clarify finally we have 3 list 1st final_word2vec with has the elements title and keys and finalvalues_list which has all the values
# and use final_word2vec.keys() for the word , final_word2vec.values() for the indexes and finalvalues_list to get the similarity values