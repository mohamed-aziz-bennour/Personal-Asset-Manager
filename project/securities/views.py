from django.shortcuts import render
from .securities_forms import StockForm
from django.views.generic import View
from securities.securities_models import Stock, Bond, ExchangeTradedFund
from django.http import JsonResponse



class StockAddView(View):
    template_name = 'securities/add_security.html'
    form_class = StockForm
    success_url = "securities:create"
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form)
        return self.render_to_response(request)

    def post(self,request):
        form = self.form_class(data=request.POST)
        data=request.POST
        if form.is_valid(): 
            form.save()
            return redirect(self.success_url)
        else:
            self.context = self.get_context(form)
            return self.render_to_response(request)


        
    def get_context(self, form):
        return {
            "form": form,
            "action": "securities:create",
            "method": "POST",
            "submit_text": "Add new stock"
        }

    def render_to_response(self, request):
        return render(request, self.template_name, self.context)


class StocksListView(View):
    
    def get(self,request):
        stocks = Stock.objects.all()
        stocks = [stock.to_json() for stock in stocks]
        return JsonResponse({'stocks':stocks, 'content_type':'stock'})

class ETFListView(View):
    
    def get(self,request):
        exchangeTradedFunds = ExchangeTradedFund.objects.all()
        exchangeTradedFunds = [exchangeTradedFund.to_json() for exchangeTradedFund in exchangeTradedFunds]
        return JsonResponse({'exchangeTradedFunds':exchangeTradedFunds, 'content_type':'etf'})

class BondsListView(View):
    
    def get(self,request):
        bonds = Bond.objects.all()
        bonds = [bond.to_json() for bond in bonds]
        return JsonResponse({'bonds':bonds, 'content_type':'bond'})