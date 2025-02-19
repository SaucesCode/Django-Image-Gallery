from django.shortcuts import render
from .models import Images

# Create your views here.

def home(request):
    data = Images.objects.all().order_by('?')
    return render(request, 'gallery.html', {'data': data})