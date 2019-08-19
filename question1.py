import requests
import json

####
# inputs
####
username = 'Xalipso21'




url = 'https://api.github.com/users/Xalipso21'
gh_session = requests.Session()
dict1 = json.loads(gh_session.get(url).text)
print (dict1["bio"])
    