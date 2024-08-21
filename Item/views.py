from django.shortcuts import render,get_object_or_404,redirect
from .models import Item 
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from core.decorators import *
# Create your views here.
# 
# 
# grid grid-cols-3 gap-3


def item(request):
    if request.method=="GET":
        query=request.GET.get('query','')
        category_id=request.GET.get('category_id',0)
        categories=Category.objects.all()

        items=Item.objects.filter(is_sold=False)

        if category_id:
            items=items.filter(category_id=category_id)

        if query:
            items=items.filter(Q(name__icontains=query)| Q(description__icontains=query))


    context={'items':items ,'query':query,'categories':categories,'category_id':category_id}
    return render(request,'Item/item.html',context)   

def get_items_by_ids(ids):
    return Item.objects.filter(id__in=ids)

    

def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_Items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:6]
    context={'item': item,'related_Items': related_Items}

    return render(request,'Item/detail.html',context)


def deleteItem(request,pk):
    item=get_object_or_404(Item,pk=pk)
    cart=request.session.get('cart')
    if str(item.id) in cart:
        # cart=request.session.get('cart')
        cart.pop(str(item.id))
        request.session['cart'] = cart
        print("Popped Out")

    print(cart)

    item.delete()
    return render(request,"core/index.html")


def edit(request,pk):
    item=get_object_or_404(Item,pk=pk)
   
    if request.method=='POST':
        form=EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            item=form.save()
        # item.created_by

            return redirect('Item:detail',pk=item.id)
    else:
        form=EditItemForm(instance=item)
        context={'form':form,'title': 'Edit Items ','instance':item}
    # return render(request)



    # return HttpResponse('This is Homepage')
    return render(request,'Item/form.html',context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','Developer'])
def newItem(request):
    form=NewItemForm()
    print("*")
    if request.method=='POST':
        form=NewItemForm(request.POST,request.FILES)
        print("**")
        if form.is_valid():
            print("II")
            item=form.save(commit=False)
            item.created_by=request.user
            print("itemname",item.name)
            item.save()
            return redirect('Item:detail',pk=item.id)

    context={'form':form,'title': 'Add NewItems '}
    # return render(request)



    # return HttpResponse('This is Homepage')
    return render(request,'Item/form.html',context=context)


