from django.test import TestCase
import time
from . import storage

class TestCalls(TestCase):

    def test_sanity_check(self):
        print('SANITY CHECK')
        self.assertTrue(True)

    def test_webapp_reposnse_contains_hello_world(self):
        print("Webapp response contains 'Hello world!' html")
        response = self.client.get('/webapp/')
        self.assertTrue('<h2>Hello world!</h2>'.encode('utf-8') in response.content)

    def test_can_get_last_stored_unix_timestamp(self):
        response = self.client.get('/webapp/')
        storage.Storage_Of.print_timestamp()
        self.assertTrue(str(storage.Storage_Of.timestamp).encode('utf-8') in response.content)
