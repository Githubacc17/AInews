import wikipedia
import feedparser
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import json
from datetime import timezone

load_dotenv()

class MultiSourceFetcher:
    def __init__(self):
        self.setup_apis()

    def setup_apis(self):
        """Setup API clients for different sources"""
        # NewsAPI setup
        self.newsapi = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))

    def fetch_newsapi_articles(self):
        """Fetch articles from NewsAPI"""
        try:
            yesterday = datetime.now(timezone.utc) - timedelta(days=1)
            yesterday_str = yesterday.strftime('%Y-%m-%d')
            
            tech_news = self.newsapi.get_everything(
                q='technology OR artificial intelligence OR programming OR cybersecurity',
                language='en',
                from_param=yesterday_str,
                sort_by='relevancy',
                page_size=5
            )
            
            return [{
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'source': article['source']['name'],
                'published_at': article['publishedAt'],
                'urlToImage': article.get('urlToImage', None),
                'type': 'news'
            } for article in tech_news['articles']]
        except Exception as e:
            print(f"Error fetching from NewsAPI: {str(e)}")
            return []

    def fetch_wikipedia_tech(self):
        """Fetch latest technology articles from Wikipedia"""
        try:
            tech_topics = ["Artificial intelligence", "Machine learning", 
                          "Cloud computing", "Blockchain"]
            wiki_articles = []
            
            for topic in tech_topics:
                try:
                    page = wikipedia.page(topic)
                    summary = wikipedia.summary(topic, sentences=2)
                    
                    wiki_articles.append({
                        'title': f"Wikipedia: {page.title}",
                        'description': summary,
                        'url': page.url,
                        'source': 'Wikipedia',
                        'published_at': datetime.now(timezone.utc).isoformat(),
                        'urlToImage': None,
                        'type': 'wikipedia'
                    })
                except:
                    continue
            return wiki_articles
        except Exception as e:
            print(f"Error fetching from Wikipedia: {str(e)}")
            return []

    def fetch_times_of_india(self):
        """Fetch technology news from Times of India RSS feed"""
        try:
            toi_tech_feed = "https://timesofindia.indiatimes.com/rssfeeds/66949542.cms"
            feed = feedparser.parse(toi_tech_feed)
            
            articles = []
            for entry in feed.entries[:5]:
                # Clean up HTML content using BeautifulSoup
                soup = BeautifulSoup(entry.summary, 'html.parser')
                clean_description = soup.get_text().strip()
                
                # Remove any HTML from title as well
                title_soup = BeautifulSoup(entry.title, 'html.parser')
                clean_title = title_soup.get_text().strip()
                
                articles.append({
                    'title': clean_title,
                    'description': clean_description,
                    'url': entry.link,
                    'source': 'Times of India',
                    'published_at': datetime.now(timezone.utc).isoformat(),
                    'urlToImage': None,
                    'type': 'times_of_india'
                })
            
            return articles
        except Exception as e:
            print(f"Error fetching from Times of India: {str(e)}")
            return []

    def fetch_all_news(self):
        """Fetch news from all sources"""
        all_articles = []
        
        # Fetch from all sources
        all_articles.extend(self.fetch_newsapi_articles())
        all_articles.extend(self.fetch_wikipedia_tech())
        all_articles.extend(self.fetch_times_of_india())
        
        # Sort by published date
        all_articles.sort(
            key=lambda x: datetime.fromisoformat(x['published_at'].replace('Z', '+00:00')),
            reverse=True
        )
        
        return all_articles 