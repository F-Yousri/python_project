"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.index),  # http://127.0.0.1:8000/opensource/
    # url(r'^posts$', views.all_posts),
    # url(r'^(?P<post_id>[0-9]+)$', views.post_details),
    #    url(r'^post/new$', views.new_post),
    url(r'^post/(?P<post_id>[0-9]+)$', views.comment),
    url(r'^post/(?P<post_id>[0-9]+)/like/$', views.like),  # for like
    url(r'^post/(?P<post_id>[0-9]+)/dislike/$', views.dislike),  # for dislike
    url(r'.success.', views.success),  # for success
    url(r'.error.', views.error),  # for errors


    url(r'^posts$', views.all_posts),
    url(r'^(?P<p_id>[0-9]+)$', views.post_details),
    #url(r'^post/new$', views.new_post),
    url(r'^login_form$',views.login_form),
    # url(r'^register$',views.resgister),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^create$', views.create),

    # url(r'^$', views.index),#http://127.0.0.1:8000/opensource/
    # url(r'^home$', views.home),#http://127.0.0.1:8000/opensource/home
    # url(r'^(?P<post_id>[0-9]+)/$',views.name),#http://127.0.0.1:8000/opensource/1/ ... details for student
    # url(r'^(?P<category_id>[0-9]+)/age$',views.age),#http://127.0.0.1:8000/opensource/99/age
    # url(r'^allstudents/$',views.allstudents),#http://127.0.0.1:8000/opensource/allstudents/
    # url(r'^student/new/$',views.newstudent),
]
