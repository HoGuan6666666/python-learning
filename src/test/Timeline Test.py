import json

import requests
from requests_oauthlib import OAuth1


# url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
# client_key = "2y0768YuRTBbacyLM7fsLuKFf"
# client_secret = "sOYwyxxDKjjY3JUz86FcQPgyXeDTZgjXKmuNS8NDTypP4Gw3Ya"
# token = "930184010709504000-KRoUdtd1hpOSeHD40xJBqyFwliPpcvH"
# token_secret = "iPWdUjf5kvCFk0aujfkDYwB4RsDUctmu5Jgoq45jiJbRz"
# auth = OAuth1(client_key=client_key, client_secret=client_secret, resource_owner_key=token, resource_owner_secret=token_secret)
# print requests.get(url, auth = auth).content


url = "https://api.twitter.com/1.1/statuses/update.json"
client_key = "2y0768YuRTBbacyLM7fsLuKFf"
client_secret = "sOYwyxxDKjjY3JUz86FcQPgyXeDTZgjXKmuNS8NDTypP4Gw3Ya"
token = "930184010709504000-KRoUdtd1hpOSeHD40xJBqyFwliPpcvH"
token_secret = "iPWdUjf5kvCFk0aujfkDYwB4RsDUctmu5Jgoq45jiJbRz"
auth = OAuth1(client_key=client_key, client_secret=client_secret, resource_owner_key=token, resource_owner_secret=token_secret)
param = {'status' : 'heiheiheiheih'}
req = requests.post(url,auth=auth, params=param)
json_data = req.json()
assert json_data['text'] == "heiheiheiheih"
print json_data['text']