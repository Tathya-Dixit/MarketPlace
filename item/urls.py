from django.urls import path
from item import views

app_name = 'item'

urlpatterns = [
    path("<int:pk>/",views.detailPage,name='detail'),
    path("additem/",views.newItem,name='newitem'),
    path("browse/",views.browse,name='browse'),
]