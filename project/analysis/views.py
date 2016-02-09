from django.shortcuts import render, redirect
from django.views.generic import View
from .analysis_models import Client, Risk, Investment_policy
from .analysis_forms import ClientForm, RiskForm, Investment_policyForm 
from securities.securities_models import Bond
from django.http import JsonResponse
from analysis.utilities.risk_calc import Risk
# from analysis.utilities.model_portfolio import ModelPortfolio
from portfolio.models import Portfolio
from django.contrib.contenttypes.models import ContentType

class ClientCreateView(View):
    template_name = 'analysis/index.html'
    model = Client
    form_class = ClientForm
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form)
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            client = form.save(commit = False)
            client.user = request.user
            client.save()
            
            return JsonResponse("saved")
        else:
            print(form.errors)
            context = dict(form=form,submit_text='Create')
            return render(request, self.template_name, context)

    def get_context(self, form):
        return {
            "form": form,
            "action": "analysis:analysis",
            "method": "POST",
            "submit_text": "Create Client"
        }


class RiskView(View):
    template_name = 'analysis/index.html'
    model = Risk
    form_class = RiskForm
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form)
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        data=request.POST
        if form.is_valid():
            risk = form.save(commit = False)
            score = int(data.get('cash_reserves')[0]) + int(data.get('time_horizont')[0])
            score += int(data.get('market_loss')[0]) + int(data.get('investment_experience')[0]) 
            score += int(data.get('investment_return')[0])
            # recommendation = ModelPortfolio(score).get_recommendation()
            risk.user = request.user
            risk.score = score
            risk.save()
            
            return JsonResponse(recommendation)
        else:
            context = dict(form=form,submit_text='Create')
            return render(request, self.template_name, context)

    def get_context(self, form):
        return {
            "form": form,
            "action": "analysis:risk",
            "method": "POST",
            "submit_text": "Submit Risk Form"
        }

class Investment_policyView(View):
    template_name = 'analysis/index.html'
    model = Investment_policy
    form_class = Investment_policyForm
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form)
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            investment_policy = form.save(commit = False)
            investment_policy.user = request.user 
            investment_policy.save()
            return render(request, "users/welcome.html")
        # What do you want to do with this
        print(form.errors)
        return JsonResponse({'result': 'failed'})

    def get_context(self, form):
        return {
            "form": form,
            "action": "analysis:policy",
            "method": "POST",
            "submit_text": "Submit Policy Form"
        }


class BetaAnalysisView(View):
    model = Portfolio
    template_name = 'portfolio/read.html'

    def get(self,request,id):
        portfolio_object = Portfolio.objects.get(id=id)
        bond = ContentType.objects.get_for_model(Bond)
        assets = portfolio_object.asset_set.exclude(content_type=bond)
        risk = Risk()

        context = {}

        for asset in assets:
           symbol = asset.content_object.symbol
           stock = risk.run_analysis(symbol)
           context[symbol] = stock
           
        return JsonResponse({'response':context})




# class Risk_calculationsView(View):
#     template_name = 'analysis/risk_analysis.html'




# class Profit_loss(View):
#     template_name = 'analysis/p_l.html'
#     model = Portfolio
#     context = None

#     def post(self, request):
#         form = self.form_class(data=request.POST)
#         data=request.POST
#         result = data
#         return JsonResponse({'result': result})

#        


















