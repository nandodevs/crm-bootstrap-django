from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer) #Registra a aplicação
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email"]