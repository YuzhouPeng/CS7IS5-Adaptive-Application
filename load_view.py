import pickle


if __name__=="__main__":
    with open('/Users/apple/projects/CS7IS-adaptive-applications/CS7IS5-Adaptive-Application/output-sport/Football.p', 'rb') as fp:
        data = pickle.load(fp)

    for key, value in data.items():
        print(key, value)

    d = data['data']
    for key, value in d.items():
        # print (key, value)
        print(key, value['similarity'])

    print(len(d.keys()))
    print(data['page'])