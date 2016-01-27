from django.shortcuts import render, redirect
from django.views.generic import View
from .analysis_models import Client, Risk, Investment_policy
from .analysis_forms import ClientForm, RiskForm, Investment_policyForm 

class ClientCreateView(View):
	template_name = 'analysis/index.html'
	model = Client
	form_class = ClientForm
	context = None

	def get(self, request):
		print('I am in the get')
		form = self.form_class()
		print(form)
		# context = dict(form=self.form_class(),submit_text='Create')
		self.context = self.get_context(form)
		print(self.context)
		return render(request, self.template_name, self.context)

	def post(self, request):
		form = self.form_class(data=request.POST)
		if form.is_valid():
			client = form.save()
			return redirect('analysis:index')
		else:
			context = dict(form=form,submit_text='Create')
			return render(request, self.template_name, context)

	def get_context(self, form):
		return {
			"form": form,
			"action": "analysis:analysis",
			"method": "POST",
			"submit_text": "Create Client"
		}