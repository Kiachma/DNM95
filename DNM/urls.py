from django.conf.urls import patterns, include, url

from DNM import views
from DNM.apps.news.events.views import export
from DNM.apps.static_pages.forms import editpage
from DNM.apps.static_pages.views import page
import settings




# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
from DNM.settings import MEDIA_ROOT

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'DNM.views.home', name='home'),
                       # url(r'^DNM/', include('DNM.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       url(r'^statistics/', views.statistics, name="statistics"),
                       url(r'^contact/', views.contact, name="contact"),
                       url(r'^editpage/(?P<page_id>\w+)$', editpage, name="editpage"),

                       url(r'^page/(?P<page_id>\w+)$', page, name="page"),

                       url(r'^news/', include('DNM.apps.news.urls', namespace='news')),
                       url(r'^gallery/', include('DNM.apps.gallery.urls', namespace='gallery')),

                       url(r'^event/', include('DNM.apps.news.events.urls', namespace='event')),
                       url(r'^UserInformation/', include('DNM.apps.members.urls', namespace='UserInformation')),
                       url(r'^signup/', include('DNM.apps.signup.urls', namespace='signup')),
                       url(r'^klotterplanket/', include('DNM.apps.klotter.urls', namespace='klotter')),


                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
                       url(r'^logout/$', views.logout_, name="logout"),

                       url(r'^$', views.base, name="base"),


                       # (r'^admin/(.*)', admin.site.root),


                       url(r'^event/export/', export, name="event_ics_export"),


                       url(r'^user/password/reset/$',
                           'django.contrib.auth.views.password_reset',
                           {'post_reset_redirect': '/user/password/reset/done/'},
                           name="password_reset"),
                       (r'^user/password/reset/done/$',
                        'django.contrib.auth.views.password_reset_done'),
                       (r'^user/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                        'django.contrib.auth.views.password_reset_confirm',
                        {'post_reset_redirect': '/user/password/done/'}),
                       (r'^user/password/done/$',
                        'django.contrib.auth.views.password_reset_complete'),
                       (r'^summernote/', include('django_summernote.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns(
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': MEDIA_ROOT, 'show_indexes': True}), )
