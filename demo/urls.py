from django.contrib import admin
from.import views
from django.urls import path,include

urlpatterns = [
    path('',views.userindex,name='userindex'),
    path('login',views.userlogin,name='userlogin'),
    path('logout',views.userlogout,name='userlogout'),
    path('products',views.userproduct,name='userproduct'),
    path('singleproduct/<int:id>',views.usersingleproduct,name='usersingleproduct'),
    path('signup',views.usersignup,name='usersignup'),
    path('contact',views.usercontact,name='usercontact'),
    path('about',views.userabout,name='userabout'),
    path('read',views.readdata,name='readdata'),
    path('cart',views.usercart,name='usercart'),
    path('delete/<int:id>',views.deletedata ,name='deletedata'),
    path('update/<int:id>',views.updatedata,name='updatedata'),
    path('payment',views.userpayment , name='payment'),
    path('details/<int:id>',views.userdetails,name='details'),
    # path('newdetails/<int:id>',views.newdetails,name='newdetails'),
    # path('cartdetails',views.cartdetails,name='cartdetails')
    path('hexadelete/<int:id>',views.hexadelete, name='hexadelete'),
    # path('addtocart',views.addtocart,name='addtocart')
    path('subscribe',views.usersubscribe,name='subscribe')
]