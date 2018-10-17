from django.db import models

class Token(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    circulating_supply = models.FloatField(null=True,blank=True)
    total_supply = models.FloatField(null=True,blank=True)
    max_supply = models.FloatField(null=True,blank=True)
    cmc_id = models.IntegerField(null=True,blank=True)
    explorer = models.CharField(null=True,max_length=200,blank=True)
    blockchain = models.CharField(null=True,max_length=200,blank=True)
    smart_contract_address = models.CharField(null=True,max_length=200,blank=True)
    website = models.CharField(null=True,max_length=200,blank=True)
    reddit = models.CharField(null=True,max_length=200,blank=True)
    twitter = models.CharField(null=True,max_length=200,blank=True)
    logo_link = models.CharField(null=True,max_length=500,blank=True)

class Token_price(models.Model):
    token = models.ForeignKey(Token,on_delete=models.CASCADE)
    cmc_usd_upd_date = models.DateTimeField(null=True)
    cmc_usd_price = models.FloatField(null=True)
    cmc_btc_upd_date = models.DateTimeField(null=True,blank=True)
    cmc_btc_price = models.FloatField(null=True,blank=True)
