from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status


class SupportTestCase(APITestCase):

    def setUp(self):
        self.create_users()
        url = '/api/v1/token/'
        data = {"username": "testuser", "password": "usertest123"}
        response = self.client.post(url, data, format='json')
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        pass

    def tearDown(self):
        pass

    def create_users(self):
        test_user = get_user_model()
        test_user.objects.create_user(username='testuser', password='usertest123').save()

    def test_get_jwt_token(self):
        url = '/api/v1/token/'
        data = {"username": "testuser", "password": "usertest123"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ticket_creation_failed(self):
        url = '/api/v1/support/ticket/'
        data = {'header': 'Problem 1', 'description': 'description1', 'status': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


