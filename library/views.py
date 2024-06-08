from django.shortcuts import render
from . import models

def home(request):
    categories = models.Category.objects.all()
    
    data = dict()

    data["Latest Arrivals"] = models.Book.objects.order_by('-created_at')[:10]

    for category in categories:
        data[category.name] = models.Book.objects.filter(category=category)[:10]


    return render(request, 'home.html', {"data":data})
