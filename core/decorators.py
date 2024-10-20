from django.http import HttpResponse 
from django.shortcuts import redirect 

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('index')

        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func 


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None 

            if request.user.groups.exists():
                groupList=request.user.groups.all()

                for group in groupList :
                    print(group)

                    if group.name in allowed_roles:
                        return view_func(request,*args,**kwargs)

            return HttpResponse('You are not authorized to this Page')


        return wrapper_func 
    return decorator
















        