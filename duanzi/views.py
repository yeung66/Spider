from django.shortcuts import render
from duanzi.models import Duanzi
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
# Create your views here.
def home(request):
    d= Duanzi.objects.all()



    return render(request, 'home.html',{"d":d})

