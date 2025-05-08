from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    login_api,
    ReadingCultureViewSet,
    FiveInitiativesParticipationViewSet,
    AcademicPerformanceViewSet,
    DisciplineAndEthicsViewSet,
    CompetitionAchievementsViewSet,
    AttendanceViewSet,
    EnlightenmentLessonsParticipationViewSet,
    VolunteeringAndCommunityWorkViewSet,
    CulturalVisitsViewSet,
    SportsAndHealthyLifestyleViewSet,
    SpiritualAndEducationalActivityViewSet,
)
from django.urls import path, include

router = DefaultRouter()
router.register(r'reading-culture', ReadingCultureViewSet, basename='reading-culture')
router.register(r'five-initiatives', FiveInitiativesParticipationViewSet, basename='five-initiatives')
router.register(r'academic-performance', AcademicPerformanceViewSet, basename='academic-performance')
router.register(r'discipline-ethics', DisciplineAndEthicsViewSet, basename='discipline-ethics')
router.register(r'competition-achievements', CompetitionAchievementsViewSet, basename='competition-achievements')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'enlightenment-lessons', EnlightenmentLessonsParticipationViewSet, basename='enlightenment-lessons')
router.register(r'volunteering-community', VolunteeringAndCommunityWorkViewSet, basename='volunteering-community')
router.register(r'cultural-visits', CulturalVisitsViewSet, basename='cultural-visits')
router.register(r'sports-healthy-lifestyle', SportsAndHealthyLifestyleViewSet, basename='sports-healthy-lifestyle')
router.register(r'spiritual-educational', SpiritualAndEducationalActivityViewSet, basename='spiritual-educational')

urlpatterns = [
    path('login/', login_api, name='login_api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
