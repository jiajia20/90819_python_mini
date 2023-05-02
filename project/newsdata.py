import pandas as pd
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from GoogleNews import GoogleNews
import seaborn as sns

# part 1: scratching sample data and conduct content analysis

def fetch_news(api_key, keyword, max_pages=10):
    base_url = "https://newsapi.org/v2/everything"
    article_data = []

    for page in range(1, max_pages + 1):
        params = {
            'q': keyword,
            'apiKey': api_key,
            'page': page,

        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            news_data = response.json()
            articles = news_data['articles']

            for article in articles:
                title = article['title']
                link = article['url']
                source = article['source']['name']
                published_date = article['publishedAt']

                article_data.append([title, link, source, published_date])

                print(f"Title: {title}\nLink: {link}\nSource: {source}\nPublished Date: {published_date}\n---")
        else:
            print("Error fetching the results.")
            break

    # Save the article data to an Excel file
    df = pd.DataFrame(article_data, columns=['Title', 'Link', 'Source', 'Published Date'])
    df.to_excel('news_data_sample.xlsx', index=False)

# use api key to search for news
if __name__ == '__main__':
    api_key = "92cea9e23fa148b6b764d90a436e7a9f"
    keyword = 'ohio train derailment'
    fetch_news(api_key, keyword)

# Read sample data
df = pd.read_excel('news_data_sample.xlsx')

# Calculate sentiment for each news title
df['sentiment'] = df['Title'].apply(lambda title: TextBlob(title).sentiment.polarity)

# Calculate average sentiment
average_sentiment = df['sentiment'].mean()
print("Average sentiment:", average_sentiment)



# part 2: record news volume and conduct trend analysis
# Initialize GoogleNews
googlenews = GoogleNews(lang='en', region='US')

# Define start and end dates
start_date = '02/01/2023'
end_date = '04/22/2023'

start_date = datetime.strptime(start_date, '%m/%d/%Y')
end_date = datetime.strptime(end_date, '%m/%d/%Y')
current_date = start_date

# Create an empty DataFrame to store the data for each day
df = pd.DataFrame(columns=['Date', 'News Volume'])

while current_date <= end_date:
    # Format current_date and next_date as strings
    current_date_str = current_date.strftime('%m/%d/%Y')
    next_date = current_date + timedelta(days=1)
    next_date_str = next_date.strftime('%m/%d/%Y')

    # Instantiate the GoogleNews object with the current date and next date
    googlenews = GoogleNews(start=current_date_str, end=next_date_str)

    # Search for news
    googlenews.search('ohio train derailment')

    print(current_date_str, googlenews.total_count())

    # Append the data for the current day to the DataFrame
    df = df.append({'Date': current_date_str, 'News Volume': googlenews.total_count()}, ignore_index=True)

    # Add one day to the date
    current_date = next_date

# Write the DataFrame to an Excel file
df.to_excel('news_volume_byday.xlsx', index=False)

# trend analysis

# Read the data from the Excel file
df = pd.read_excel('news_volume_byday.xlsx')

# Convert the 'Date' column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Set the plot style
sns.set(style='darkgrid')

# Create a line plot with date on the x-axis and news volume on the y-axis
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='News Volume')

# Customize the plot
plt.title('News Volume Over Time for "Ohio Train Derailment"')
plt.xlabel('Date')
plt.ylabel('News Volume')

# Show the plot
plt.show()