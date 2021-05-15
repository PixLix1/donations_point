from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.shortcuts import reverse
from django.contrib.sites.models import Site


def send_register_email(user):
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        # 'login_url': f"http://localhost:8000{reverse('users:account:login')}",
        'login_url': 'http://%s%s' % (Site.objects.get_current().domain, reverse('users:account:login')),
    }
    template = get_template('users/emails/register.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject='Your account has been registered.',
        body=content,
        from_email='pixlix61@gmail.com',
        to=[user.email]
    )
    mail.content_subtype = 'html'
    mail.send()


# def send_register_email(user):
#     send_mail(
#         subject='Your account has been registered.',
#         message=f'Hey {user.first_name} {user.last_name},\nWelcome to our platform.',
#         from_email='pixlix61@gmail.com',
#         recipient_list=[user.email]
#     )
