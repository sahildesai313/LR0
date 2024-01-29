from django.db import models

# Create your models here.



class person(models.Model):

    username=models.CharField(unique=True,max_length=100)
    fullname=models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100,default="")
    confirmpassword=models.CharField(max_length=100,default="")

    
    def _str_(self):
        return f"{self.username}{self.fullname}{self.phone}{self.email}{self.password}{self.confirmpassword}"