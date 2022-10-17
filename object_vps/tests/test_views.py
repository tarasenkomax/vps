import json

from django.urls import reverse
from rest_framework import status
from django.test import TestCase, Client
from object_vps.models import VPS
from object_vps.serializers import VPSSerializer


class VPSListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        VPS.objects.create(cpu=1, ram='1 GB', hdd='512 GB')
        VPS.objects.create(cpu=2, ram='2 GB', hdd='512 GB')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/list_vps/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('vps_list'))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_validate_data(self):
        resp = self.client.get(reverse('vps_list'))
        contacts = VPS.objects.all()
        serializer = VPSSerializer(contacts, many=True)
        self.assertEqual(resp.data, serializer.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


class CreateVPSViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_data = {'cpu': 1, 'ram': '2 GB', 'hdd': '1 TB'}

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.post('/api/create_vps/', data=json.dumps(self.valid_data), content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_view_url_accessible_by_name(self):
        resp = self.client.post('/api/create_vps/', data=json.dumps(self.valid_data), content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)


class UpdateVPSViewTest(TestCase):
    def setUp(self):
        self.vps = VPS.objects.create(cpu=1, ram='2 GB', hdd='1 TB')
        self.new_status = {"status": "started"}

    def test_update_vps_status(self):
        url = reverse('vps_update', kwargs={'id': self.vps.id})
        response = self.client.put(url, format='json', data=self.new_status, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], self.new_status['status'])


class VPSDetailViewTest(TestCase):
    def setUp(self):
        self.vps = VPS.objects.create(cpu=1, ram='1 GB', hdd='512 GB')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get(reverse('vps_detail', kwargs={'id': self.vps.id}))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('vps_detail', kwargs={'id': self.vps.id}))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_invalid_id(self):
        resp = self.client.get(reverse('vps_detail', kwargs={'id': 'invalid_id'}))
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)
