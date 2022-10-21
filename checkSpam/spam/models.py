import json

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Spam (models.Model):
  phone_number = PhoneNumberField(null = False, blank = False, unique = True)
  reports = models.TextField(default = json.dumps([]))

  def get_report_count (self) -> int:
    return len(json.loads(self.reports))