from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^posts$', views.all_posts),
    url(r'^(?P<p_id>[0-9]+)$', views.post_details),
    url(r'^post/new$',views.new_post),
    url(r'^$', views.index), 
    url(r'^post/(?P<post_id>[0-9]+)$', views.comment),
    url(r'^post/(?P<post_id>[0-9]+)/like/$', views.like),  # for like
    url(r'^post/(?P<post_id>[0-9]+)/dislike/$', views.dislike),  # for dislike
    url(r'.success.', views.success),  # for success
    url(r'.error.', views.error),  # for errors

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
