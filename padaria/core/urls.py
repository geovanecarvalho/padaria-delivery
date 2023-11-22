from django.urls import path
from .views import home, detail

app_name = 'core'

urlpatterns = [
    path('', home, name="home"),
    path('detail/<int:pk>/', detail, name='detail')
]
