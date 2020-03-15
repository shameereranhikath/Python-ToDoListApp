from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import Todolist
from django.utils import timezone

# Create your views here.

def index(request):
    Todolistdata=Todolist.objects.all().order_by("created_date")
    return render(request,'index.html',{'Todolistdata':Todolistdata})

def AddItem(request):
    current_date=timezone.now()
    content1=request.POST["content"]
    Todolist.objects.create(created_date=current_date,text=content1)
    # Todolistdata=Todolist.objects.all().order_by("created_date")
    # return render(request,'index.html',{'Todolistdata':Todolistdata})
    return HttpResponseRedirect('/ToDoListApp/')
    # Redirect('/ToDoListApp/'),


def DeleteItem(request,todo_id):
    Todolist.objects.get(id=todo_id).delete()
    print(todo_id)
    return HttpResponseRedirect('/ToDoListApp/')