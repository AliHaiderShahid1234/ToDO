import logging
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Set up logging for debugging
logger = logging.getLogger(__name__)

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created and instance.email:
        send_mail(
            'Welcome to MySite',
            f'Hi {instance.username}, thank you for registering.',
            'ShahidHaiderAlil@gmail.com',
            [instance.email],
            fail_silently=False,
        )

@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    logger.info(f"Sending login alert email to: {user.email}")
    print(f"Sending login alert email to: {user.email}")
    try:
        send_mail(
            'Login Alert',
            f'Hi {user.username}, you just logged in.',
            'ShahidHaiderAlil@gmail.com',
            [user.email], 
            fail_silently=False,
        )
    except Exception as e:
        logger.error(f"Error sending login email: {e}")
        print(f"Error sending login email: {e}")
