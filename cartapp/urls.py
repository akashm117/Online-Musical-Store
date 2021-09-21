from django.urls import path

from cartapp import views

urlpatterns = [
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('cartlist', views.cartlist, name='cartlist')
]