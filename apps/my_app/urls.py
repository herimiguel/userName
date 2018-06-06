from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
    url(r'^submit_user$', views.submit_user),
    url(r'^success$', views.success),
    url(r'^delete_user/(?P<id>\d+)$', views.delete_user)
]
