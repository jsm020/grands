from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import ExternalAuthToken
from .serializers import LoginSerializer
import requests
from drf_yasg import openapi

from drf_yasg.utils import swagger_auto_schema
import os

@swagger_auto_schema(
    method='post',
    request_body=LoginSerializer,
    responses={
        200: openapi.Response(
            description="Login muvaffaqiyatli",
            examples={
                "application/json": {"success": True, "token": "your_token_here"}
            }
        ),
        400: openapi.Response(
            description="Xatolik",
            examples={
                "application/json": {"error": "Username va password kiritilishi shart."}
            }
        ),
        401: openapi.Response(
            description="Login yoki parol xato.",
            examples={
                "application/json": {"error": "Login yoki parol xato."}
            }
        ),
    }
)
@api_view(['POST'])
def login_api(request):
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    url = 'https://student.samdukf.uz/rest/v1/auth/login'

    # Agar sizda shaxsiy token bo'lsa, uni headers ga qo'shamiz
    # Masalan:
    # personal_token = 'YOUR_PERSONAL_TOKEN_HERE'
    # headers = {'Authorization': f'Bearer {personal_token}'}
    # resp = requests.post(url, json={...}, headers=headers, timeout=10)

    # Token .env faylidan olinadi
    personal_token = os.environ.get('SAMDUKF_PERSONAL_TOKEN', '')
    headers = {'Authorization': f'Bearer {personal_token}'}

    # Debug uchun so'rov va javobni terminalga chiqaramiz
    print(f"POST {url}")
    print(f"Request body: {{'login': '{username}', 'password': '***'}}")
    print(f"Headers: {headers}")
    try:
        resp = requests.post(url, json={'login': username, 'password': password}, headers=headers, timeout=10)
        print(f"Response status: {resp.status_code}")
        print(f"Response body: {resp.text}")
    except Exception as e:
        print(f"Exception: {e}")
        return Response({'error': 'Tashqi server bilan bog‘lanib bo‘lmadi.'}, status=status.HTTP_502_BAD_GATEWAY)

    if resp.status_code == 200:
        resp_data = resp.json()
        token = resp_data.get('data').get('token')
        if not token:
            return Response({'error': 'Tashqi API token qaytarmadi.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        User = get_user_model()
        user, created = User.objects.get_or_create(username=username)
        ExternalAuthToken.objects.update_or_create(user=user, defaults={'token': token})
        return Response({'success': True, 'token': token})
    else:
        try:
            error_msg = resp.json().get('error', 'Login yoki parol xato.')
        except Exception:
            error_msg = 'Login yoki parol xato.'
        return Response({'error': error_msg}, status=status.HTTP_401_UNAUTHORIZED)

