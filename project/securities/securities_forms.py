from django import forms
from securities.securities_models import Stock, Bond, Etf

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['symbol', 'company_name', 'sector', 'industry', 'market_capitalization']

class BondForm(forms.ModelForm):
	class Meta:
		model = Bond
		fields = ['symbol', 'company_name', 'coupon', 'maturity_date', 'bond_type']


class Etf(models.ModelForm):
	class Meta:
		model = Etf
		fields = ['symbol', 'name', 'category', 'fund_family', 'bata', 'alpha', 'r_squared', 'sharpe_ratio']

