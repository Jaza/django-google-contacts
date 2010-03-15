from gdata.auth import GenerateAuthSubUrl

from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

from ..utils import google_get_state

register = template.Library()
    
@register.simple_tag
def google_auth_url(request):
    state = google_get_state(request)
    if not state:
        next = '%s%s' % (settings.GOOGLE_REDIRECT_BASE_URL, reverse('google_contacts_login'))
        scope = 'http://www.google.com/m8/feeds/'
        return GenerateAuthSubUrl(next, scope, secure=False, session=True)
    else:
        return reverse('google_contacts_logout')
