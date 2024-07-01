from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def Gallery(request):
    return render(request,'Gallery.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
def info(request):
    return render(request,'info.html')
def homework(request):
    return render(request,'homework.html')
def form(request):
    return render(request,'form.html')