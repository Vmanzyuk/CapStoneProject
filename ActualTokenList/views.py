from django.shortcuts import render
from django.http import HttpResponse
from TokensDB.models import Token, Token_price
from django.http import JsonResponse

def get_cryptocurrency_info(request):
    result = []

    for token_price in Token_price.objects.filter(token__name__in=['0x','0xBitcoin']).order_by('-cmc_usd_upd_date'):
        result.append({ 'name': token_price.token.name, 'symbol': token_price.token.symbol,'cmc_usd_price':token_price.cmc_usd_price,'cmc_usd_upd_date': token_price.cmc_usd_upd_date })

#    for token in Token.objects.filter(name='ZrCoin'):
#        result.append({ 'name': token.name, 'symbol': token.symbol })

    return JsonResponse({'result': result})
# Create your views here.
