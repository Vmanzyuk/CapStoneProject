import requests
import datetime
from .models import Token, Token_price
from ActualTokenList.passwords import CMC_PRO_API_KEY


def fill_main_info():
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
            Token.objects.create(cmc_id=i['id'],name=i['name'],symbol=i['symbol'],circulating_supply=i['circulating_supply'],
                total_supply=i['total_supply'],max_supply=i['max_supply'])
    else:
        logfile = open('log.txt','a')
        logfile.write('{} fill_main_info, status code={}'.format(str(datetime.datetime.now()),r.status_code))

def fill_additional_info():
    cmc_identificators = ''
    for i in Token.objects.all():
        cmc_identificators+=str(i.cmc_id)+','
    cmc_identificators = cmc_identificators[:-1]

    payload2 = {'id':cmc_identificators,'CMC_PRO_API_KEY':CMC_PRO_API_KEY}
    r2 = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?', params=payload2)
    if r2.status_code==200:
        req2json = r2.json()

        for i in Token.objects.all():
            if len(req2json['data'][str(i.cmc_id)]['urls']['website'])!=0:
                i.website = req2json['data'][str(i.cmc_id)]['urls']['website'][0]
            else:
                pass

            if len(req2json['data'][str(i.cmc_id)]['urls']['twitter'])!=0:
                i.twitter = req2json['data'][str(i.cmc_id)]['urls']['twitter'][0]
            else:
                pass

            if len(req2json['data'][str(i.cmc_id)]['urls']['reddit'])!=0:
                i.reddit = req2json['data'][str(i.cmc_id)]['urls']['reddit'][0]
            else:
                pass

            if len(req2json['data'][str(i.cmc_id)]['logo'])!=0:
                i.logo = req2json['data'][str(i.cmc_id)]['logo']
            else:
                pass

            if len(req2json['data'][str(i.cmc_id)]['urls']['explorer'])!=0:
                i.explorer = req2json['data'][str(i.cmc_id)]['urls']['explorer'][0]
                for g in req2json['data'][str(i.cmc_id)]['urls']['explorer']:
                    if g.find('etherscan')!=-1:
                        i.blockchain = 'Ethereum'
                        i.smart_contract_address = g[-42:]
            else:
                pass

            i.save()
    else:
        logfile = open('log.txt','a')
        logfile.write('{} fill_additional_info, status code={}'.format(str(datetime.datetime.now()),r2.status_code))

