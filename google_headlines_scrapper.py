# pip install these below in terminal
# 
# pip install feedparser
# pip install pandas
# 
# Run - python google_headlines_scrapper.py
# 

import feedparser
from datetime import datetime
import pandas as pd

# Dates are set for the week of code creation. Need to sort out dates to call url, perhaps given from front-end or selects current week? 
start_date = datetime(2024, 3, 25)
end_date = datetime(2024, 3, 31)

rss_url = "https://news.google.com/rss/search?q=%22S%26P+500%22+OR+%22SPX%22+OR+%22$SPY%22&hl=en-US&gl=US&ceid=US:en"
feed = feedparser.parse(rss_url)

articles = []

for entry in feed.entries:
    published_date = datetime(*entry.published_parsed[:6])
    
    if start_date <= published_date <= end_date:
        articles.append({
            'Title': entry.title,
            # 'Link': entry.link,
            'Published': published_date.strftime('%Y-%m-%d %H:%M:%S'),
        })

df_articles = pd.DataFrame(articles)

print(df_articles.head())

output_file_name = 'google_news_headlines.csv'
df_articles.to_csv(output_file_name, index=False)

print(f"Filtered and saved {len(articles)} articles to {output_file_name}.")
