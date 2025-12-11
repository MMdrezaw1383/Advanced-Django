import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from datetime import datetime
from accounts.models import User,Profile
from ..models import Category
@pytest.fixture
def api_client():
    client = APIClient()
    return client    

@pytest.fixture
def common_user():
    user = User.objects.create_user(email="common@fixture.com",password="@/1234567",is_verified=True)
    return user

@pytest.fixture
def common_category():
    category = Category.objects.create(name="testcategory")
    return category
    
    
    
@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self,api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200
        
        
    def test_create_post_response_401_status(self,api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title":'test',
            "content":'description',
            "status":True,
            "published_date": datetime.now(),
            
        }
        
        response = api_client.post(url,data)
        assert response.status_code == 401
        
        
    def test_create_post_response_201_status(self,api_client,common_user,common_category):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title":'test',
            "content":'description',
            "status":True,
            "category":common_category,
            "published_date": datetime.now(),
            
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url,data,)
        print("RESPONSE DATA:", response.data)
        assert response.status_code == 201
        
        
    def test_create_post_response_invalid_400_status(self,api_client,common_user,):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title":'test',
            "content":'description',
            "status":True,  
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url,data,)
        print("RESPONSE DATA:", response.data)
        assert response.status_code == 400