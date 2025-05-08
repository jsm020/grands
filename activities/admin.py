from django.contrib import admin
from .models import (
    UserProfile,
    UserGPA,
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
    ExternalAuthToken,
)

for model in [
    UserProfile,
    UserGPA,
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
    ExternalAuthToken,
]:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


