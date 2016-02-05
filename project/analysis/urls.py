from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^analysis$', views.ClientCreateView.as_view(), name="analysis"),
	url(r'^risk$', views.RiskView.as_view(), name="risk"),
	url(r'^policy$', views.Investment_policyView.as_view(), name="policy"),
	url(r'^asset_risk$', views.Risk_calculationsView.as_view(), name="asset_risk"),


	]




