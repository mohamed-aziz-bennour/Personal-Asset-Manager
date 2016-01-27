from django.db import models



class Stock(models.Model):
	symbol = models.CharField(max_length = 15)
	company_name = models.CharField(max_length = 255)
	sector = models.CharField(max_length = 30)
	industry = models.CharField(max_length = 30)
	market_capitalization = models.IntegerField(max_digits = 10)


class Bond(models.Model):
	symbol = models.CharField(max_length = 15)
	company_name = models.CharField(max_length = 255)
	coupon = models.DecimalField(max_digits = 2, decimal_places = 2)
	maturity_date = DateTimeField(auto_now_add = False)
	bond_type = models.CharField(max_length = 15)


class Etf(models.Model):
	symbol = models.CharField(max_length = 15)
	name = mdels.CharField(max_length = 255)
	category = models.CharField(max_length = 30)
	fund_family = model.CharField(max_length = 30)
	beta = models.DecimalField(max_digits = 2, decimal_places = 2)
	alpha = models.DecimalField(max_digits = 2, decimal_places = 2)
	r_squared = models.DecimalField(max_digits = 3, decimal_places = 2)
	sharpe_ratio = models.DecimalField(max_digits = 2, decimal_places = 2)

