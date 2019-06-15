from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DetailView
from django.views.generic.edit import DeleteView,CreateView
from .models import Coursesdata,Detail_enquiry,Detail_course
from django.urls import reverse_lazy

# Create your views here.
class Homepage(ListView):
    model=Coursesdata
    template_name='home.html'
    

class Enquiry(ListView):
    model=Detail_enquiry
    template_name='enquiry.html'

class Euquiry_create(CreateView):
    model=Detail_enquiry
    template_name="create_enquiry.html"
    fields='__all__'
    success_url=reverse_lazy('home')

class Details_view(DetailView):
    model=Coursesdata
    template_name='courses_details.html'

class Create_course(CreateView):
    model=Coursesdata
    template_name='create_course.html'
    fields='__all__'

class Update_course(UpdateView):
    model=Coursesdata
    template_name='update_course.html'
    fields='__all__'

class Delete_course(DeleteView):
    model=Coursesdata
    template_name='delete_course.html'
    success_url=reverse_lazy('home')

