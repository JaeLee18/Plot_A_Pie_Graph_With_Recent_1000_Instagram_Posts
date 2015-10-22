#
#
# To see a pie graph
# Go to
#https://plot.ly/~lee2161/29/capitalone-trending-with-recent-1000-instagram-posts/

from instagram.client import InstagramAPI
import urllib2
import urllib
import json

import plotly.plotly as py
import plotly.graph_objs as go
#Constants to check the number of Post.
positive = 0
negative = 0
netural = 0

#Keys for Instagram API
access_token = "1997307189.6b69e77.ef755b6606bf4e7e9b1c452587eaaaba"
client_secret = "c760225bb9cf43c89105a63f746846a5"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)

#Get recent 20 posts which have #CapitalOne
url = 'https://api.instagram.com/v1/tags/CapitalOne/media/recent?access_token=1997307189.1fb234f.53a2d32698954f1087d3a1f23449c2ed'

#Load the result.
json_file = urllib2.urlopen(url)
json_data = json.load(json_file)




no_emoji = [ ] #no_emoji -> An array which is exactly same as 'text' array but it does not have any emojis.
response = [ ]
text = [ ]
next_url = [ ]

# Get Recent 1000 Instagram Posts and Analyze each post whether it is positive, negative or
# positive toward Capital One.
for k in range(50):
    for j in range(20):
        text.append(json_data["data"][j]["caption"]["text"])

    for i in range(20):
        no_emoji.append(text[i].encode('ascii', 'ignore').decode('ascii'))
        text_encode = urllib.urlencode({"text": no_emoji[i]}) 
        text_data = urllib2.urlopen("http://text-processing.com/api/sentiment/", text_encode)
        text_json_data = json.load(text_data)
        response.append(text_json_data["label"])
        if (response[i] == "pos"):
            positive += 1
        elif (response[i] == "neg"):
           negative += 1
        else:
            netural += 1
            
url = json_data["pagination"]["next_url"]
json_file = urllib2.urlopen(url)
json_data = json.load(json_file)

# Empty text, no_emoji, response Array .
del text[:]
del no_emoji[:]
del response[:]

percent_positive = str(((float)(positive)/float(1000))*100) + "%"
percent_negative = str(((float)(negative)/float(1000))*100) + "%"
percent_netural = str(((float)(netural)/float(1000))*100) + "%"
    
    
print "\n#----------------------------------------#CapitalOne Anaylsis Summary------------------------------------#"
print "      - Number of Positive Posts: " + str(positive) 
print "      - Number of Negative Posts: " + str(negative)
print "      - Number of Netural Posts:  " + str(netural) + "\n"
print "      - Percentage of Positive Posts in 1000 Posts: " + percent_positive
print "      - Percentage of Negative Posts in 1000 Posts: " + percent_negative
print "      - Percentage of Netural Posts in 1000 Posts:  " + percent_netural
print "#---------------------------------------------------------------------------------------------------------------#"

fig = {
    'data': [{'labels': ['Positive', 'Negative', 'Netural'],
              'values': [positive, negative, netural],
              'type': 'pie'}],
    'layout': {'title': '#CapitalOne Trending with recent 1000 Instagram Posts.'}
}

url = py.plot(fig, filename='Lee_JaeJoong')

