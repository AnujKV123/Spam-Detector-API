import json

from rest_framework import serializers

from .models import User
from spam.models import Spam

class UserSerializer (serializers.ModelSerializer):
  spam_report_count = serializers.SerializerMethodField()



  class Meta:
    model = User
    fields = ['id', 'name', 'phone_number', 'email', 'password', 'spam_report_count']
  
  def get_spam_report_count (self, obj: User):
    try:
      spam: Spam = Spam.objects.get(phone_number = obj.phone_number)
    except Spam.DoesNotExist:
      return 0
    return spam.get_report_count()


