from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    context={'name':'Shivam','course':'Django'}
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        print(name,email)
        contact=Contact(name=name,email=email)
        contact.save()
    return render(request,'contact.html')
def project(request):
    return render(request,'project.html')