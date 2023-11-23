from django.urls import path
from .views import home, detail, register_customer

app_name = 'core'

urlpatterns = [
    path('', home, name="home"),
    path('register/product', register_customer, name="register"),
    path('detail/<int:pk>/', detail, name='detail'),
]
