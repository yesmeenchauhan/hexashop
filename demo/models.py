from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class hexa(models.Model):
 image=models.ImageField(upload_to="images/")
 name=models.CharField(max_length=40)
 price=models.CharField(max_length=10)
 discription=models.CharField(max_length=500)
 categories=models.CharField(max_length=390)

class pay(models.Model):
  # cart_details = models.OneToOneField(on_delete=models.CASCADE)
  firstname=models.CharField(max_length=20)
  lastname=models.CharField(max_length=10)
  email=models.EmailField(unique=True)
  streetaddress=models.CharField(max_length=200)
  streetaddressline2=models.CharField(max_length=200)
  city=models.CharField(max_length=20)
  state=models.CharField(max_length=10)
  zipcode=models.CharField(max_length=10)

class userlog(models.Model):
  userdata = models.ForeignKey(User,on_delete=models.CASCADE)
  user_pay = models.ForeignKey(hexa,on_delete=models.CASCADE)
  quantity=models.IntegerField()
class contact(models.Model):
  name=models.CharField(max_length=20)
  email=models.EmailField(unique=True) 
  message=models.CharField(max_length=300)
class subscribe(models.Model):
  name=models.CharField(max_length=20)
  email=models.EmailField(unique=True)