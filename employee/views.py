from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .serializers import EmployeeSerializer,ProductSerializer, CustomerSerializer,BillCustomerSerializer
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

# employee management 
class EmployeeCreateView(GenericAPIView, CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# product management 
class AddProduct(GenericAPIView, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FetchAllProduct(GenericAPIView, ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UpdateProduct(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class DeleteProduct(GenericAPIView, DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#  customer management
class AddCustomer(GenericAPIView, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FetchCustomers(GenericAPIView, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class UpdateCustomer(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    
class DeleteCustomer(GenericAPIView, DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class CreateBillCustomer(GenericAPIView, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = BillCustomer.objects.all()
    serializer_class = BillCustomerSerializer

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        quantity = request.data.get('quantity')
        product = Product.objects.get(product_id=product_id)
        product_price = product.product_price
        total_price = product_price * quantity
        
        request.data['total_price'] = total_price
        print(request.data,'>>> data')
        return self.create(request, *args, **kwargs)
    

class CreateBillCustomer(GenericAPIView, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = BillCustomer.objects.all()
    serializer_class = BillCustomerSerializer

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        quantity = request.data.get('quantity')
        product = Product.objects.get(product_id=product_id)
        product_price = product.product_price
        total_price = product_price * quantity

        # Create a new dictionary without 'total_price'
        modified_data = request.data.copy()
        modified_data.pop('total_price', None)

        # Assign calculated total_price to the serializer instance
        serializer = self.get_serializer(data=modified_data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['total_price'] = total_price

        # Save the instance
        self.perform_create(serializer)

        instance_data = serializer.data

        # Add total_price to the response data
        instance_data['total_price'] = total_price
        
        return Response(instance_data, status=HTTP_201_CREATED)


class EmployeeAnalytics(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        output_payload = []
        # Get all the employees
        employees = Employee.objects.all()

        for employee in employees:
            emp_id = employee.id
            sales = BillCustomer.objects.filter(seller=emp_id)
            sales_by_employee = sales.count()
            total_revenue = 0
            sold_products_count = 0
            for sale in sales:
                total_revenue += sale.total_price
                sold_products_count += sale.quantity
                

            output_payload.append({
                'employee_name': employee.first_name + ' ' + employee.last_name,
                'employee_email': employee.email,
                'total_sales': sales_by_employee,
                'total_revenue': total_revenue,
                'sold_products_count': sold_products_count
            })
     

        return Response({"ouput_payload":output_payload})