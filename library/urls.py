from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name="home"),
    path('login', view=views.login, name="login"),
    path('logout', view=views.logout, name="logout"),
    path('book-details/<int:id>', view=views.book_details, name="book_details"),
]