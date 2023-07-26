from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from rest_framework.authtoken.models import Token


# Custom User Model
class CustomUser(AbstractUser):
    # Add any additional fields you need
    phone_number = models.CharField(max_length=20, blank=True)

    # Define the related_name for groups and user_permissions fields
    # Use unique names to avoid conflicts with the default User model
    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions', blank=True, help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

# Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(
        max_length=100, choices=(("IT", "IT"), ("Non IT", "Non IT"), ("Mobile Phones", "Mobile Phones")), blank=True
    )
    added_data = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Employee Model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    hire_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, default="")

# Custom Token Model
class CustomToken(Token):
    # Add any custom fields or behaviors here if needed.
    # For example, you can add an expiration date to the token.
    expiration_date = models.DateTimeField(default=timezone.now)

    # You can also add any custom methods if required.
    # For example, you can create a method to check if the token has expired.
    def is_expired(self):
        return timezone.now() > self.expiration_date
