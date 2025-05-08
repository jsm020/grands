from rest_framework import viewsets, permissions

from .models import (
    ReadingCulture,
    FiveInitiativesParticipation,
    AcademicPerformance,
    DisciplineAndEthics,
    CompetitionAchievements,
    Attendance,
    EnlightenmentLessonsParticipation,
    VolunteeringAndCommunityWork,
    CulturalVisits,
    SportsAndHealthyLifestyle,
    SpiritualAndEducationalActivity,
)
from .serializers import (
    ReadingCultureSerializer,
    FiveInitiativesParticipationSerializer,
    AcademicPerformanceSerializer,
    DisciplineAndEthicsSerializer,
    CompetitionAchievementsSerializer,
    AttendanceSerializer,
    EnlightenmentLessonsParticipationSerializer,
    VolunteeringAndCommunityWorkSerializer,
    CulturalVisitsSerializer,
    SportsAndHealthyLifestyleSerializer,
    SpiritualAndEducationalActivitySerializer,
)

# Generic file upload viewset
class FileUploadViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReadingCultureViewSet(FileUploadViewSet):
    queryset = ReadingCulture.objects.all()
    serializer_class = ReadingCultureSerializer

class FiveInitiativesParticipationViewSet(FileUploadViewSet):
    queryset = FiveInitiativesParticipation.objects.all()
    serializer_class = FiveInitiativesParticipationSerializer

class AcademicPerformanceViewSet(FileUploadViewSet):
    queryset = AcademicPerformance.objects.all()
    serializer_class = AcademicPerformanceSerializer

class DisciplineAndEthicsViewSet(FileUploadViewSet):
    queryset = DisciplineAndEthics.objects.all()
    serializer_class = DisciplineAndEthicsSerializer

class CompetitionAchievementsViewSet(FileUploadViewSet):
    queryset = CompetitionAchievements.objects.all()
    serializer_class = CompetitionAchievementsSerializer

class AttendanceViewSet(FileUploadViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class EnlightenmentLessonsParticipationViewSet(FileUploadViewSet):
    queryset = EnlightenmentLessonsParticipation.objects.all()
    serializer_class = EnlightenmentLessonsParticipationSerializer

class VolunteeringAndCommunityWorkViewSet(FileUploadViewSet):
    queryset = VolunteeringAndCommunityWork.objects.all()
    serializer_class = VolunteeringAndCommunityWorkSerializer

class CulturalVisitsViewSet(FileUploadViewSet):
    queryset = CulturalVisits.objects.all()
    serializer_class = CulturalVisitsSerializer

class SportsAndHealthyLifestyleViewSet(FileUploadViewSet):
    queryset = SportsAndHealthyLifestyle.objects.all()
    serializer_class = SportsAndHealthyLifestyleSerializer

class SpiritualAndEducationalActivityViewSet(FileUploadViewSet):
    queryset = SpiritualAndEducationalActivity.objects.all()
    serializer_class = SpiritualAndEducationalActivitySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import ExternalAuthToken, ReadingCulture
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

        # --- Yangi: Profil ma'lumotlarini olish va saqlash ---
        me_url = 'https://student.samdukf.uz/rest/v1/account/me'
        me_headers = {'Authorization': f'Bearer {token}'}
        try:
            me_resp = requests.get(me_url, headers=me_headers, timeout=10)
            print(f"GET {me_url} status: {me_resp.status_code}")
            print(f"GET {me_url} body: {me_resp.text}")
        except Exception as e:
            print(f"Exception (me): {e}")
            return Response({'error': 'Profil maʼlumotlarini olishda xatolik.'}, status=status.HTTP_502_BAD_GATEWAY)

        if me_resp.status_code == 200:
            me_data = me_resp.json().get('data', {})
            from datetime import datetime
            birth_date = None
            if me_data.get('birth_date'):
                try:
                    birth_date = datetime.utcfromtimestamp(int(me_data['birth_date'])).date()
                except Exception:
                    birth_date = None
            group_name = ''
            if isinstance(me_data.get('group'), dict):
                group_name = me_data['group'].get('name', '')
            from .models import UserProfile
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    'first_name': me_data.get('first_name', ''),
                    'second_name': me_data.get('second_name', ''),
                    'third_name': me_data.get('third_name', ''),
                    'full_name': me_data.get('full_name', ''),
                    'image': me_data.get('image', ''),
                    'birth_date': birth_date,
                    'passport_pin': me_data.get('passport_pin', ''),
                    'passport_number': me_data.get('passport_number', ''),
                    'university': me_data.get('university', ''),
                    'group_name': group_name,
                }
            )
        else:
            print('Profil maʼlumotlarini olishda xatolik:', me_resp.text)

        # --- Yangi: GPA olish va saqlash ---

        gpa_url = 'https://student.samdukf.uz/rest/v1/education/gpa-list'
        gpa_headers = {'Authorization': f'Bearer {token}'}
        gpa_score = None
        try:
            gpa_resp = requests.get(gpa_url, headers=gpa_headers, timeout=10)
            print(f"GET {gpa_url} status: {gpa_resp.status_code}")
            print(f"GET {gpa_url} body: {gpa_resp.text}")
            if gpa_resp.status_code == 200:
                gpa_data_list = gpa_resp.json().get('data', [])
                if isinstance(gpa_data_list, list) and len(gpa_data_list) > 0:
                    gpa_score = gpa_data_list[0].get('gpa')
                    try:
                        gpa_score = float(gpa_score)
                    except Exception:
                        gpa_score = None
        except Exception as e:
            print(f"Exception (gpa): {e}")
            gpa_score = None
        from .models import UserGPA
        UserGPA.objects.update_or_create(user=user, defaults={'gpa_score': gpa_score})

        return Response({'success': True, 'token': token})
    else:
        try:
            error_msg = resp.json().get('error', 'Login yoki parol xato.')
        except Exception:
            error_msg = 'Login yoki parol xato.'
        return Response({'error': error_msg}, status=status.HTTP_401_UNAUTHORIZED)

