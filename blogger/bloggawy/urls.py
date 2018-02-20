from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^post/(?P<post_id>[0-9]+)$', views.post_page),
    url(r'^post/(?P<post_id>[0-9]+)/like/$', views.like),  # for like
    url(r'^post/(?P<post_id>[0-9]+)/dislike/$', views.dislike),  # for dislike
    url(r'.success.', views.success),  # for success
    url(r'.error.', views.error),  # for errors
    url(r'^login_form$',views.login_form),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^create$', views.create),
]
