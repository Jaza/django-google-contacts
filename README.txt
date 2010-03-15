google_contacts
===============

Allows you to retrieve the contacts from the Gmail account of a user of your
site, via Google's APIs.

Dependencies:

- gdata-python-client
  http://code.google.com/p/gdata-python-client/

- json_response
  http://www.djangosnippets.org/snippets/154/
  (save this snippet in a file on your PYTHONPATH called json_response.py)

- django-picklefield
  http://github.com/shrubberysoft/django-picklefield
  (save the fields.py file on your PYTHONPATH and rename it picklefield.py)

Installation instructions:

1. Place the google_contacts directory somewhere in your PYTHONPATH.

2. Ensure that all the dependencies (listed above) are installed.

3. Define the following variables in your project's settings.py file:

-----------------------------------------------------------------------------

GOOGLE_COOKIE_CONSENT = 'google_token_consent'

(the value can be whatever you want, as long as it's a unique cookie name
within your project)

GOOGLE_REDIRECT_SESSION_VAR = 'google_contacts_redirect'

(the value can be whatever you want, as long as it's a unique session var
within your project)

GOOGLE_REDIRECT_BASE_URL = 'http://localhost:8000'
(should be whatever the base URL of your site is)

-----------------------------------------------------------------------------

4. Use code similar to the following, in the view for which you want to
   display the contact import functionality:

-----------------------------------------------------------------------------

import gdata.contacts.service

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from google_contacts.utils import google_get_state, google_import

def test_page(request):
    request.session[settings.GOOGLE_REDIRECT_SESSION_VAR] = request.path
    
    google_state = google_get_state(request)
    gcs = gdata.contacts.service.ContactsService()
    google_contacts = google_import(request, gcs, cache=True)
        
    return render_to_response('test_page.html', {
        'google_state': google_state,
        'google_contacts': google_contacts
    }, context_instance=RequestContext(request))

-----------------------------------------------------------------------------

5. Use code similar to the following, in the template for which you want to
   display the contact import functionality:

-----------------------------------------------------------------------------

{% load google_contacts %}

<p>
{% if google_state %}
  Using imported contacts from Gmail [<a
  href="{% google_auth_url request %}">stop using</a>]
{% else %}
  Import contacts from <a
  href="{% google_auth_url request %}">Gmail</a>
{% endif %}
</p>

{% if google_contacts %}
<ul>
  {% for contact in google_contacts %}
  <li>{{ contact }}</li>
  {% endfor %}
</ul>
{% endif %}

-----------------------------------------------------------------------------
