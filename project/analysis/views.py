from django.shortcuts import render, redirect
from django.views.generic import View
from .analysis_models import Client, Risk, Investment_policy
from users.models import Profile
from .analysis_forms import ClientForm, RiskForm, Investment_policyForm 
from securities.securities_models import Bond
from django.http import JsonResponse
from analysis.utilities.risk_calc import RiskAnalysis
# from analysis.utilities.model_portfolio import ModelPortfolio
from portfolio.models import Portfolio
from django.contrib.contenttypes.models import ContentType
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

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
            return redirect('/analysis/policy')
            # return JsonResponse("saved")
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
        risk = RiskAnalysis()
        # print(risk)

        context = {}

        for asset in assets:
           symbol = asset.content_object.symbol
           print(symbol)
           stock = risk.run_analysis(symbol)
           context[symbol] = stock
           
        return JsonResponse({'response':context})


class ReportInvestmentPolicy(View):
    def get(self,request):
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

        buffer = BytesIO()

        # Create the PDF object, using the BytesIO object as its "file."
        p = canvas.Canvas(buffer)
        user = request.user
        client = Client.objects.get(user=user)
        investment = Investment_policy.objects.get(user=user)
        profile = Profile.objects.get(user=user)
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(500,20,"PAM®")
        p.setTitle("Investment Policy")
        p.setFont("Helvetica-Bold", 24)
        p.drawCentredString(250, 800, "Investment Policy")


        

        p.setFont("Times-Roman", 12)
        gap = 20
        y = 780
        x = 400

        p.drawString(x,y,'Client Name: '+user.first_name +' '+user.last_name)
        p.drawString(x,y- gap * 1,'Email address: '+user.email)
        p.drawString(x,y- gap * 2,'Phone Number: '+profile.phone_number)
        
        
        gap = 30

        y = 700
        x = 300
        p.drawString(x,y,client.age)
        p.drawString(x,y- gap * 1,client.marital_status)
        p.drawString(x,y- gap * 2,client.income)
        p.drawString(x,y- gap * 3,client.saving_rate)
        p.drawString(x,y- gap * 4,client.fixed_expenses)
        p.drawString(x,y- gap * 5,str(client.federal_tax))
        p.drawString(x,y- gap * 6,str(client.state_tax))
        x = 100
        p.drawString(x,y,"Age Range:")
        p.drawString(x,y- gap * 1,"Marital Status:")
        p.drawString(x,y- gap * 2,"Income Range:")
        p.drawString(x,y- gap * 3,"Saving Rate:")
        p.drawString(x,y- gap * 4,"Fixed Expenses:")
        p.drawString(x,y- gap * 5,"Federal Taxes:")
        p.drawString(x,y- gap * 6,"Staets Taxes:")

        y = 450
        x = 300
        p.drawString(x,y,investment.time_retirement)
        p.drawString(x,y- gap * 1,investment.liquidity_needs)
        p.drawString(x,y- gap * 2,investment.goal_short)
        p.drawString(x,y- gap * 3,investment.goal_mid)
        p.drawString(x,y- gap * 4,investment.goal_long)
        p.drawString(x,y- gap * 5,str(investment.expected_return))
        p.drawString(x,y- gap * 6,str(investment.expected_inflation))
        x = 100
        p.drawString(x,y,"Time before retirement:")
        p.drawString(x,y- gap * 1,"Need to liquidity:")
        p.drawString(x,y- gap * 2,"Short Goal:")
        p.drawString(x,y- gap * 3,"Mid Goal:")
        p.drawString(x,y- gap * 4,"Long Goal:")
        p.drawString(x,y- gap * 5,"Expected Return:")
        p.drawString(x,y- gap * 6,"Expected Inflation:")




        # Close the PDF object cleanly.
        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response



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


















