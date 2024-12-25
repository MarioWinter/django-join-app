from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

class Contact(models.Model):
    """
    Contact model representing a user's contact information.
    Attributes:
        user (ForeignKey): Reference to the user who owns the contact.
        username (CharField): The username of the contact.
        email (EmailField): The email address of the contact.
        phone (CharField): The phone number of the contact, validated with a regex pattern.
        bgcolor (CharField): The background color associated with the contact.
    Methods:
        __str__(): Returns the username of the contact as its string representation.
    """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts')
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?(?:[0-9] ?){6,14}[0-9]$', message="Enter a valid phone number")],
        blank=True,
        null=True
    )
    bgcolor = models.CharField(max_length=100)

    def __str__(self):
        return self.username
