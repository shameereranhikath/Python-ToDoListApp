from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('AddItem/',views.AddItem),
    path('DeleteItem/<int:todo_id>/',views.DeleteItem),

   
  
]