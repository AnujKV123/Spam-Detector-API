import json

from rest_framework import serializers
from .models import Spam

class SpamSerializer (serializers.ModelSerializer):
  report_count = serializers.SerializerMethodField()

  class Meta:
    model = Spam
    fields = ['id', 'phone_number', 'reports', 'report_count']

  def get_report_count (self, obj: Spam) -> int:
    return obj.get_report_count()