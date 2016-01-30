from django.shortcuts import render
from .securities_forms import StockForm
from django.views.generic import View

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
            # stock = Stock.objects.create(
            #     user = request.user,
            #     portfolio_name=data.get('portfolio_name')
                # )
            
        
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

    # def post(self, request):
    #   security_name = StockForm(request.POST)
    #   context = {'stock':security_name}
    #   if security_name.is_valid():
    #       security = security_name.save()
    #       return redirect('stock:add_security')
    #   else:
    #       return render(request, self.template_name, context)
