from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class IndexTests(TestCase):
    def test_index_status_code(self):
        ## using the named URL: thats where 'name' attribute has its use in url() method
        url = reverse('index')
        resp = self.client.get(url)
        self.assertEquals(resp.status_code,200)

