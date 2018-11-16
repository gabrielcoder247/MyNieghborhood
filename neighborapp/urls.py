from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^$',views.home,name='home_page'),
]