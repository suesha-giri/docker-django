from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from MyApi.views import api

# Create your tests here.

class URLResolverTestCase(APITestCase):

    def test_url_resolve(self):
        url=reverse('api')
        self.assertEqual(resolve(url).func,api)


class ApiViewTestCase(APITestCase):

    def test_url_returns_200(self):
        url='/api'
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)


class DatabaseApiViewTestCase(APITestCase):

    def test_get_data_from_database(self):   
        data = {"id": 1, "name":"John" , "age":24}
        response = self.client.get("/dblist",data)
        self.assertEqual(response.status_code, 200)



    

        



