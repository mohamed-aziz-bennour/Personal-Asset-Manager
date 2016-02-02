from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^create$', views.StockAddView.as_view(), name="create"),
    url(r'^list_stock$', views.StocksListView.as_view(), name="list_stock"),
    url(r'^list_etf$', views.ETFListView.as_view(), name="list_etf"),
    url(r'^list_bond$', views.BondsListView.as_view(), name="list_bond"),
    ]