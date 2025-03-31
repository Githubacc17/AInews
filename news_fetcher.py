from newsapi import NewsApiClient
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

class NewsFetcher:
    def __init__(self):
        self.api_key = os.getenv('NEWS_API_KEY')
        self.newsapi = NewsApiClient(api_key=self.api_key)

    def fetch_tech_news(self):
        """Fetch technology news from the last 24 hours"""
        try:
            # Get yesterday's date
            yesterday = datetime.now() - timedelta(days=1)
            yesterday_str = yesterday.strftime('%Y-%m-%d')

            # Fetch news
            tech_news = self.newsapi.get_everything(
                q='technology OR artificial intelligence OR programming OR cybersecurity',
                language='en',
                from_param=yesterday_str,
                sort_by='relevancy',
                page_size=10
            )

            # Process and return articles
            articles = []
            for article in tech_news['articles']:
                articles.append({
                    'title': article['title'],
                    'description': article['description'],
                    'url': article['url'],
                    'source': article['source']['name'],
                    'published_at': article['publishedAt'],
                    'urlToImage': article.get('urlToImage', None)
                })

            return articles

        except Exception as e:
            print(f"Error fetching news: {str(e)}")
            return [] 