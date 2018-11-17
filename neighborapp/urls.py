from django.conf.urls import url,include
from . import views
from . import views as core_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^$',views.home,name='home_page'),
]