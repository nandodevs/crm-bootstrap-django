from django.views.generic import ListView, CreateView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse

class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    model = Customer
    queryset = Customer.objects.all()

class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm #Formulário padrão do Django

    def form_valid(self, form):
        return super().form_valid(form)
    
    #Retorna a URL após preencher com sucesso o forms
    def get_success_url(self):
        return reverse('customer:customer_list')