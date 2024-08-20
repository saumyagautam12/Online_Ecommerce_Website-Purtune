from django.contrib import admin
from django.urls import path,include
# from core.views import *
from . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.urls import path
# from .forms import *
from middleware import *


app_name='dashboard'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include(core.urls))
    path('',views.Dashboard,name='Dashboard'),
    path("razorpaycheck/",views.razorpaycheck,name='razorpaycheck'),
    path('CheckOut',CheckOut.as_view(),name='CheckOut'),
    path('myOrders/',views.myOrders,name='myOrders'),
    path('myOrders/',auth_middleware(views.myOrders),name='myOrders')
    # path('contact/',views.contact,name='contact'),
    # path('signup/',views.signup,name='signup'),
    # path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login')

]
