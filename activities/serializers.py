from rest_framework import serializers
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


class FileUploadBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'user', 'file', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

class ReadingCultureSerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = ReadingCulture

class FiveInitiativesParticipationSerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = FiveInitiativesParticipation

class AcademicPerformanceSerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = AcademicPerformance

class DisciplineAndEthicsSerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = DisciplineAndEthics

class CompetitionAchievementsSerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = CompetitionAchievements

class AttendanceSerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = Attendance

class EnlightenmentLessonsParticipationSerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = EnlightenmentLessonsParticipation

class VolunteeringAndCommunityWorkSerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = VolunteeringAndCommunityWork

class CulturalVisitsSerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = CulturalVisits

class SportsAndHealthyLifestyleSerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = SportsAndHealthyLifestyle

class SpiritualAndEducationalActivitySerializer(FileUploadBaseSerializer):
    class Meta(FileUploadBaseSerializer.Meta):
        model = SpiritualAndEducationalActivity

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
