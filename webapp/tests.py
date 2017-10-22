from django.test import TestCase

class TestCalls(TestCase):

    def test_sanity_check(self):
        print('SANITY CHECK')
        self.assertTrue(True)

    def test_call_hello_world(self):
        response = self.client.get('/webapp/')
        self.assertTrue('<h2>Hello World!</h2>'.encode('utf-8') in response.content)
