import pandas as pd
import requests
import matplotlib.pyplot as plt
import datetime as dt


#set up the url 
url = 'https://api.pushshift.io/reddit/search/submission'

def get_data(url):
    #set up the parameters
    # collect from r/conspiracy subreddit
    # collect 100 posts at a time
    # collect posts from 3 February 2023 to April 2023
    # retrive only data contain keywords "ohio"

    params = {
        'subreddit': 'conspiracy',
        'size': 1000,
        'after': start_date,
        'q': 'derailment'
    }
    #pull the data
    res = requests.get(url, params)
    #check the status code
    res.status_code

    #convert the data to a json file
    data = res.json()
    #check the data
    df = pd.DataFrame(data['data'])
    return (df)

def visualize_df(df):
    # create visualization of post per day
    df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')
    df['date'] = df['created_utc'].dt.date
    grouped = df.groupby('date')['id'].count()
    grouped.plot(kind='line', figsize=(10,5))
    plt.title(f'Daily Submissions to r/Conspiracy with keyword "derailment"')
    plt.xlabel('Date')
    plt.ylabel('Number of Submissions')
    plt.show()

