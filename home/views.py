from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def home_view(request):
    views = {}
    views['projects'] = Project.objects.all()
    
    if request.method == 'POST':
        na = request.POST.get('name', '').strip()
        ph = request.POST.get('phone', '').strip()
        e = request.POST.get('email', '').strip()
        mes = request.POST.get('message', '').strip()
        
        # Check if any of the required fields are missing
        if not na or not ph or not e or not mes:
            messages.error(request, "All fields are required.")
            views.update({
                'name': na,
                'phone': ph,
                'email': e,
                'message': mes,
            })
            return render(request, 'portfolio.html', views)
        
        # Create and save the Contact instance if all fields are provided
        data = Contact.objects.create(
            name=na,
            email=e,
            phone=ph,
            message=mes,
        )
        data.save()
        messages.success(request, "Successfully sent")
        return redirect('/')
    
    return render(request, 'portfolio.html', views)