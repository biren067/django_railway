from django.shortcuts import render

def home(request):
    return render(request,template_name='blog/home.html')
# Create your views here.
