from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.




Category = (
        ( "Dental","Dental"     ),
        ( "Neuro"  ,"Neuro"   ),
        ( "Child" ,"Child"   ),
        ( "Bone" , "Bone"  ),
        ( "General","General"  ),
        ( "Heart" ,"Heart"  ),
        ( "Eyes" , "Eyes" ),
        ( "Gyno" , "Gyno"  ),
    )

class Doctor(models.Model):

    firstName = models.CharField(max_length=100 , null=True , blank=True)
    lastName = models.CharField(max_length=100 , null=True , blank=True)
    
    age = models.IntegerField(default=18 , null=True )
    token = models.IntegerField(default=0 , null=True)
    category = models.CharField(max_length=100 , choices=Category , null=True)
    slug = AutoSlugField(populate_from='firstName')
    likes = models.IntegerField(default=0 , null=True)


    def __str__(self):
        return self.firstName
