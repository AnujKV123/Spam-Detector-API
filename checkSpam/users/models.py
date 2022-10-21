from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User (models.Model):
  name = models.TextField(null = False, blank = False)
  phone_number = PhoneNumberField(null = False, blank = False, unique = True)
  email = models.EmailField(null = True, blank = True)
  password = models.CharField(null = False, blank = False, max_length=50)