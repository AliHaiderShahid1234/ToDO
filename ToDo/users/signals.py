import logging
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Set up logging for debugging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created and instance.email:
        try:
            send_mail(
                'Welcome to MySite',
                f'Hi {instance.username}, thank you for registering. To ToDo, I hope you have a great time using this software.',
                settings.DEFAULT_FROM_EMAIL,
                [instance.email],
                fail_silently=False,
            )
            logger.info(f"Welcome email sent to {instance.email}")
        except Exception as e:
            logger.error(f"Error sending welcome email to {instance.email}: {e}")


@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    logger.info(f"Sending login alert email to: {user.email}")
    try:
        send_mail(
            'Login Alert',
            f'Hi {user.username}, you just logged in.',
            settings.DEFAULT_FROM_EMAIL,
            [user.email], 
            fail_silently=False,
        )
        logger.info(f"Login alert email sent to {user.email}")
    except Exception as e:
        logger.error(f"Error sending login email to {user.email}: {e}")
