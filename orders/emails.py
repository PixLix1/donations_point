from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.shortcuts import reverse
from django.contrib.sites.models import Site
from donations_point.settings import EMAIL_HOST_USER


def send_donation_approval_email(user, product_name):
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'product_name': product_name,
        'products_url': 'http://%s%s' % (Site.objects.get_current().domain, reverse('products:items:list')),
    }
    template = get_template('orders/emails/donation_approved.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject='Your donation request has been approved.',
        body=content,
        to=[user.email]
    )
    mail.content_subtype = 'html'
    mail.send()


def send_donation_rejection_email(user, product_name):
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'product_name': product_name,
        'products_url': 'http://%s%s' % (Site.objects.get_current().domain, reverse('products:items:list')),
    }
    template = get_template('orders/emails/donation_declined.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject='Your donation request was declined.',
        body=content,
        to=[user.email]
    )
    mail.content_subtype = 'html'
    mail.send()


def send_product_donated_bulk_email(user_list, product_name):
    context = {
        'product_name': product_name,
        'products_url': 'http://%s%s' % (Site.objects.get_current().domain, reverse('products:items:list')),
    }
    template = get_template('orders/emails/product_not_available.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject='Product donated to another member',
        body=content,
        to=[EMAIL_HOST_USER],
        bcc=user_list,
    )
    mail.content_subtype = 'html'
    mail.send()
