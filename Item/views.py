from django.shortcuts import render,get_object_or_404,redirect
from .models import Item 
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from core.decorators import *

from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, View
# Create your views here.
# 
# 
# grid grid-cols-3 gap-3


def item(request):
    if request.method=="GET":
        query=request.GET.get('query','')
        category_id=request.GET.get('category',0)
        categories=Category.objects.all()

        print(category_id,type(category_id))
        

        items=Item.objects.filter(is_sold=False)
       

        if category_id:
            
            items=items.filter(category_id=category_id)
            print(items)

        if query:
            items=items.filter(Q(name__icontains=query)| Q(description__icontains=query))


    context={'items':items ,'query':query,'categories':categories,'category_id':int(category_id)}
    return render(request,'Item/item.html',context)  



class ListItems(ListView):
    template_name = "item/item1..html"
    model = Item
    context_object_name = "item"
    paginate_by = 2



from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.http import JsonResponse
ITEMS_PER_PAGE = 3
def listItems(request):
    
    ordering = request.GET.get('ordering', "")     # http://www.wondershop.in:8000/listproducts/?page=1&ordering=price
    search = request.GET.get('query', "")
    price = request.GET.get('price', "")
    category_id=request.GET.get('category',0)
    categories=Category.objects.all()


    if search:
        item = Item.objects.filter(Q(name__icontains=search) )    #| Q(category__contains=search)) # SQLite doesn’t support case-sensitive LIKE statements; contains acts like icontains for SQLite

    else:
        item = Item.objects.all()

    if ordering:
        item = item.order_by(ordering) 

    if price:
        item = item.filter(price__lt = price)

    if category_id:
            
            item=item.filter(category_id=category_id)
            # print(items)


    
    

    # Pagination
    page = request.GET.get('page',1)
    item_paginator = Paginator(item, ITEMS_PER_PAGE)
    try:
        item = item_paginator.page(page)
    except EmptyPage:
        item = item_paginator.page(item_paginator.num_pages)
    except:
        item = item_paginator.page(ITEMS_PER_PAGE)
    return render(request, "Item/item4.html", {"items":item, 'page_obj':item, 'is_paginated':True, 'paginator':item_paginator,'categories':categories,'category_id':int(category_id),'query':search}) 


def suggestionApi(request):
    if 'term' in request.GET:
        search = request.GET.get('term')
        qs = Item.objects.filter(Q(name__icontains=search))[0:10]
        # print(list(qs.values()))
        # print(json.dumps(list(qs.values()), cls = DjangoJSONEncoder))
        titles = list()
        for item in qs:
            titles.append(item.name)
        #print(titles)
        # if len(qs)<10:
        #     length = 10 - len(qs)
        #     qs2 = Item.objects.filter(Q(category__icontains=search))[0:length]
        #     for item in qs2:
        #         titles.append(item.category)
        return JsonResponse(titles, safe=False)      # [1,2,3,4] ---> "[1,2,3,4]"   queryset ---> serialize into list or dict format ---> json format using json.dumps with a DjangoJSONEncoder(encoder to handle datetime like objects)




def listItemsApi(request):
    # print(Product.objects.all())
    # print(Product.objects.values())
    #result = json.dumps(list(Product.objects.values()), sort_keys=False, indent=0, cls=DjangoJSONEncoder)   # will return error if you have a datetime object as it is not jsonserializable  so thats why use DjangoJSONEncoder, indent to beautify and sort_keys to sort keys
    #print(type(result))    #str type  
    #print(result)
    result = list(Item.objects.values())          # will work like passing queryset as a context data if used by a template
    #print(result)
    #return render(request, "firstapp/listproducts.html", {"product":result})
    return JsonResponse(result, safe=False)






def get_items_by_ids(ids):
    return Item.objects.filter(id__in=ids)

    

def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_Items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:6]
    context={'item': item,'related_Items': related_Items}

    return render(request,'Item/detail.html',context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','Developer'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','Developer'])
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


