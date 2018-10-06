from django.db import models

class Token(models.Model):
	name = models.CharField(max_length=200)
	symbol = models.CharField(max_length=200)
	circulating_supply = models.FloatField(null=True)
	total_supply = models.FloatField(null=True)
	max_supply = models.FloatField(null=True)
	cmc_id = models.IntegerField()
	explorer = models.CharField(null=True,max_length=200)
	based_on_blockchain = models.CharField(null=True,max_length=200)
	website = models.CharField(null=True,max_length=200)
	reddit = models.CharField(null=True,max_length=200)
	twitter = models.CharField(null=True,max_length=200)
	

class Token_price(models.Model):
	Token = models.ForeignKey(Token,on_delete=models.CASCADE)
	cmc_usd_upd_date = models.DateTimeField(null=True)
	cmc_usd_price = models.FloatField(null=True)
	cmc_btc_upd_date = models.DateTimeField(null=True)
	cmc_btc_price = models.FloatField(null=True)
