from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('add/',views.addItem),
    path('update/<int:pk>/',views.updateItem),
    path('item/<int:pk>/delete/',views.deleteItem),
]
