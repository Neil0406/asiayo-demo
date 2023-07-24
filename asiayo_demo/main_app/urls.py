from main_app import views
from django.urls import path

urlpatterns = [
    path("convert_currency", views.ConvertCurrency.as_view(), name="convert_currency")
]
