from django.conf.urls import url,include
from . import views
from . import views as core_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^$',views.homePage,name='home_page'),
    url(r'^search/', views.search_business, name='search_business'),
    url(r'^join/(\d+)', views.join, name='join'),
    url(r'^exit/(\d+)', views.exit, name='exit'),
    url(r'^business/(\d+)', views.business, name='business'),
    url(r'^neighborhood/(\d+)', views.neighborhood, name='neighborhood'),
    url(r'^new/business$', views.new_business, name='new_business'),
    url(r'^new/neighborhood$', views.new_neighborhood, name='new_neighborhood'),
    url(r'^new/image$', views.new_image, name='new_image'),
    url(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    url(r'^profile/(?P<username>[0-9]+)$',views.profile, name='profile'),

  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)