
from django.contrib import admin
from django.urls import path,include
from core.views import *
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include(core.urls))
    path('',index.as_view(),name='index'),
    path('cart',cart.as_view(),name='cart'),
    path('contact/',views.contact,name='contact'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('login/',Login.as_view(),name='Login'),
    # path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login'),
    path('Logout/',views.Logout,name='Logout'),

]
