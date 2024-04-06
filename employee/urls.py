from django.urls import path,include
from .views import *

urlpatterns = [
    # path('create_employee/', EmployeeCreateView.as_view() , name='add-employee'), 

    path('add_product/', AddProduct.as_view() , name='add-product'), 
    path('update_product/<int:pk>/', UpdateProduct.as_view() , name='update-product'), 
    path('delete_product/<int:pk>/', DeleteProduct.as_view(), name='delete-product'),
    path('product_list/', FetchAllProduct.as_view(), name='list-product'), 

    path('add_customer/', AddCustomer.as_view(), name='add-customer'), 
    path('fetch_all_customer/', FetchCustomers.as_view(), name='fetch-all-customer'), 
    path('update_customer/', UpdateCustomer.as_view(), name='update-customer'), 
    path('delete_customer/', DeleteCustomer.as_view(), name='delete-customer'), 

    path('create_customer_bill/', CreateBillCustomer.as_view(), name='create-customer-bill'), 
    path('employee_analytics/', EmployeeAnalytics.as_view(), name='employee-analytics'), 

]   