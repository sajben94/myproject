from django.conf.urls import url
from myapp import views

app_name = 'myapp'

urlpatterns = [
    # url(r'^$',views.index,name='index2'),
    url(r'^help/',views.help,name='help')
]
