from django.db import models
from email.policy import default
from enum import unique
from random import choices
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name

###################################   my app  ##########################
class UserData(models.Model):
    CID = models.IntegerField(unique=True, null=False)
	# CID = models.OneToOneField(User, on_delete=models.CASCADE)
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    gen = [
        ('Male', 'Male'),
        ('Female', 'Female')
        ]
    gender = models.CharField(max_length=100, choices = gen)
    DOB = models.DateField()
    profile = models.ImageField(upload_to='image', null= True, blank=True)
    Village = models.CharField(max_length=100)
    Chiwog = models.CharField(max_length=100)
    ThramNo = models.CharField(max_length=100)
    HouseHoldNo = models.CharField(max_length=100)  
    Created = models.DateTimeField(auto_now_add=True)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return str(self.CID)



class Marriage(models.Model):
	MarriageId = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
	# Spousecid = models.IntegerField()
	your_cid = models.IntegerField()
	Spousecid = models.OneToOneField(UserData, on_delete=models.CASCADE, related_name="spouce")
	# Spousename = models.CharField(max_length=100)
	MarriageCertificate  = models.FileField(upload_to='file', null=True)
	status = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.MarriageId)


class Passdata(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	reason = models.CharField(max_length=100)
	request_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=100, default="pending")

	def __str__(self):
		return str(self.user)

class childdata(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	childname= models.CharField(max_length=100)
	DOB = models.DateField()
	request_date = models.DateTimeField(auto_now_add=True)
	parentsid = models.IntegerField()

	def __str__(self):
		return str(self.user)









