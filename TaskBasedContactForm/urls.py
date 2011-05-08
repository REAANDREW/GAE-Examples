from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	(r'^$', 'views.index'),
	(r'^enquiry/$', 'views.enquiry'),
	(r'^enquiry_submit/$', 'views.enquiry_submit'),
	(r'^enquiry_thanks/$', 'views.enquiry_thanks'),
	(r'^tasks/sendenquiry/$', 'views.enquiry_task_process'),
    # url(r'^forum/', include('forum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
