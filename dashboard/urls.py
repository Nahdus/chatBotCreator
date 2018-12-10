


from django.conf.urls import include,url
from . import views



app_name='dashboard'
urlpatterns = [
    #url(r'^$',views.dashboard, name ='dashboard'),
    url(r'^$', views.createBot_form.as_view(), name='home'),
    url(r'^(?P<bot_id>[0-9]+)/',include('edit_bot.urls')),
    url(r'^delete/(?P<bot_id>[0-9]+)/', views.deleteBot, name='deletebot'),
    url(r'^api/Bot/', include('apigate.urls') ),
   
    
]



