from django.test import TestCase
from django.test import Client
c = Client()
response = c.get('/')
print("status code ",response.status_code)
response = c.post('/',{'Name': 'abc'})
# print(dir(response))
# print(response.content)
print("status code ",response.status_code)
# response = c.get('/',{'Name': 'abc'})
