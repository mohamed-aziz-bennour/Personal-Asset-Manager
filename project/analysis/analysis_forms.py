from django import forms
from analysis.analysis_models import Client, Risk, Investment_policy
from analysis.analysis_choices import *


class ClientForm(forms.ModelForm):
    age = forms.ChoiceField(choices=AGE, label="", initial='', widget=forms.Select(), required=True)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS, label="", initial='', widget=forms.Select(), required=True)
    income = forms.ChoiceField(choices=INCOME, label="", initial='', widget=forms.Select(), required=True)
    saving_rate = forms.ChoiceField(choices=SAVING_RATE, label="", initial='', widget=forms.Select(), required=True)
    fixed_expenses = forms.ChoiceField(choices=FIXED_EXPENSES, label="", initial='', widget=forms.Select(), required=True)
    federal_tax = forms.ChoiceField(choices=FEDERAL_TAX, label="", initial='', widget=forms.Select(), required=True)
    state_tax = forms.ChoiceField(choices=STATE_TAX, label="", initial='', widget=forms.Select(), required=True)
    # user_id = forms.(widget='HiddenInput')
    class Meta:
        model = Client
        fields = [
            "age",
            "marital_status",
            "income",
            "saving_rate",
            "fixed_expenses",
            "federal_tax",
            "state_tax"
            ]

class RiskForm(forms.ModelForm):
    cash_reserves = forms.ChoiceField(choices=CASH_RESERVES, initial='', widget=forms.RadioSelect(), required=True)
    time_horizont = forms.ChoiceField(choices=TIME_HORIZONT, initial='', widget=forms.RadioSelect(), required=True)
    market_loss = forms.ChoiceField(choices=MARKET_LOSS, initial='', widget=forms.RadioSelect(), required=True)
    investment_experience = forms.ChoiceField(choices=INVESTMENT_EXPERIENCE, initial='', widget=forms.RadioSelect(), required=True)
    investment_return = forms.ChoiceField(choices=INVESTMENT_RETURN, initial='', widget=forms.RadioSelect(), required=True)
    # user_id = models.(widget='HiddenInput')
    class Meta:
        model = Risk
        fields = [
            'cash_reserves',
            'time_horizont',
            'market_loss',
            'investment_experience',
            'investment_return',
            ]

class Investment_policyForm(forms.ModelForm):
    time_retirement = forms.ChoiceField(choices=TIME_RETIREMENT, initial='', widget=forms.RadioSelect(), required=True)
    liquidity_needs = forms.ChoiceField(choices=LIQIDITY_NEEDS, initial='', widget=forms.RadioSelect(), required=True)
    goal_short = forms.ChoiceField(choices=GOAL_SHORT, initial='', widget=forms.RadioSelect(), required=True)
    goal_mid = forms.ChoiceField(choices=GOAL_MID, initial='', widget=forms.RadioSelect(), required=True)
    goal_long = forms.ChoiceField(choices=GOAL_LONG, initial='', widget=forms.RadioSelect(), required=True)
    expected_return = forms.DecimalField()
    expected_inflation = forms.DecimalField()
    # user_id = models(widget='HiddenInput')
    class Meta:
        model = Investment_policy
        fields = [
            'time_retirement',
            'liquidity_needs',
            'goal_short',
            'goal_mid',
            'goal_long',
            'expected_return',
            'expected_inflation',
            ]

