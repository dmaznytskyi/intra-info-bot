# redirect links:
#     https://web.telegram.org/#/im?p=@intra_info_bot
#     tg://join?invite=<invite_key>
#     tg://resolve?domain=<USERNAME>

import requests
import json

uid = ""
secret = ""

token_post = requests.post("https://api.intra.42.fr/oauth/token", data={'grant_type':'client_credentials','client_id':uid,'client_secret':secret})
data = json.loads(token_post.text)
acto = data['access_token']
exin = data['expires_in']
crat = data['created_at']
# print acto
# print exin
# print crat

test = requests.get("https://api.intra.42.fr/v2/users/22719", params={'access_token':acto})
data = json.loads(test.text)
# print test.text
print data['campus']
# users/:id22719
# get = requests.get("https://api.intra.42.fr/oauth/token", params={uid, secret})
# print get
