from urllib.request import urlopen 
from urllib.parse import urlencode, unquote, quote_plus
import urllib 
import requests 
import json

def jsonReturn():
    url = 'http://apis.data.go.kr/1262000/CountryCovid19SafetyServiceNew/getCountrySafetyNewsListNew'
    serviceKey = 's1RQAGpmziXf5us4w%2FmB5M9zN4yk%2B6M8R4EMVxxpuB1S0XILvxtzuNq5wuP21TNCwBm%2BLhe8WKc9IJxB7oW%2FAQ%3D%3D'
    queryParams = '?' + urlencode({ 
        quote_plus('ServiceKey') : serviceKey, 
        quote_plus('returnType') : 'JSON', 
        quote_plus('numOfRows') : '1',
    })

    get_data = requests.get(url + unquote(queryParams))
    result_data = get_data.json()
    return json.dumps(result_data['data'], ensure_ascii=False)

print(jsonReturn())
