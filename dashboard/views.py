from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required 
from Item.models import * 
from Item.views import *
from .models import * 
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from core.templatetags.cart import * 
import razorpay
from middleware.auth import  *
from core.decorators import * 


@login_required
@allowed_users(allowed_roles=['admin','Developer'])
def Dashboard(request):
    items=Item.objects.filter(created_by=request.user) 

    
    context={'items':items,'title':'Dashboard'}
    print(items)

    return render(request,'dashboard/index.html',context)


@login_required
def razorpaycheck(request):
    cart=request.session.get('cart')
    print(cart)
    items=get_items_by_ids(list(cart.keys()))
    return JsonResponse({

            'total_price': cart_total_price(items,cart)


        })
    # return HttpResponse('my razorpaycheck')


@auth_middleware
def myOrders(request):
    
    all_orders=Order.objects.filter(user=request.user).order_by('-date')
    # [:length(cart)]
    items=Item.objects.all()

    
    
    context={"orders":all_orders,"items":items}

    return render(request,'dashboard/orders.html',context)
    # return HttpResponse('my orders')




client = razorpay.Client(auth=("RAZOR_KEY_ID", "RAZOR_KEY_SECRET"))

# def verify_payment(payment_id):
#     try:
#         payment = client.payment.fetch(payment_id)
#         if payment['status'] == 'captured':
#             return True
#         else:
#             return False
#     except Exception as e:
#         print(f"Payment verification failed: {str(e)}")
#         return False
        
    
    



class CheckOut(View):
    def post(self,request):
        user = request.user
        fname=request.POST.get('Fname')
        lname=request.POST.get('Lname')
        phone=request.POST.get('Phone')
        address=request.POST.get('Address')
        city=request.POST.get('City')
        state=request.POST.get('State')
        pincode=request.POST.get('Pincode')
        payment_id=request.POST.get('payment_id')
       
        cart=request.session.get('cart')
        print(cart,user)
        items=get_items_by_ids(list(cart.keys()))

        # if not verify_payment(payment_id):
        #         return JsonResponse({'status': "Payment verification failed"}, status=400)

        print(address,phone,fname,lname,phone,address,city,state,pincode )

        for item in items:
            print(item.id,type(item.id))
            order=Order(user=user,fname=fname,lname=lname,phone=phone,address=address,city=city,state=state,pincode=pincode,payment_id=payment_id,item=item,quantity=cart[str(item.id)],price=item.price)

            order.save()
            print("Order saved")

        

        
        request.session['cart']={}

        return JsonResponse({'status': "Your order successfully placed " })
        # messages.info(request,'Order successfully placed!!')

        
        # return redirect('cart')


# Create your views here.
