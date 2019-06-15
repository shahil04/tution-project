from django.urls import path
from . import views

urlpatterns=[
    path('address/',views.Address.as_view(),name='address'),
    path('training/',views.Training.as_view(),name='training'),
    path('consultancy/',views.Consultancy.as_view(),name='consultancy'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('websites_services/',views.Website_services.as_view(),name='websites'),
    path('products/',views.Products.as_view(),name='products'),

]