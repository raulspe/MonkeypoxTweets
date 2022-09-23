#!pip install snscrape
#!pip install pandas

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "monkeypox"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    for tweet in sntwitter.TwitterUserScraper(tweet.user.id):
        print(vars(tweet))
        break
