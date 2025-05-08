from .models import UserProfile
from django.contrib import admin
admin.site.register(UserProfile)
from django.contrib import admin
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
    ExternalAuthToken,
)

admin.site.register(ReadingCulture)
admin.site.register(FiveInitiativesParticipation)
admin.site.register(AcademicPerformance)
admin.site.register(DisciplineAndEthics)
admin.site.register(CompetitionAchievements)
admin.site.register(Attendance)
admin.site.register(EnlightenmentLessonsParticipation)
admin.site.register(VolunteeringAndCommunityWork)
admin.site.register(CulturalVisits)
admin.site.register(SportsAndHealthyLifestyle)
admin.site.register(SpiritualAndEducationalActivity)
admin.site.register(ExternalAuthToken)
