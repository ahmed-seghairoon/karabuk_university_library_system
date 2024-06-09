from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name="home"),
    path('login', view=views.login, name="login"),
    path('logout', view=views.logout, name="logout"),
    path('change-password', views.ChangePasswordView.as_view(), name='change_password'),
    path('book-details/<int:id>', view=views.book_details, name="book_details"),
    path('search-books', view=views.search_books, name="search_books"),
]