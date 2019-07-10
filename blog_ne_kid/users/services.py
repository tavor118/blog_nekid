from django.core.mail import send_mail
from django.template import loader


def send_notification_email(user):
    subject = '[Django Blog] New post in your subscriptions.'
    message = loader.render_to_string(
        'notification_about_new_post.html',
        {
            'user_name': user.username,
        }
    )
    send_mail(
        subject,
        message,
        'djangoblog@gmail.com',
        [user.email],
        fail_silently=True
    )
