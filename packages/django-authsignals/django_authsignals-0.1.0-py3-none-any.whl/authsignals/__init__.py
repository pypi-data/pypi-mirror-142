from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.conf import settings


superusers = []
if hasattr(settings, 'AUTHSIGNALS_SUPERUSERS'):
    superusers = settings.AUTHSIGNALS_SUPERUSERS


@receiver(user_logged_in)
def superuser_mapper(sender, request, user, **kwargs):
    if user and not user.is_superuser and \
       user.username in superusers:
        user.is_superuser = True
        user.save()
