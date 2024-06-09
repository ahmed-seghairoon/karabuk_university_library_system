from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from . import models, forms

def home(request):
    categories = models.Category.objects.all()
    
    data = dict()

    data["Latest Arrivals"] = models.Book.objects.order_by('-created_at')[:10]

    for category in categories:
        data[category.name] = models.Book.objects.filter(category=category)[:10]


    return render(request, 'home.html', {"data":data})


def login(request):
    if request.method == "POST":
        form = forms.UserLoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("home")
    else:
        form = forms.UserLoginForm()
    return render(request, 'login.html', {'form':form})
