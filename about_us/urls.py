from django.conf.urls.defaults import *


urlpatterns = patterns('about_us.views',
    url(r'^$', 'home', name='home'),
    url(r'^check\-person/(?P<person_id>\d+)/$', 'check_person'),
)