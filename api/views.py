from django.shortcuts import render
from django.http import HttpResponse
from TokensDB.models import Token, Token_price
from django.http import JsonResponse
from django.db.models import Max

def get_cryptocurrency_test(request):
    data = []

    for token_price in Token_price.objects.filter(token__name__in=['0x','0xBitcoin']).order_by('-cmc_usd_upd_date'):
        data.append({ 'name': token_price.token.name, 'symbol': token_price.token.symbol,'cmc_usd_price':token_price.cmc_usd_price,'cmc_usd_upd_date': token_price.cmc_usd_upd_date })

#    for token in Token.objects.filter(name='ZrCoin'):
#        result.append({ 'name': token.name, 'symbol': token.symbol })

    return JsonResponse({'data': data})

def get_cryptocurrency_info(request):
    data = []

    for i in Token.objects.all():
    	max_date = Token_price.objects.filter(token_id=i.id).aggregate(Max('cmc_usd_upd_date'))
    	last_token_price_queryset = Token_price.objects.filter(token_id = i.id) & Token_price.objects.filter(cmc_usd_upd_date=max_date['cmc_usd_upd_date__max'])
    	last_token_price_obj = last_token_price_queryset.get()


    	data.append({ 'name': i.name, 'symbol': i.symbol, 'circulating_supply' : i.circulating_supply,
    	'total_supply': i.total_supply, 'max_supply' : i.max_supply, 'coinmarketcap_id' : i.cmc_id,
    	'explorer': i.explorer, 'blockchain' : i.blockchain, 'smart_contract_address' : i.smart_contract_address,
    	'website' : i.website, 'twitter' : i.twitter, 'reddit' : i.reddit, 'logo_link' : i.logo_link,
    	'coinmarketcap_usd_price' : last_token_price_obj.cmc_usd_price, 'coinmarketcap_usd_upd_date' : last_token_price_obj.cmc_usd_upd_date })

#    for token in Token.objects.filter(name='ZrCoin'):
#        result.append({ 'name': token.name, 'symbol': token.symbol })

    return JsonResponse({'data': data})
# Create your views here.