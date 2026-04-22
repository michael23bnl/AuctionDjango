from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone


@shared_task
def send_lot_created_email(email, lot_name):
    send_mail(
        subject='Лот успешно создан',
        message=f'Ваш лот "{lot_name}" успешно размещён {timezone.now().strftime('%d.%m.%Y %H:%M:%S')}',
        from_email='mikhail.malyshev.2002@mail.ru',
        recipient_list=[email],
        fail_silently=False,
    )


