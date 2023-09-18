import unittest
import json
from BinSize import app
import requests

class BinPackingAPITestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def testNewProblem(self):
        api_command = '/newproblem'
        response = requests.get('http://127.0.0.1:8080/'+ api_command)
        jsonResponse = response.json()
        self.assertIsInstance(jsonResponse['ID'], int)
        self.assertEquals(jsonResponse['bins'], "")
        self.assertEquals(response.status_code, 200)
        


    def testPlaceItem(self):
        api_command = '/placeItem'
        api_input='/1/90'
        response = requests.get('http://127.0.0.1:8080/'+ api_command + '/' + api_input)
        jsonResponse = response.json()
        self.assertIsInstance(jsonResponse['ID'], int)
        self.assertEquals(jsonResponse['size'], '90')
        self.assertEquals(jsonResponse['loc'], 1)
        self.assertEquals(jsonResponse['bins'], "!90")
        self.assertEquals(response.status_code, 200)
        
    
    def testEndProblem(self):
        api_command = '/endproblem'
        api_input='/1'
        response = requests.get('http://127.0.0.1:8080/'+ api_command + '/' + api_input)
        jsonResponse = response.json()
        self.assertIsInstance(jsonResponse['ID'], int)
        self.assertEquals(jsonResponse['size'], '90')
        self.assertEquals(jsonResponse['items'], 1)
        self.assertEquals(jsonResponse['count'], 1)
        self.assertEquals(jsonResponse['wasted'], 0)
        self.assertEquals(jsonResponse['bins'], "!90")
        self.assertEquals(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()