from django.core.mail import send_mail
from django.conf import settings


def send_otp(email,otp):
    send_mail(
        subject='OTP Verify Account',
        message=f'Your OTP is {otp}\n It will expire in 5 minutes',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )