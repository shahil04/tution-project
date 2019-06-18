from django.urls import path
from . import views

urlpatterns=[
    path('',views.Homepage.as_view(),name='home'),
    path('enquiry/',views.Enquiry.as_view(),name='enquiry'),
    path('courses/<int:pk>',views.Details_view.as_view(),name='course_detail'),
    path('course/update/<int:pk>',views.Update_course.as_view(),name='course_update'),
    path('course/create/',views.Create_course.as_view(),name='create_course'),
    path('delete/<int:pk>',views.Delete_course.as_view(),name='delete_course'),
    path('enquiry_create/',views.Euquiry_create.as_view(),name='enquiry_create'),
    ]