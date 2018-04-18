from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'(?P<id>\d+)$',views.show, name='show'),
    url(r'(?P<id>\d+)/edit',views.edit, name='edit'),
    url(r'add$',views.add, name ='add'),
    url(r'(?P<id>\d+)/delete$', views.delete, name='delete'),
    url(r'create$',views.create),
    url(r'(?P<id>\d+)/update$',views.update)
]