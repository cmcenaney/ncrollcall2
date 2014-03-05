from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home/', 'myapp.views.home', name='home'),
    url(r'^bills/', 'myapp.views.bill', name='gadb_bill'),
    url(r'^members/$', 'myapp.views.member', name='gadb_legislator'),


    
   	url(r'^members/(?P<pk>\d+)$', 'myapp.views.each_member', name='each_member'),
    url(r'^bills/(?P<bill_id>\d+)/$', 'myapp.views.bill', name='gadb_bill'),



    url(r'^$', 'myapp.views.index', name='index'),
    url(r'^$', include('myapp.urls')),
    url(r'^admin/', include(admin.site.urls)),

)


