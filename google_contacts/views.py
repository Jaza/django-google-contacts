import gdata.contacts.service

from django.conf import settings
from django.shortcuts import redirect

from json_response import JsonResponse
from models import ActionState

def google_get_state_token(request, action_type_id, action_id):
    action_state = ActionState.objects.create(**{
        'action_type_id': action_type_id,
        'action_id': action_id,
        'data': request.GET
    })
    return JsonResponse({'stat': 'ok', 'token': action_state.uuid})

def google_login(request):
    token_login = request.GET.get('token')
    
    if token_login:
        gcs = gdata.contacts.service.ContactsService()
        gcs.SetAuthSubToken(token_login)
        gcs.UpgradeToSessionToken()
        request.session[settings.GOOGLE_COOKIE_CONSENT] = gcs.GetAuthSubToken()
    
    return redirect(request.session.get(settings.GOOGLE_REDIRECT_SESSION_VAR))


def google_logout(request):
    if request.session.get(settings.GOOGLE_COOKIE_CONSENT):
        del request.session[settings.GOOGLE_COOKIE_CONSENT]
    if request.session.get('google_contacts_cached'):
        del request.session['google_contacts_cached']
    return redirect(request.session.get(settings.GOOGLE_REDIRECT_SESSION_VAR))
