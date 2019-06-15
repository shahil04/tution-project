from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .models import Products,Address,Train
from .models import Consultancy,Contact,Website_services,Features_add
from django.urls import reverse_lazy

class Products(ListView):
    model=Products
    template_name='products.html'

class Address(ListView):
    model=Address
    template_name='address.html'
  
class Training(ListView):
    model=Train
    template_name='training.html'
    
class Consultancy(ListView):
    model=Consultancy
    template_name='consultancy.html'

class Contact(CreateView):
    model=Contact
    template_name='contact.html' 
    fields='__all__'
class Website_services(ListView):
    model=Website_services
    template_name='websites.html'