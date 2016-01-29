from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^create$', views.StockAddView.as_view(), name="create"),
    ]