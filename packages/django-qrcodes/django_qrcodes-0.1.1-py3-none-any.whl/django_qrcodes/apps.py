from django.apps import AppConfig


class SimpelQrcodeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_qrcodes'
    label = 'django_qrcodes'
    verbose_name = "QR Code"
    icon = "qrcode-scan"
