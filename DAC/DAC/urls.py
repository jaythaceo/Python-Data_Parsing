from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'information.views.home', name='home'),
    url(r'^thank-you/$', 'information.views.thankyou', name='thankyou'),
    url(r'^about-us/$', 'information.views.aboutus', name='aboutus'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

