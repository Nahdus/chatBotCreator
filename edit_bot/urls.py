from django.conf.urls import include,url
from . import views

app_name='edit_bot'
urlpatterns = [
    #url(r'^$',views.dashboard, name ='dashboard'),
    url(r'^$', views.createFlow_form.as_view(), name='createflow'),
    url(r'^edit/(?P<flow_id>[0-9]+)/$', views.createFlow_form.as_view(), name='editFlow'),
    url(r'^delete/(?P<flow_id>[0-9]+)/$', views.delete_flow, name='deleteFlow'),
        
    
   
]