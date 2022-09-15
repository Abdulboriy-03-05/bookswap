from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "account"
urlpatterns = [
    path('', views.ProfileView.as_view(), name="deatil"),
    path('login/', LoginView.as_view(template_name="main/login.html" , success_url="/"), name="login"),
    path('logout/', LogoutView.as_view(template_name="main/logout.html"), name="logout"),
    path("register/", views.register, name='register'),
    path("update/", views.ProfileUpdate.as_view(), name='update'),
]