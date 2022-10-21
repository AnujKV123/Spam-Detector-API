import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from phonenumber_field.phonenumber import PhoneNumber
from phonenumbers import NumberParseException

from .models import Spam
from .serializers import SpamSerializer

from users.models import User

@api_view(['GET'])
def spamLists (request, format = None):
  spams = Spam.objects.all()
  for spam in spams:
    spam.report_count = len(json.loads(spam.reports))
  serializer = SpamSerializer(spams, many = True)
  return Response({'spam': serializer.data}, status = status.HTTP_200_OK)

@api_view(['POST'])
def reportSpam (request, format = None):
  try:
    phone_number = PhoneNumber.from_string(request.data.get('phone_number'))
    id = request.data.get('id')
  except NumberParseException:
    return Response({'status': 'failure', 'error': 'parsing exception due to invalid phonenumber'}, status = status.HTTP_400_BAD_REQUEST)
  except AttributeError:
    return Response({'status': 'failure', 'error': 'missing attribute(s): phone_number, id'}, status = status.HTTP_400_BAD_REQUEST)
  
  try:
    spam = Spam.objects.get(phone_number = phone_number)
  except Spam.DoesNotExist:
    spam = Spam.objects.create(phone_number = phone_number)
  try:
    user = User.objects.get(id = id)
  except User.DoesNotExist:
    return Response({'status': 'failure', 'error': 'user does not exist'}, status = status.HTTP_400_BAD_REQUEST)
  
  report_list = json.loads(spam.reports)
  if user.id not in report_list:
    report_list.append(user.id)
  spam.reports = json.dumps(report_list)
  spam.save()
  serializer = SpamSerializer(spam)
  return Response({'status': 'success', 'spam': serializer.data}, status = status.HTTP_200_OK)
