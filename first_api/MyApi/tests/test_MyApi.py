from django.http import response
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.

# class URLResolverTestCase(APITestCase):

#     def test_url_resolve(self):
#         url=reverse('api')
#         self.assertEqual(resolve(url).func,api)


class ApiViewTestCase(APITestCase):

    def test_url_returns_401(self): #returns 401 because we require authenication
        url='/api'
        response=self.client.get(url)
        self.assertEqual(response.status_code, 401)


class DatabaseApiViewTestCase(APITestCase):

    def test_get_data_from_database(self):   
        data = {"id": 1, "name":"John" , "age":24}
        response = self.client.get("/dbList",data)
        self.assertEqual(response.status_code, 200)


class AuthenticatorTestCase(APITestCase):

    def setUp(self):
        self.user= User.objects.create_user("suesh","suesh@gmail.com","password")
        self.client=APIClient()
        self.api_url=reverse('api')
        self.count_url=reverse('count')
        self.dbList_url=reverse('dbList')
        self.token_obtained_url=reverse('token_obtain_pair')

    def test_token_obtained_returns_jwt(self):
        credentials = {
            'username':'suesh',
            'password':'password',
        }
        response = self.client.post(self.token_obtained_url, credentials)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('access' in response.json().keys())
        self.assertTrue('refresh' in response.json().keys())


        

    

        

