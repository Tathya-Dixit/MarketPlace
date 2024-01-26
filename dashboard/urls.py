from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path("",views.dashboard,name='dashboard'),
    path("delete<int:pk>/",views.deleteItem, name='delete'),
    path("edit<int:pk>/",views.editItem, name='edititem'),
]