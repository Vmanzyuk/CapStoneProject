import requests
from TokensDB.models import Token_price, Token
from ActualTokenList.passwords import CMC_PRO_API_KEY


def cmc_update_usd_price():
# Variables for coinmarketcap API method
    sort = 'name'
    start = '1'
    limit = '2000'
    cryptocurrency_type ='tokens'
    convert = 'USD'

    payload = {
                'sort':sort,'start':start,'limit':limit,'cryptocurrency_type':cryptocurrency_type,
                'convert':convert,'CMC_PRO_API_KEY':CMC_PRO_API_KEY
              }

    r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?', params=payload)
    reqjson = r.json()

    for i in reqjson['data']:
        token = Token.objects.filter(cmc_id=i['id']).first()
        tp_obj = Token_price.objects.filter(Token=token).first()
        tp_obj.cmc_usd_price = i['quote']['USD']['price']
        tp_obj.cmc_usd_upd_date = i['quote']['USD']['last_updated']
        tp_obj.save()


