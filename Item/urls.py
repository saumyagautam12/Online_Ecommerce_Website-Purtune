from django.contrib import admin
from django.urls import path,include
from Item.views import *
from . import views

app_name='Item'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include(core.urls))
    path('<int:pk>',views.detail,name='detail'),
    path('delete/<int:pk>',views.deleteItem,name='delete'),
    path('newItem',views.newItem,name="newItem"),
    path('edit/<int:pk>',views.edit,name="edit"),
    # path('item/',views.item,name='item'),
    path('item/',views.listItems,name='listItems'),

    path('api/listItemsapi/', views.listItemsApi, name="listItemsapi"),
    path('api/suggestionapi/', views.suggestionApi, name="suggestionapi"),
]