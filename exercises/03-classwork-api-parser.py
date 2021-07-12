#!/usr/bin/env python
# coding: utf-8

# # Web scraping: headers, the networks tab and parsing an API URL
# ## Helpful links and resources
# - [urllib](https://docs.python.org/3/library/urllib.parse.html#) is a Python library that will pick apart URLs
# - [Sessions object - request library](https://docs.python-requests.org/en/master/user/advanced/#session-objects)

# In[2]:


#import libraries
from urllib.parse import urlparse
import requests


# ## The networks tab
# ### Static data files
# [Covid cases in the US - New York Times](https://www.nytimes.com/interactive/2021/us/covid-cases.html)

# In[3]:


# get static data file
covid_cases_r = requests.get('https://static01.nyt.com/newsgraphics/2021/coronavirus-tracking/data/pages/usa/data.json')


# In[4]:


covid_cases = covid_cases_r.json()


# In[6]:


#covid_cases


# ### "Secret" APIs
# Shopping websites are good candidates for secret APIs, such as [Target](www.target.com)
# 
# #### Target's Search API

# In[10]:


# search for an item with the networks tab open to ID which APIs you can use
target_search_url = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&channel=WEB&count=24&default_purchasability_filter=false&include_sponsored=true&keyword=pool+float&offset=0&page=%2Fs%2Fpool+float&platform=desktop&pricing_store_id=3991&useragent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_6%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F91.0.4472.114+Safari%2F537.36&visitor_id=017A8089E1D702019EF771AEBB6A55D6"


# In[11]:


# parse the URL so it's easier to read
parsed_url = urlparse(target_search_url)


# In[12]:


# check the parsed URL
parsed_url


# In[13]:


# format the endpoint and parameters
target_search_endpoint = parsed_url[0] + '://' + parsed_url[1] + parsed_url[2]
target_search_endpoint


# In[16]:


parsed_url[4]


# In[14]:


#identify params
target_search_parameters = {}
for key_value in parsed_url[4].split('&'):
    key_value_list = key_value.split('=')
    target_search_parameters[key_value_list[0]] = key_value_list[1]


# In[15]:


target_search_parameters


# In[18]:


# get request with endpoint and params
target_search_r = requests.get(target_search_endpoint, params=target_search_parameters)
target_search_r


# In[19]:


#get the json file
response = requests.get(target_search_endpoint, params=target_search_parameters)
data = response.json()


# In[40]:


data['data']['search']['products'][0]['item']['product_description']['title']


# In[47]:


# change something in the parameters (like keyword)
target_search_parameters1 = target_search_parameters
target_search_parameters['keyword'] = 'drinking+glass'
target_search_parameters['page'] = '%2Fs%2Fdrinking+glass'
target_search_parameters1


# In[48]:


#get new data via requests
target_search_r1 = requests.get(target_search_endpoint, params=target_search_parameters1)
target_search_r1


# In[49]:


#store as json
response1 = requests.get(target_search_endpoint, params=target_search_parameters1)
data1 = response1.json()


# In[52]:


# drill down the json file
data1.keys()


# In[53]:


# drill down some more
#data1['data']['search']['products'][0]
data1['data']['search']['products'][0]['item']['product_description']['title']


# In[70]:


#get the list of title of the items 
for product in data1['data']['search']['products']:
    print (product['item']['product_description']['title'])


# #### Target's aggregation API

# In[3]:


# parse the URL so it's easier to read


# In[2]:


# check the parsed URL


# In[197]:


# format the endpoint and parameters


# In[198]:


# change something in the parameters (like tcins)


# In[199]:


# get request with endpoint and params


# In[1]:


# drill down the json file


# In[4]:


# drill down some more


# ## Using sessions to login
# ### Accessing password-protected pages
# [Sessions object - request library](https://docs.python-requests.org/en/master/user/advanced/#session-objects)

# In[170]:


# open up a session so that your login credentials are saved


# In[171]:


# load in config file with passwords


# In[172]:


# check the website for the login parameters


# In[173]:


# post the payload to the site to login with the correct log in endpoint


# In[174]:


# check credentials to see if successful


# In[175]:


# look at an example page to get you started with a query


# In[177]:


# create a new post object from the example


# In[ ]:


# post request for the data


# In[179]:


# check to see what is returned

