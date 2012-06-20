from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.conf import settings
#from app_one.views import LoginPage
from app_one.views import myaccount,list_files,csv_data 
import registration
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
       
    url(r'^$', redirect_to, {'url': '/accounts/login'}),
    url(r'^myaccount/$',myaccount),
    url(r'^list_files/$',list_files),
    url(r'^csv_data/$',csv_data),
    url( r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT} ),
       
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),


)
