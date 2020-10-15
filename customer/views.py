from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q #permite uso de Or (ou)

class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    paginate_by = 4
    model = Customer

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
            ) #icontains ignora letras maiusculas e minusculas
        else:
            object_list = self.model.objects.all()
        return object_list

class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm #Formulário padrão do Django

    def form_valid(self, form):
        return super().form_valid(form)

    #Retorna a URL após preencher com sucesso o forms
    def get_success_url(self):
        return reverse('customer:customer_list')

class CustomerUpdateView(UpdateView):
    template_name = "customer/customer.html" #página html selecionada
    form_class = CustomerForm #Definindo o Models

    def get_object(self):
        pk = self.kwargs.get("pk")
        #método que retorno o err0 404 caso não encontre o id
        return get_object_or_404(Customer, pk=pk)


        #Validar formulário
    def form_valid(self, form):
        return super().form_valid(form)

    #Retorna a URL após preencher com sucesso o forms
    def get_success_url(self):
        return reverse('customer:customer_list')

class CustomerDeleteView(DeleteView):

    def get_object(self):
        pk = self.kwargs.get("pk")
        # método que retorno o err0 404 caso não encontre o id
        return get_object_or_404(Customer, pk=pk)

    # Retorna a URL após preencher com sucesso o forms
    def get_success_url(self):
        return reverse('customer:customer_list')