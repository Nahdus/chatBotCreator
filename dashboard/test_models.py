from django.test import TestCase
from .models import Bot
from django.test import Client
# c = Client()
# response = c.get('/')
# print("status code ",response.status_code)
# response = c.post('/',{'Name': 'abc'})
# print(dir(response))
# print(response.content)
# print("status code ",response.status_code)
# response = c.get('/',{'Name': 'abc'})

print('='*50)
class BotTestCase(TestCase):
    
    c = Client()
       
    def setUp(self):
        response = self.c.post('/',{'Name': 'abc'})
        

    def getPK(self,name):
        pk=Bot.objects.get(Name="abc").pk
        return pk

    def test_pageforBot(self):
        print("executing pageforBot")
        print('Hello Hello')
        print('/'+str(self.getPK()))
        response = self.c.get('/'+str(self.getPK()))
        print(response.status_code)
        self.assertEqual(response.status_code,301)