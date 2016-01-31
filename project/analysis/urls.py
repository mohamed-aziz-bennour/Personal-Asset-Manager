from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^analysis$', views.ClientCreateView.as_view(), name="analysis"),
	url(r'^risk$', views.RiskView.as_view(), name="risk"),

	]




