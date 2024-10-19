from django.shortcuts import render,redirect,HttpResponseRedirect
from Item.models import Category,Item
from Item.views import get_items_by_ids

from .forms import *
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from .decorators import * 
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy


# User=get_user_model()

 

class cart(View):

    def get(self,request):
        if request.session.get('cart'):

            ids=list(request.session.get('cart').keys())
            items=get_items_by_ids(ids)
        # print(items)
        else:
            items={}

        
        return render(request,'core/cart.html',{'items':items})

    def post(self,request):
        item=request.POST.get('item')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        

        if remove:
            print(item,cart,type(item))
            if cart[str(remove)]==1:
                cart.pop(str(remove))
            else:
                cart[str(remove)]-=1
        else:

            if cart:
                if item in cart:
                    cart[item]+=1 
                else:
                    cart[item]=1 
            else:
                cart={}
                cart[item]=1

        print(cart)

        request.session['cart']=cart 
        return redirect('cart')







# Create your views here.

class index(View):
    def post(self,request):
        item=request.POST.get('item')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        # print(request.user.groups.all.0.name,"Check")
        

        if remove:
            print(item,cart,type(item))
            if cart[str(remove)]==1:
                cart.pop(str(remove))
            else:
                cart[str(remove)]-=1
        else:

            if cart:
                if item in cart:
                    cart[item]+=1 
                else:
                    cart[item]=1 
            else:
                cart={}
                cart[item]=1

        print(cart)

        request.session['cart']=cart 
        return redirect('index')


        


    def get(self,request):
        query=request.GET.get('query','')
        category_id=request.GET.get('category',0)
        # category_id=request.GET['category']
        

        categories=Category.objects.all()

        items=Item.objects.filter(is_sold=False)

        if category_id:
            print("CHeck")
            items=items.filter(category_id=category_id)

        if query:
            items=items.filter(Q(name__icontains=query)| Q(description__icontains=query))


        

        # items=Item.objects.filter(is_sold=False)[0:6]
        print(items)
        categories=Category.objects.all()
        print(categories)
        # context={ categories :'categories',
        # items :'items'}
        # for item in items:
        #     print(item.name)
        #     print(item.price)

        return render(request,'core/index.html',{'items':items,'categories':categories})

# def index(request):
    

def contact(request):
    return render(request, 'core/contact.html')



class SignUpView(CreateView):
    form_class = SignUpForm
    model = CustomUser
    template_name='core/SignUp.html'
    success_url = reverse_lazy('Login') 


class Login(LoginView):
    # form_class=LoginForm 
    # model=CustomUser 
    template_name='core/login.html'
    success_url=reverse_lazy('index') 

# class Logout(LogoutView):
#     success_url=reverse_lazy('index') 

# def signup(request):
#     form=SignupForm()

#     if request.method=='POST':

#         form=SignupForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             # Customer.objects.create(user=user,first_name=user.first_name,last_name=user.last_name,email=user.email,phone=user.phone,)

#             return redirect('login')
#     msg=False


#     context={'form':form,'msg':msg}
#     # return render(request)

#     # return HttpResponse('This is Homepage')
#     return render(request,'core/signup.html',context=context)


# @unauthenticated_user
# def login(request):
#     # returnUrl=request.GET.get('return_url')
#     # returnUrl=request.GET.get('return_url')          -------- land with the same earlier url which was before after login 

#     if request.method=="POST":
#         # name=request.POST.get('name')
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         # password2=request.POST.get('password2')

#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             # messages.info(request,'Welcome')
#             # if returnUrl :
#             #     return HttpResponseRedirect(returnUrl)
                
#             # else:
#                 # returnurl=None
#             return redirect("index")

#             # Redirect to a success page.
        
#         else:

#             # messages.info(request,'Invalid Credentials')
#             return render(request,'core/login.html')

#     # return HttpResponse('This is about Page')
#     else:
#         # return render(request,'about.html')
#         return render(request,'core/login.html')

#     # return HttpResponse('This is Login page')
#     # return render(request,'index.html')
#     # return render(request,'core/login.html')


def Logout(request):
    request.session.clear()
    auth.logout(request)
    print("logout")



    return redirect('index')

#     return redirect('login')


# @login_required(login_url='Login')
# def Logout(request):
    
#     return redirect('Home')

    
