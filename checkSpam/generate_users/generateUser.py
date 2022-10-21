import requests
import random, math
import string

def generateUser ():
  first_name = ''.join(random.sample(string.ascii_lowercase, random.randint(1, 10)))
  last_name = ''.join(random.sample(string.ascii_lowercase, random.randint(1, 10)))
  
  name = first_name + ' ' + last_name
  phone_number = '+91 ' + str(random.randint(5, 9)) + ''.join(random.sample(string.digits, 9))
  email = random.choices(population = [
    '',
    ''.join(
    random.sample(string.ascii_letters, random.randint(5, 10))) +
    '@' +
    random.choice(['gmail', 'yahoo', 'hotmail']) +
    '.' +
    random.choice(['com', 'net', 'org', 'edu'])
  ], weights = [0.2, 0.8], k = 1)[0]

  stringX = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  password = ""
  length = len(stringX)
  for i in range(10) :
    password += stringX[math.floor(random.random() * length)]

  return {'name': name, 'phone_number': phone_number, 'email': email, 'password':password}

url = 'http://127.0.0.1:8000/api/create_user/'

for i in range(10):
  user = generateUser()
  r = requests.post(url, data = user)
  print(i, user)
  print(r.text)