import feedparser
from datetime import timezone,datetime
from typing import List
import requests
from bs4 import BeautifulSoup
ARXIV_FEEDS =[
    "http://export.arxiv.org/rss/cs.AI",
    "http://export.arxiv.org/rss/cs.LG"
]

def collect_arxiv():
  items =[]
  for feed_url in ARXIV_FEEDS :
    feed = feedparser.parse(feed_url)
  for entry in feed.entries:
    title = entry.title
    abstract = entry.summary
    url = entry.link
    # Ensure published_at is timezone-aware (UTC)
    published= datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
    items.append(
              RawItem(
                title = title,
                source= "arXiV",
                abstract = abstract,
                url = url,
                published_at= published

              )
        )
  return items
# anthropic collector
Anthropic_blog = "https://www.anthropic.com/news"
def collect_anthropic():
  items = []
  html = requests.get(Anthropic_blog, timeout = 10).text
  soup = BeautifulSoup(html, "html.parser")
  links = soup.select("a[href^='/news/']")

  for link in links[:10]:
    url = "https://www.anthropic.com"+ link ["href"]
    page = requests.get(url,timeout= 10).text
    psoup = BeautifulSoup(page,"html.parser")
    title = psoup.find("h1").get_text(strip = True)
    paragraphs = psoup.find_all("p")[:3]
    abstract = " ".join(p.get_text(strip=True) for p in paragraphs)
    items.append(
        RawItem(
            title = title,
            source ="anthropic",
            abstract = abstract,
            url = url,
            published_at = datetime.now(timezone.utc)
        )
    )
  return items
#deepmind collector
deepmind_blog ="https://deepmind.google/discover/blog"
def collect_deepmind():
  items= []
  html = requests.get(deepmind_blog,timeout = 10).text
  soup = BeautifulSoup(html,"html.parser")
  links = soup.select("a[href^='discover/blog']")
  for link in links[:10]:
    url = "https://deepmind.google"+link["href"]
    page = requests.get(url,timeout= 10).text
    psoup = BeautifulSoup(page,"html.parser")
    title = psoup.find("h1".get_text(strip = True))
    paragraphs= psoup.find_all("p")[:3]
    abstract = " ".join(p.get_text(strip = True)for p in paragraphs)

    items.append(
        RawItem(
            title = title,
            source = "deepmind",
            abstract = abstract,
            url = url,
            published_at = datetime.now(timezone.utc)
        )
    )
  return items
NEWS_FEED =[
    "https://www.technologyreview.com/feed"

]
def collect_news():
  items = []
  for feed_url in NEWS_FEED:
    feed = feedparser.parse(feed_url)
  for entry in feed.entries:
    title = entry.title
    url = entry.link
    abstract = entry.summary
    published = datetime(*entry.published_parsed[:6], tzinfo = timezone.utc)
    items.append(
        RawItem(
            title = title,
            source = "News",
            abstract = abstract,
            url = url,
            published_at = published
        )
    )
  return items