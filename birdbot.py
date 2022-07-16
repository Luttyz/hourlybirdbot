import json
import requests
import shutil 
import telegram_send
import numpy as np
import tweepy

# grab the image's link from the shibe.online bird image API
jsonData = requests.get('https://shibe.online/api/birds')

# change that request's data to text so we can modify it after
gay = jsonData.text

# this modifies the request's text as to get rid of the different characters that would annoy us when later downloading the image
url = gay.replace('[', '').replace(']','').replace('\"','')

# set the image's name to bird.jpg as... well, it *is* a bird after all
filename = 'bird.jpg'

r = requests.get(url, stream = True)

# This part definitely wasn't copy pasted and I definitely do understand what it does yes yes

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image couldn\'t be downloaded')


# Send through Telegram API to your group

with open("bird.jpg", "rb") as f:
    telegram_send.send(images=[f], captions=[url])

# Send through Twitter API
# Depending on where you want your bot to send things, you can either uncomment this part or the first part.

# Insert your different Twitter API keys here
consumer_key='SET YOUR OWN CONSUMER KEY HERE'
consumer_secret_key='SET YOUR OWN SECRET KEY HERE'
access_token='SET YOUR OWN ACCESS TOKEN HERE'
access_token_secret='SET YOUR OWN SECRET ACCESS TOKEN HERE'

# This sets the API keys into Tweepy's settings
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

# idk
imagePath = filename

# Generate text tweet with image
api.update_status_with_media(filename = imagePath, status = url)