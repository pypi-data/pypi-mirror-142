import json
import requests

with open('base.json', 'r', encoding='utf-8') as f:
    site = json.load(f)
    api_list = []
    for key, value in site.items():
        api_list.append(value['api'])
        ## print(value['api'])
        r = requests.get(value['api'])
        print(value['api'], r.status_code)
