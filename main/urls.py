from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "main"
urlpatterns = [
    path('', views.homeView, name="index"),
    path('book-list/', views.BooksView, name="book-list"),
    path('mybooks/', views.MyBookView, name="my-book"),
    path("delete/<slug:url>/", views.delete_view, name='delete'),
    path('book-list/<slug:slug>', views.BookView, name="detail"),
    path('update/<slug:url>/', views.UpdateBook.as_view(), name="edit"),
    path("create_advert/", views.BookCreate.as_view(), name="create-book"),
    
]