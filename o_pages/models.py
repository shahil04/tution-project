from django.urls import reverse,reverse_lazy

from django.db import models

class Products(models.Model):
    title_topic=models.CharField(max_length=200)
    about=models.TextField(max_length=20000)

class Address(models.Model):
    address=models.TextField(max_length=200)

    def __str__(self):
        return self.address

class Consultancy(models.Model):
    title_topic=models.CharField(max_length=200)
    about=models.TextField(max_length=20000)

class Website_services(models.Model):
    title_topic=models.CharField(max_length=200)
    about=models.TextField(max_length=20000)

class Features_add(models.Model):
    title_topic=models.CharField(max_length=200)
    about=models.TextField(max_length=20000)

class Question(models.Model):
    question=models.CharField(max_length=200)
    date=models.DateTimeField('enquiry_date')

class Contact(models.Model):
    name=models.CharField(max_length=200)
    phone_no=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField(max_length=2000)

    def get_absolute_url(self):
        return reverse('home')

class Train(models.Model):
    title_topic=models.CharField(max_length=200)
    about=models.TextField(max_length=20000)
