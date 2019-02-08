
from django.urls import path, include
from.import views

app_name = 'retail'
urlpatterns = [

    path('', views.retailPrice_start, name="price"),

]
