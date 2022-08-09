#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pandas --quiet')
get_ipython().system('pip install tweepy --quiet')
get_ipython().system('pip install wordcloud --quiet')


# In[3]:


import pandas as pd
import tweepy
import matplotlib.pyplot as plt


# In[4]:


bearer_token = #bearertoken
client = tweepy.Client(bearer_token)


# In[29]:


query = 'monkeypox fag -is:retweet'
response = client.search_recent_tweets(query=query, tweet_fields=['id', 'text', 'author_id', 'created_at', 'lang', 'geo', 'public_metrics', 'source'], max_results=10)


# In[31]:


for tweet in response.data:
    print(tweet.id)
    print(tweet.text)
    print(tweet.author_id)
    print(tweet.created_at)
    print(tweet.lang)
    print(tweet.geo)
    print(tweet.public_metrics)
    print(tweet.source)


# In[37]:


tweets_values = [[tweet.id, tweet.text, tweet.created_at, tweet.lang, tweet.geo, tweet.public_metrics, tweet.source] for tweet in response.data]
df = pd.DataFrame(tweets_values, columns=['Tweet_ID', 'Tweet', 'Created At', 'Language', 'Localization', 'Public Metrics', 'Source'])
df.head()


# In[38]:


df.to_csv(r"C:\Users\rauls\Desktop\tweets.csv", index = False, header=True)


# In[ ]:




