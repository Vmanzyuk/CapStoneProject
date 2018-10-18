import requests
import datetime
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
    if r.status_code==200:
        reqjson = r.json()

        for i in reqjson['data']:
            try:
                token = Token.objects.get(cmc_id=i['id'])
                obj = Token_price(token_id=token.id,cmc_usd_price=i['quote']['USD']['price'],cmc_usd_upd_date=i['quote']['USD']['last_updated'])
                obj.save()
            except Token.DoesNotExist:
                pass
    else:
        logfile = open('log.txt','a')
        logfile.write('{} cmc_update_usd_price, status code={}'.format(str(datetime.datetime.now()),r.status_code))





