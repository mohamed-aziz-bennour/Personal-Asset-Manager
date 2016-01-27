from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, PasswordChangeForm
)
# from .forms import UserUpdateForm
from .forms import ProfileForm
from users.models import Profile
# from . import helper as help_ 
# Create your views here.
# Rolling Your Own User Views

# These Views Only Render A Template
# class index
class Index(View):

    def get(self,request):
        if "next" in request.GET:
            request.session["next"] = request.GET["next"]
        return render(request, "users/index.html")

    def post(self, request):
        return HttpResponseNotAllowed(['GET'])




class Welcome(LoginRequiredMixin, View):

    def get(self,request):
        return render(request, "users/welcome.html")
    def post(self,request):
        return HttpResponseNotAllowed(['GET'])


# class logout 
class UserLogout(LoginRequiredMixin, View):

    def get(self,request):
        logout(request)
        request.session['dict_profile'] = None
        return redirect(settings.LOGIN_URL)
        
    def post(self,request):
        return HttpResponseNotAllowed(['GET'])



# The Following Views All Have An Associated Form
class CreateUser(View):
    template_name = "users/user_form.html"
    form_class = ProfileForm
    success_url = "users:login"
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form)
        print(self.context)
        return self.render_to_response(request)

    def post(self, request):
        form = self.form_class(data=request.POST)
        data=request.POST
        if form.is_valid(): 
            user = User.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('username'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                )
            profile = Profile.objects.create(user=user,
                phone_number=data.get('phone_number')
                )
        
            return redirect(self.success_url)
        else:
            self.context = self.get_context(form)
            return self.render_to_response(request)

    def get_context(self, form):
        return {
            "form": form,
            "action": "users:create",
            "method": "POST",
            "submit_text": "Register"
        }

    def render_to_response(self, request):
        return render(request, self.template_name, self.context)

class LoginUser(View):
    template_name = "users/user_form.html"
    form_class = AuthenticationForm
    success_url = "users:welcome"
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form)
        return self.render_to_response(request)

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        data=request.POST
        if True:
        # if form.is_valid():
            print ("11111111111111111111")
            # user = form.get_user()
            print(data.get('username'),data.get('password'))
            user = User.objects.filter(username=data.get('username'))
            
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user and user.is_authenticated() and user.is_active:
                login(request, user)
            else:
                self.context = self.get_context(form)
                return self.render_to_response(request)
            print('33333333333333333333')
            profile = Profile.objects.filter(user=user)
            if "next" in request.session:
                self.success_url = request.session["next"]
                del request.session["next"]
            request.session.set_expiry(300)
            # dict_profile = {'username': data.get('username'),
            #     'first_name':data.get('first_name'),
            #     'last_name' : data.get('last_name'),
            #     'email' : data.get('email'),
            #     'phone_number' : data.get('phone_number')
            #     }
            # request.session['dict_profile'] = dict_profile
            return redirect(self.success_url)
        else:
            self.context = self.get_context(form)
            return self.render_to_response(request)

    def get_context(self, form):
        return {
            "form": form,
            "action": "users:login",
            "method": "POST",
            "submit_text": "Login" 
        }

    def render_to_response(self, request):
        return render(request, self.template_name, self.context)

# class UpdateUser(LoginRequiredMixin, View):
#     template_name = "users/user_form.html"
#     form_class = UserUpdateForm
#     success_url = "users:welcome"
#     context = None

#     def get(self, request):
#         form = self.form_class(instance=request.user)
#         self.context = self.get_context(form)
#         return self.render_to_response(request)

#     def post(self, request):
#         form = self.form_class(
#             data=request.POST, instance=request.user
#         )
#         if form.is_valid():
#             form.save()
#             return redirect(self.success_url)
#         else:
#             self.context = self.get_context(form)
#             return self.render_to_response(request)

#     def get_context(self, form):
#         return {
#             "form": form,
#             "action": "users:update",
#             "method": "POST",
#             "submit_text": "Update" 
#         }
        
#     def render_to_response(self, request):
#         return render(request, self.template_name, self.context)

# class ChangePassword(LoginRequiredMixin, View):
#     template_name = "users/user_form.html"
#     form_class = PasswordChangeForm
#     success_url = "users:welcome"
#     context = None

#     def get(self, request):
#         form = self.form_class()
#         self.context = self.get_context(form)
#         return self.render_to_response(request)

#     def post(self, request):
#         form = self.form_class(
#             user=request.users, data=request.POST
#         )
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect(self.success_url)
#         else:
#             self.context = self.get_context(form)
#             return self.render_to_response(request)

#     def get_context(self, form):
#         return {
#             "form": form,
#             "action": "users:update",
#             "method": "POST",
#             "submit_text": "Update" 
#         }
        
#     def render_to_response(self, request):
#         return render(request, self.template_name, self.context)
