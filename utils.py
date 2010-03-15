from django.conf import settings

def google_import(request, gcs, cache=False):
    """
    Uses the given contacts service object to retrieve Google Contacts and
    import the entries with an email address into the contacts of the
    given user.
    
    Returns a list of 'contact name <contact@email>' strings.
    """
    state = google_get_state(request)
    contacts = []
    
    if state == 'authorized':
        if cache and request.session.get('google_contacts_cached'):
            return request.session.get('google_contacts_cached')
        
        gcs.SetAuthSubToken(request.session.get(settings.GOOGLE_COOKIE_CONSENT))
    
        entries = []
        feed = gcs.GetContactsFeed()
        entries.extend(feed.entry)
        next_link = feed.GetNextLink()
        while next_link:
            feed = gcs.GetContactsFeed(uri=next_link.href)
            entries.extend(feed.entry)
            next_link = feed.GetNextLink()
    
        for entry in entries:
            for email in entry.email:
                if email.primary:
                    contact = '%s <%s>' % (entry.title.text, email.address)
                    contacts.append(contact)
        
        if cache:
            request.session['google_contacts_cached'] = contacts
    
    return contacts


def google_get_state(request):
    """
    Get the current login state for the Google Contacts API.
    Possible states are:
    None - logged out
    authorized - logged in and consent granted
    """
    state = None
    if request.session.get(settings.GOOGLE_COOKIE_CONSENT):
        state = 'authorized'
    
    return state
