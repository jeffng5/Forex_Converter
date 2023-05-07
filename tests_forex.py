from unittest import TestCase
import requests

# getting API info
url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
assert response.status_code == 200
data = response.json()

#class for unit testing
class ForexTest(TestCase):
    def tests_forex(self):
        self.assertIsNotNone(response) #testing that api call return something
        self.assertIsNotNone(data['rates']) #testing that api has exchange rates
