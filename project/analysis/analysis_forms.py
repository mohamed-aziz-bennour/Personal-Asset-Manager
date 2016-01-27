from django import forms
from analysis.analysis_models import Client, Risk, Investment_policy
from analysis.analysis_choices import *


class ClientForm(forms.Form):
	age = forms.ChoiceField(choices=AGE, label="", initial='', widget=forms.Select(), required=True)
	marital_status = forms.ChoiceField(choices=MARITAL_STATUS, label="", initial='', widget=forms.Select(), required=True)
	income = forms.ChoiceField(choices=INCOME, label="", initial='', widget=forms.Select(), required=True)
	saving_rate = forms.ChoiceField(choices=SAVING_RATE, label="", initial='', widget=forms.Select(), required=True)
	fixed_expenses = forms.ChoiceField(choices=FIXED_EXPENSES, label="", initial='', widget=forms.Select(), required=True)
	federal_tax = forms.ChoiceField(choices=FEDERAL_TAX, label="", initial='', widget=forms.Select(), required=True)
	state_tax = forms.ChoiceField(choices=STATE_TAX, label="", initial='', widget=forms.Select(), required=True)
	# user_id = forms.(widget='HiddenInput')

class RiskForm(forms.Form):
	cash_reserves = forms.ChoiceField(choices=CASH_RESERVES, label="", initial='', widget=forms.Select(), required=True)
	time_horizont = forms.ChoiceField(choices=TIME_HORIZONT, label="", initial='', widget=forms.Select(), required=True)
	market_loss = forms.ChoiceField(choices=MARKET_LOSS, label="", initial='', widget=forms.Select(), required=True)
	investment_experience = forms.ChoiceField(choices=INVESTMENT_EXPERIENCE, label="", initial='', widget=forms.Select(), required=True)
	investment_return = forms.ChoiceField(choices=INVESTMENT_RETURN, label="", initial='', widget=forms.Select(), required=True)
	# user_id = models.(widget='HiddenInput')

class Investment_policyForm(forms.Form):
	time_retirement = forms.ChoiceField(choices=TIME_RETIREMENT, label="", initial='', widget=forms.Select(), required=True)
	liquidity_needs = forms.ChoiceField(choices=LIQIDITY_NEEDS, label="", initial='', widget=forms.Select(), required=True)
	goal_short = forms.ChoiceField(choices=GOAL_SHORT, label="", initial='', widget=forms.Select(), required=True)
	goal_mid = forms.ChoiceField(choices=GOAL_MID, label="", initial='', widget=forms.Select(), required=True)
	goal_long = forms.ChoiceField(choices=GOAL_LONG, label="", initial='', widget=forms.Select(), required=True)
	expected_return = forms.DecimalField()
	expected_inflation = forms.DecimalField()
	# user_id = models(widget='HiddenInput')

