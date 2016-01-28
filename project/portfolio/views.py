from django.shortcuts import render, redirect
from portfolio.models import Portfolio, Asset
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from portfolio.forms import PortfolioForm


# Create your views here.

class CreatePortfolio(LoginRequiredMixin,View):
    template_name = "portfolio/portfolio_form.html"
    form_class = PortfolioForm
    success_url = "portfolio:create"
    context = None

    def get(self,request):
        form = self.form_class()
        self.context = self.get_context(form)
        return self.render_to_response(request)

    def post(self,request):
        form = self.form_class(data=request.POST)
        data=request.POST
        if form.is_valid(): 
            portfolio = Portfolio.objects.create(
                user = request.user,
                portfolio_name=data.get('portfolio_name')
                )
            
        
            return redirect(self.success_url)
        else:
            self.context = self.get_context(form)
            return self.render_to_response(request)


        
    def get_context(self, form):
        return {
            "form": form,
            "action": "portfolio:create",
            "method": "POST",
            "submit_text": "Add new Portfolio"
        }

    def render_to_response(self, request):
        return render(request, self.template_name, self.context)

class ShowPortfolio(LoginRequiredMixin,View):
    
    def get(self,request):
        portfolio_objects = Portfolio.objects.filter(user=request.user)
        # portfolios = [portfolio.to_json() for portfolio in portfolio_objects]
        portfolios = [portfolio for portfolio in portfolio_objects]
        # if portfolios.exists():
        return render(request, 'portfolio/list_portfolio.html',
         {'portfolios':portfolios}
         )

    def post(self,request):
        return HttpResponseNotAllowed(['GET'])


class DeletePortfolio(LoginRequiredMixin,View):
    success_url="portfolio:show_list"
    
    def get(self,request,id):
        print(id)
        portfolio_objects = Portfolio.objects.get(id=id,
            user=request.user).delete()
        return redirect(self.success_url)
       

    def post(self,request):
        return HttpResponseNotAllowed(['GET'])



