from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'localspotifyclient.views.home', name='home'),
     url(r'^playpause/', 'localspotifyclient.views.playpause', name='playpause'),
     url(r'^next/', 'localspotifyclient.views.next', name='next'),
     url(r'^previous/', 'localspotifyclient.views.previous', name='previous'),
     url(r'^shuffle/', 'localspotifyclient.views.shuffle', name='shuffle'),
     url(r'^volumeup/', 'localspotifyclient.views.volumeup', name='volumeup'),
     url(r'^volumedown/', 'localspotifyclient.views.volumedown', name='volumedown'),
     url(r'^mute/', 'localspotifyclient.views.mute', name='mute')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
