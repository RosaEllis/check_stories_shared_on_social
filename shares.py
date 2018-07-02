'''
    share.py - this program retrieves share counts from a list of social networks
    for a given URL
'''
import requests, json                               # the added libraries to retrieve urls and process json results

target_url = 'http://trackyourpoliceworkforce.org/'
apis = ['http://graph.facebook.com/?id=', 'https://www.linkedin.com/countserv/count/share?format=json&url=']

print 'fetching share counts for ' + target_url     # give some feedback to the user

for api in apis:                                    # for each item (api) in the list (apis) repeat the following indented section

    url = api + target_url                          # join the two strings together to make a valid call to the api

    try:
        content = requests.get(url).json()          # fetch the data

        if 'facebook' in url:
             print 'FaceBook shares ', content['share']['share_count']

        if 'linkedin' in url:
            print 'Linked in shares ', content['count']

    except Exception as e:
        print e
