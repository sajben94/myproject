from django.conf.urls import url
from myapp import views

app_name = 'myapp'

urlpatterns = [
    # url(r'^$',views.index,name='index2'),
    url(r'^help/',views.help,name='help'),
    url(r'^(?P<id>\d+)/delete/$', views.user_delete,name='deleteuser'),
    url(r'^default/',views.home_default,name='home_default'),
    url(r'^onepage/',views.home_one_page,name='home_one_page')
]
