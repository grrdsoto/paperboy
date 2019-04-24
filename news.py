from newsapi import NewsApiClient
import requests
import pprint

# Init
newsapi = NewsApiClient(api_key='0d8fe10ac2ff464bb70e631287fa5009')
url = 'https://newsapi.org/v2/everything?'
#/v2/top-headlines
url = ('https://newsapi.org/v2/everything?'
       'q=notre-dame&'
       'from=2019-04-16&'
       'sortBy=popularity&'
       'apiKey=0d8fe10ac2ff464bb70e631287fa5009')
       
sources = newsapi.get_sources()
response = requests.get(url, params=url)
response_json = response.json()
pprint.pprint(response_json)
class NewsForm(newsapi):
