from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home/', 'myapp.views.home', name='home'),
    url(r'^hvotes/', 'myapp.views.gadb_action', name='gadb_action'),
    url(r'^hmembers/', 'myapp.views.gadb_bill', name='gadb_bill'),
    url(r'^svotes/', 'myapp.views.gadb_legislator', name='gadb_legislator'),
    url(r'^smembers/', 'myapp.views.gadb_stats', name='gadb_stats'),
    

    url(r'^$', 'myapp.views.index', name='index'),
    url(r'^$', include('myapp.urls')),
    url(r'^admin/', include(admin.site.urls)),

)


