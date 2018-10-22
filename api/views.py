from django.shortcuts import render
from django.http import HttpResponse
from TokensDB.models import Token, Token_price
from django.http import JsonResponse
from django.db.models import Max

def get_cryptocurrency_test(request):
    data = []

    for i in Token.objects.all():
    	last_token_price_obj = Token_price.objects.filter(token_id=i.id).order_by('-cmc_usd_upd_date').last()


    	data.append({ 'name': i.name, 'symbol': i.symbol, 'circulating_supply' : i.circulating_supply,
    	'total_supply': i.total_supply, 'max_supply' : i.max_supply, 'coinmarketcap_id' : i.cmc_id,
    	'explorer': i.explorer, 'blockchain' : i.blockchain, 'smart_contract_address' : i.smart_contract_address,
    	'website' : i.website, 'twitter' : i.twitter, 'reddit' : i.reddit, 'logo_link' : i.logo_link,
    	'coinmarketcap_usd_price' : last_token_price_obj.cmc_usd_price, 'coinmarketcap_usd_upd_date' : last_token_price_obj.cmc_usd_upd_date })


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


    return JsonResponse({'data': data})
