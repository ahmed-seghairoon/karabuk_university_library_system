from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from . import models, forms


@login_required(login_url='login')
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


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("login")


@login_required(login_url='login')
def book_details(request, id):
    book = get_object_or_404(models.Book, pk=id)
    book.views += 1
    book.save()
    return render(request,"book-details.html", {'book': book})
