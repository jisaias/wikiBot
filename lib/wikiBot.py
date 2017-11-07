import pytumblr
import random
import time
import os

USERNAME = "wikibot"

#For the sake of secrecy regarding API Keys
C_KEY = os.environ.get("CONSUMER_KEY")
C_SECRET = os.environ.get("CONSUMER_SECRET")
O_TOKEN = os.environ.get("OAUTH_TOKEN")
O_SECRET = os.environ.get("OAUTH_TOKEN_SECRET")

def readMessage():
  # Authenticate via OAuth
    client = pytumblr.TumblrRestClient(
      C_KEY,
      C_SECRET,
      O_TOKEN,
      O_SECRET
    )
    
    message = client.submission(USERNAME)['posts'][0]['question']
    
    return message
    
    

def postAThing(URL, para, message):
    # Authenticate via OAuth
    client = pytumblr.TumblrRestClient(
      C_KEY,
      C_SECRET,
      O_TOKEN,
      O_SECRET
    )
    
    ask = client.submission(USERNAME)['posts'][0]
    
    
    
    response = '\n\n' + para + '\n\n' + URL
    
    client.edit_post(USERNAME, id=ask['id'], answer=response, state = 'published')