from django.shortcuts import render
from django.http import HttpResponse
from . models import Todolist

# Create your views here.

def index(request):
    Todolistdata=Todolist.objects.all().order_by("created_date")
    return render(request,'index.html',{'Todolistdata':Todolistdata})