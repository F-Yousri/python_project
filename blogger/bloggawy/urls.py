from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
   
    url(r'^registeration$',views.registeration),
    url(r'^allusers$',views.allusers),
    url(r'^adminpanel$',views.adminpanel),
    url(r'^allposts$',views.allposts),
    url(r'^allcategories$',views.allcategories),
    url(r'^(?P<st_id>[0-9]+)/Category/edit$',views.editcategory),
    url(r'^(?P<st_id>[0-9]+)/Category/delete$',views.deletecategory),
    url(r'^Category/add$',views.addcategory),
    url(r'^(?P<st_id>[0-9]+)/Post/showpost$',views.showpost),
    url(r'^(?P<st_id>[0-9]+)/Post/deletepost$',views.deletepost),
    url(r'^Post/addpost$',views.addpost),
    url(r'^(?P<st_id>[0-9]+)/Post/editpost$',views.editpost),
    url(r'^forbiddenwords$',views.forbiddenwords),
    url(r'^(?P<st_id>[0-9]+)/deleteword$',views.deleteword),
    url(r'^(?P<st_id>[0-9]+)/editword$',views.editword),
    url(r'^Curse/add$',views.addcurse),
    url(r'^Tags$',views.tags),
    url(r'^(?P<st_id>[0-9]+)/deletetag$',views.deletetag),
    url(r'^(?P<st_id>[0-9]+)/edittag$',views.edittag),
    url(r'^Tag/add$',views.addtag)





    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)