import pytest

from django.urls import reverse

def test_health(client):
   url = reverse('health')
   response = client.get(url)
   assert response.status_code == 200