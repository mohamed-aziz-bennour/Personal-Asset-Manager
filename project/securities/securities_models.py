from django.db import models
from portfolio.models import Asset
from django.contrib.contenttypes.fields import GenericRelation



class Stock(models.Model):
    symbol = models.CharField(max_length = 15)
    company_name = models.CharField(max_length = 255)
    sector = models.CharField(max_length = 30)
    industry = models.CharField(max_length = 30)
    market_capitalization = models.DecimalField(max_digits = 10, 
        decimal_places = 2
        )
    def to_json(self):
        return dict(
            id = self.id,
            symbol = self.symbol,
            company_name = self.company_name,
            sector = self.sector,
            industry = self.industry,
            market_capitalization = self.market_capitalization

        )
    # assets = GenericRelation(Asset)


class Bond(models.Model):
    symbol = models.CharField(max_length = 15)
    company_name = models.CharField(max_length = 255)
    coupon = models.DecimalField(max_digits = 2, decimal_places = 2)
    maturity_date = models.DateTimeField(auto_now_add = False)
    bond_type = models.CharField(max_length = 15)
    # assets = GenericRelation(Asset)

    # add a to_json here when art will push his code with the new bon model 


class ExchangeTradedFund(models.Model):
    symbol = models.CharField(max_length = 15)
    name = models.CharField(max_length = 255)
    category = models.CharField(max_length = 30)
    fund_family = models.CharField(max_length = 30)
    beta = models.FloatField(null=True,blank=True)
    alpha = models.FloatField(null=True,blank=True)
    r_squared = models.FloatField(null=True,blank=True)
    sharpe_ratio = models.FloatField(null=True,blank=True)
    # assets = GenericRelation(Asset)
    def to_json(self):
        return dict(
            id = self.id,
            symbol = self.symbol,
            name = self.name,
            category = self.category,
            fund_family= self.fund_family,
            beta = self.beta,
            alpha = self.alpha,
            r_squared = self.r_squared,
            sharpe_ratio = self.sharpe_ratio
        )

