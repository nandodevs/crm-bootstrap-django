from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView

app_name = "customer"

urlpatterns = [
    path("list/", CustomerListView.as_view(), name="customer_list"),
    path("", CustomerCreateView.as_view(), name="customer_create"),
    path("<int:pk>/", CustomerUpdateView.as_view(), name="customer-update"), #Pk=Chave Primária
    path("<int:pk>/delete", CustomerDeleteView.as_view(), name="customer-delete")
]