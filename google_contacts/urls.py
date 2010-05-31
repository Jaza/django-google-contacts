from django.conf.urls.defaults import *

from views import google_get_state_token, google_login, google_logout

urlpatterns = patterns('',

    url(r'^get-state-token/(?P<action_type_id>\d+)/(?P<action_id>\d+)/$', google_get_state_token, name='google_contacts_get_state_token'),
    url(r'^login/$', google_login, name='google_contacts_login'),
    url(r'^logout/$', google_logout, name='google_contacts_logout'),
    
)
