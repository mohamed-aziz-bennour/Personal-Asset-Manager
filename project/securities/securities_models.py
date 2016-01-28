from django.db import models
from portfolio.models import Asset



class Stock(models.Model):
	symbol = models.CharField(max_length = 15)
	company_name = models.CharField(max_length = 255)
	sector = models.CharField(max_length = 30)
	industry = models.CharField(max_length = 30)
	market_capitalization = models.DecimalField(max_digits = 10, 
		decimal_places = 2
		)
	assets = GenericRelation(Asset)


class Bond(models.Model):
	symbol = models.CharField(max_length = 15)
	company_name = models.CharField(max_length = 255)
	coupon = models.DecimalField(max_digits = 2, decimal_places = 2)
	maturity_date = models.DateTimeField(auto_now_add = False)
	bond_type = models.CharField(max_length = 15)
	assets = GenericRelation(Asset)


class ExchangeTradedFund(models.Model):
	symbol = models.CharField(max_length = 15)
	name = models.CharField(max_length = 255)
	category = models.CharField(max_length = 30)
	fund_family = models.CharField(max_length = 30)
	beta = models.DecimalField(max_digits = 2, decimal_places = 2)
	alpha = models.DecimalField(max_digits = 2, decimal_places = 2)
	r_squared = models.DecimalField(max_digits = 3, decimal_places = 2)
	sharpe_ratio = models.DecimalField(max_digits = 2, decimal_places = 2)
	assets = GenericRelation(Asset)

