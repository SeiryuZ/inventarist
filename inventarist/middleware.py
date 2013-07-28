from django.conf import settings
from django.utils import translation


# Taken from here http://source.mihelac.org/2009/11/12/django-set-language-for-admin/
class AdminLocaleURLMiddleware:

    def process_request(self, request):
        if request.path.startswith('/admin'):
            request.LANG = getattr(settings, 'ADMIN_LANGUAGE_CODE', settings.LANGUAGE_CODE)
            translation.activate(request.LANG)
            request.LANGUAGE_CODE = request.LANG
