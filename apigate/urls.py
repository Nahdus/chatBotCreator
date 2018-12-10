


from django.conf.urls import include,url

from . import views




app_name='dashboard'
urlpatterns = [
    url(r'^$',views.Botlist.as_view()),
    url(r'flows',views.FlowViewList.as_view()),
    url(r'^(?P<bot_id>[0-9]+)$',views.BotFlowViewList.as_view()),
]



