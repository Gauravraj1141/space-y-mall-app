from rest_framework import serializers
from .models import Employee,Product, Customer,BillCustomer
from django.contrib.auth.hashers import make_password


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'username','first_name','last_name', 'email', 'department', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_price', 'product_quantity', 'product_description']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'customer_name', 'customer_email', 'customer_phone', 'customer_address']
        
        
class BillCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillCustomer
        fields = ['bill_id', 'customer', 'product', 'seller', 'quantity', 'date']
        read_only_fields = ['total_price']  # Making total_price read-only