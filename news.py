from newsapi import NewsApiClient
import requests
import pprint
import time
from datetime import date

# Init
# newsapi = NewsApiClient(api_key='0d8fe10ac2ff464bb70e631287fa5009')
# url = 'https://newsapi.org/v2/everything?'
#/v2/top-headlines
# url = ('https://newsapi.org/v2/everything?'
#        'q=breaking-news&'
#        'from=2019-04-16&'
#        'sortBy=popularity&'
#        'apiKey=0d8fe10ac2ff464bb70e631287fa5009')
       
# sources = newsapi.get_sources()
# response = requests.get(url, params=url)
# response_json = response.json()
# pprint.pprint(response_json)
class news():
       def __init__(self):
              self.query='breaking-news'
              self.time=date.today()
              self.sortBy='popularity'
              self.articles=[]
       def update(self,query=None,time=None,sortby=None):
              if query:              self.query=query.replace(' ','-')
              if time:              self.time=time
              if sortby:              self.sortBy=sortby
              url = 'https://newsapi.org/v2/everything?q={0}&from={1}&sortBy={2}&apiKey=0d8fe10ac2ff464bb70e631287fa5009'.format(self.query, self.time,self.sortBy)
              response = requests.get(url,params=url)
              response_json = response.json()
              self.articles=response_json
              # pprint.pprint(self.articles)
              # pprint.pprint(response_json)
              # with open('news.json', 'w') 
              
              # f.write(response_json) #this will put the info in the file

              # f.close() #this will close the file handler. AKA free the used memory
          
# news().update()



       

