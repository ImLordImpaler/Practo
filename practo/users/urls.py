
from django.urls import path
from . import  views
urlpatterns = [
    path('' , views.doctor, name = 'doctors'),
    path('addDoctor' , views.addDoctor , name ='addDoctor'),
    path('newAppoint' , views.newAppoint , name = 'book')
]
