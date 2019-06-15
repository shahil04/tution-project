from django.db import models
from django.urls import reverse
class Coursesdata(models.Model):
    course_no=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title=models.CharField(max_length=250)
    image=models.FileField(upload_to='image')
    time=models.CharField(max_length=250)
    fee=models.CharField(max_length=250)
    read_more=models.CharField(max_length=500)
    add_date=models.DateField(auto_now=True,null=True)
    overview_titles=models.CharField(max_length=250)
    overview=models.TextField()
  #  overview1=models.TextField()
    syllabus_title=models.CharField(max_length=250)
    syllabus=models.TextField()
    training_methodology_title=models.CharField(max_length=250)
    training_methodology=models.TextField()
    upcoming_batches_title=models.CharField(max_length=250)
    upcoming_batches=models.TextField(blank=True)
    additional_title1=models.CharField(max_length=250,null=True)
    additional_topic1=models.TextField(blank=True)
    additional_title2=models.CharField(max_length=250)
    additional_topic2=models.TextField(blank=True)
    additional_title3=models.CharField(max_length=250)
    additional_topic3=models.TextField(blank=True)
    


    
    class Meta:
        ordering=['-add_date']
        


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('course_detail',args=[str(self.id)])

class Detail_enquiry(models.Model):
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    quary_more=models.TextField(max_length=250)

    def __str__(self):
        return self.name
    

class Detail_course(models.Model):
    title=models.CharField(max_length=250)
    path='home/'
    courseimg=models.FileField()
    coursename=' course overviews '
    syllabus=models.TextField(max_length=10000)
    batch=models.TextField(max_length=400)
    traning=models.TextField(max_length=1000)
    traning_fee=models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('course_detail',args=[str(self.id)])

