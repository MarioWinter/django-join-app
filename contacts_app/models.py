from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?\d{1,3}?\d{4,14}$', message="Enter a valid phone number.")]
    )
    bgcolor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
