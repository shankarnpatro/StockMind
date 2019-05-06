from celery import shared_task

from apps.usermgmt.views import EmailVerification


@shared_task
def send_verification_email(user):
    email = EmailVerification()
    return email.send_email(user)
