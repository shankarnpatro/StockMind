# Create your views here.
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import int_to_base36, base36_to_int

from StockMind import settings
from StockMind.environment_mixin import EnvironmentMixin
from apps.usermgmt.models import User
from apps.usermgmt.tokens import account_activation_token


class EmailVerification(EnvironmentMixin):
    def send_email(self, user):
        if self.is_production:
            curr_user = User.objects.get(id=user.id)
            mail_subject = 'Verify your StockMind Account'
            message = render_to_string('email_verification_template.html', {
                'user': curr_user.first_name,
                'domain': settings.CURRENT_DOMAIN,
                'uid': int_to_base36(curr_user.id),
                'token': account_activation_token.make_token(curr_user),
            })
            to_email = curr_user.email
            print(to_email)
            email = EmailMultiAlternatives(mail_subject, message, from_email=settings.DEFAULT_FROM_EMAIL, to=[to_email])
            email.attach_alternative(message, "text/html")
            email.send()

    def activate(self, request, uidb36, token):
        try:
            # uid = int(uidb64)
            uid = base36_to_int(uidb36)
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.email_verified = True
            user.save()
            # return user.email_verified
            return True
            # return HttpResponse('Thank you for confirming your Email.')
        else:
            # return user.email_verified
            return False
            # return HttpResponse('Invalid activation link.')
