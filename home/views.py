from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib import messages

def home(request):

    projects = Project.objects.all()
    context = {'projects': projects}

    messages.success(request, 'Contact me by filling the form below')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']

        if len(name)<3 or len(email)<11 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, content=content)
            contact.save()
            messages.success(request, "Your message has been sent")
    
    return render(request, 'home/index.html', context)