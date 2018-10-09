import requests
from .models import Token
from ActualTokenList.passwords import CMC_PRO_API_KEY

def fill_main_info():
# Variables for coinmarketcap API method
    sort = 'name'
    start = '1'
    limit = '3'
    cryptocurrency_type ='tokens'
    convert = 'USD'
 #   CMC_PRO_API_KEY = 'b51ef67e-59f8-4e82-8b63-d26939e97b1b'

    payload = {
                'sort':sort,'start':start,'limit':limit,'cryptocurrency_type':cryptocurrency_type,
                'convert':convert,'CMC_PRO_API_KEY':CMC_PRO_API_KEY
              }

    r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?', params=payload)
    a = r.json()

    for i in a['data']:
        Token.objects.create(cmc_id=i['id'],name=i['name'],symbol=i['symbol'],circulating_supply=i['circulating_supply'],total_supply=i['total_supply'],max_supply=i['max_supply'])

