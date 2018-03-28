import pickle


if __name__=="__main__":
    with open('/Users/apple/projects/CS7IS-adaptive-applications/CS7IS5-Adaptive-Application/output/Music.p', 'rb') as fp:
        data = pickle.load(fp)

    for key, value in data.items():
        print(key, value)

    d = data['data']
    for key, value in d.items():
        # print (key, value)
        print(key, value['similarity'])

    print(len(d.keys()))
    print(data['page'])

  
for key, value in data['data'].items():
    start_index = value['index_start']
    end_index = value['index_end']
    content = data['content']

    print ("Actual: ", content[start_index:end_index], "\n",
           "Expected: ", key)
    