from django.urls import path
from .views import home, detail, register_customer, register_client, product_list

app_name = 'core'

urlpatterns = [
    path('', home, name="home"),
    path('product/list', product_list, name="product_list"),
    path('register/client', register_client, name="register_client"),
    path('register/product', register_customer, name="register_product"),
    path('detail/<int:pk>/', detail, name='detail'),
]
