from bs4 import BeautifulSoup
from facepy import GraphAPI
from random import shuffle
import time
import urllib2
import urlparse

import warnings



warnings.filterwarnings('ignore', category=DeprecationWarning)


client_id     = "CLIENT_ID"
client_secret = "CLIENT_SECRET"
grant_type    = "client_credentials"
message_number = 5
fb_userid = "FB_USERID"
send_delay = 60

accessTokenUrl = "https://graph.facebook.com/oauth/access_token?client_id="+client_id+"&client_secret=16ebdba77e4d183f025bc1a2269d7fe1"+"&grant_type="+grant_type
oauth_response = urllib2.urlopen(accessTokenUrl).read()
try:
    oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
except KeyError:
    print('Unable to grab an access token!')
    exit()


def getBattuteGroucho(domContent):
    
    questionBoxes = domContent.find_all("words")
    retList = []
    for box in questionBoxes:
        wd = box.get_text().encode('utf-8')
        retList.append(wd.strip())
    return retList

facebook_graph = GraphAPI(oauth_access_token)
graph = GraphAPI(oauth_access_token)

with open('battute.xml', 'r') as content_file:
    content = content_file.read()

    siteContent = content
    domContent = BeautifulSoup(siteContent)

    bt = getBattuteGroucho(domContent)
    for i in range(1,message_number):
        shuffle(bt)
        print bt[0]
        graph.post(fb_userid+'/feed', message=bt[0])
        
        
        time.sleep(send_delay)
