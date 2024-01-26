from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm
app_name = 'core'

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contactPage,name='contactpage'),
    path('signup/',views.signUp,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html', authentication_form = LoginForm),name='login'),
    path('logout/',views.logoutView,name='logout'),
]