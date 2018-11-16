from django.conf.urls import url
from . import views
from . import views as core_views

urlpatterns=[
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^$',views.home,name='home_page'),
]