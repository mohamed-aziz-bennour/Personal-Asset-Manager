from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^anlysis$', views.ClientCreateView.as_view(), name="create"),
	]




