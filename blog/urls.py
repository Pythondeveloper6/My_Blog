from django.conf.urls import url , include , patterns
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin


urlpatterns = [

    url(r'^$' , views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$',	views.post_detail),
    url(r'^post/new/$',	views.post_new,	name='post_new'),
    url(r'^about/$',	views.about_us,	name='about_us'),
    url(r'^contact/$',	views.contact_us,	name='contact_us'),
    url(r'^courses/$',	views.courses,	name='courses'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',	views.post_edit,	name='post_edit'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
