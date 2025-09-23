from django.shortcuts import render
from .models import Contact

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'app_name/index.html', {'contacts': contacts})
