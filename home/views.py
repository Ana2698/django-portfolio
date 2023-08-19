from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from django.conf import settings
from django.core.mail import send_mail
import os

def home(request):
    #return HttpResponse("This is my homepage")
    return render(request, 'home.html')
def about(request):
    #return HttpResponse("About me")
    return render(request, 'about.html')
def projects(request):
    return render(request, 'projects.html')
def contact(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        message = request.POST.get('desc', None)
        message = fullname + " " + email + " " + phone + " " + message
        send_mail('subject', message, 'settings.EMAIL_HOST_USER', ['anuchatt42@gmail.com'], fail_silently=False)
    return render(request, 'contact.html')
def resume(request):
    file = os.path.join(settings.BASE_DIR, 'archive/resume.pdf') 
    fileOpened = open(file, 'rb')
    return FileResponse(fileOpened)
# Create your views here.

# Create your views here.
