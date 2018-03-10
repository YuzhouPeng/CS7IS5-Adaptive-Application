import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
print model.similarity('woman', 'man') 
list = ['music','Pink_Floyd','Sex_Pistols']
for i in list:
    print model.similarity('song', i) 

model.similarity('Sachin_Tendulkar','Pink_Floyd')
model.similarity('Music','Magnetoencephalography')
model.similarity('Music','Symphony_No._5_(Beethoven)')
model.similarity('Music','Magnetoencephalography')
model.similarity('Music','Magnetoencephalography')
