from django.shortcuts import render, redirect
from django.views.generic import View
from .analysis_models import Client, Risk, Investment_policy
from .analysis_forms import ClientForm, RiskForm, Investment_policyForm 

class ClientCreateView(View):
    template_name = 'analysis/index.html'
    model = Client
    form_class = ClientForm

    def get(self, request):
        context = dict(form=self.form_class(),submit_text='Create')
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('analysis:index')
        else:
            context = dict(form=form,submit_text='Create')
            return render(request, self.template_name, context)