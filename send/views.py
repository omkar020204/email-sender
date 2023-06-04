from django.shortcuts import render,redirect
from django.http import HttpResponse
from .utils import send_email_to_client
from django.shortcuts import redirect
def index(request):
    if request.method=='POST':
        message=request.POST.get('message','')
        title=request.POST.get('title','')
        email=request.POST.get('email','')
        print(message,title)
        send_email_to_client(title,message,email)
        return redirect('home')
    return render(request,'send/index.html')