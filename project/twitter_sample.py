import json
import pandas as pd

def return_length(in_path):
    # Load the Twitter data from a file
    with open(in_path, 'r') as f:
        data = [json.loads(line) for line in f]

    # # create a empty dataframe
    # df = pd.DataFrame(columns=['id', 'author_id', 'lang', 'text', 'created_at'])

    # # loop through the data
    # for i in range(len(data)):
    #     for j in range(len(data[i]['data'])):
    #         tweet_id = data[i]['data'][j]['id']
    #         author_id = data[i]['data'][j]['author_id']
    #         lang = data[i]['data'][j]['lang']
    #         text = data[i]['data'][j]['text']
    #         created_at = data[i]['data'][j]['created_at']
    #         df = df.append({'id': tweet_id, 'author_id': author_id, 'lang': lang, 'text': text, 'created_at': created_at}, ignore_index=True)
    
    # #create a name for the output file based on the dates of the tweets
    time = data[0]['data'][0]['created_at']
    #exact the date from time
    date = time.split('T')[0]

    # full_out_path = out_path + date +'_clean.csv'
    # df.to_csv(full_out_path, index=False)

    return ((date,len(data)))

import os
import glob

def get_path_list(x):
    path_list = []
    for file in glob.glob(x + "/*.json"):
        path_list.append(file)
    return path_list


# create a csv file for Twitter volume

def Twitter_volume(in_path, out_path):
    # get a list of path for all the json files in the folder x
    path_list = get_path_list('/Users/cmu-work/Data/Conspiracy dataset/Twitter_Ohio_Palestine')
    length_list = []
    for i in range(len(path_list)):
        result = return_length(path_list[i])
        print(result)
        length_list.append(result)
    # create a dataframe
    df = pd.DataFrame(length_list, columns=['date', 'length'])
    # create a csv file
    df.to_csv(out_path, index=False)


