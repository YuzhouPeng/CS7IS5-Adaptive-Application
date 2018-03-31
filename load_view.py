import csv
import pickle
import os, os.path

# Contains the file path for the pickle files
filepath = "./output-sports-2/"

# Name of the CSV files
PAGE_ID_FILE = 'pageID_1.csv'
KEYWORDS_FILE = 'keywords_1.csv'

# Store the topics in a dictionary. Currently we have two topics
topic_dict = {"Music"   : 1,
              "Sports"  : 2}  

if __name__=="__main__":

    # Open the CSV Files:
    csv_page = open(PAGE_ID_FILE, 'a')
    csv_keywords = open(KEYWORDS_FILE, 'a')

    # List to contain the dictionary entries for all the pickle file objects
    list_of_dict = []    

    # Read the pickle files and load into memory
    for root, dirs, files in os.walk(filepath):
        for filename in files:
            print(filename)
            filename = (filepath + filename)
            with open(filename, 'rb') as fp:
                list_of_dict.append(pickle.load(fp))
    
    # Total number of pickle files
    number_of_files = len(list_of_dict)

    keyword_id = 0
    
    for x in range(0, number_of_files):

        topic_id = 0;
        page_name = ''
        content = ''
        page_id = (x + 1)

        data = list_of_dict[x]
        # data = list_of_dict[0]

        # print(data)


        # get the topic ID
        topic_id = topic_dict.get(data['topic'])
        page_name = data['page']
        content = data['content']

        # print(topic_id)
        # print(page_name)
        # print(content)

        # exit(0)


        csv_page_writer = csv.writer(csv_page, delimiter = '~', lineterminator = '\r\n', quotechar = '"')
        # csv_page_writer = csv.writer(csv_page, delimiter = ',', quotechar = '"')
        csv_page_writer.writerow([str(page_id), str(topic_id), page_name, content])
        # csv_page_writer.writerow([str(page_id), str(topic_id), page_name])
        
        # Total number of keywords
        # print(len(data['data']))
        csv_keywords_writer = csv.writer(csv_keywords, delimiter = '~', lineterminator = '\r\n', quotechar = '"')
        keywords_dict = data['data']
        # print(keywords_dict)
        
        
        for key, value in keywords_dict.items():
            keyword = key
            keyword_id = keyword_id + 1
            # print(value)
            # for _key, _value in value.items():
                # print(_key, _value)
                # Update the CSV file
                # print([str(keyword_id), str(page_id), keyword, value.get('index_start'), value.get('index_end'), 
                #             value.get('summary'), value.get('similarity')])
            csv_keywords_writer.writerow([str(keyword_id), str(page_id), keyword, value.get('index_start'), value.get('index_end'), 
                        value.get('summary'), value.get('similarity')])



