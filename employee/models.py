from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(AbstractUser):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_description = models.TextField()
    
    def __str__(self):
        return str(self.product_name)
    

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    customer_phone = models.CharField(max_length=15,unique=True)
    customer_address = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return str(self.customer_name)
    

class BillCustomer(models.Model):
    bill_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Employee, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.bill_id)