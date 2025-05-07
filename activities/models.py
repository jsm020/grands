
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import os

def validate_file_extension_and_size(value):
    allowed_extensions = ['.pdf', '.doc', '.docx', '.png', '.jpeg', '.jpg']
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in allowed_extensions:
        raise ValidationError(f"Fayl formati noto'g'ri. Ruxsat etilgan formatlar: {', '.join(allowed_extensions)}.")
    max_size = 30 * 1024 * 1024  # 30 MB
    if value.size > max_size:
        raise ValidationError("Fayl hajmi 30 MB dan oshmasligi kerak.")

User = get_user_model()

class BaseActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to='activities/',
        validators=[validate_file_extension_and_size],
        help_text="Ruxsat etilgan formatlar: .pdf, .doc, .docx, .png, .jpeg, .jpg. Maksimal hajm: 30 MB."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

# 1. Kitobxonlik madaniyati
class ReadingCulture(BaseActivity):
    class Meta:
        verbose_name = "Kitobxonlik madaniyati"
        verbose_name_plural = "Kitobxonlik madaniyati"

# 2. “5 muhim tashabbus” doirasidagi to‘garaklarga faol ishtirok
class FiveInitiativesParticipation(BaseActivity):
    class Meta:
        verbose_name = "5 muhim tashabbus doirasidagi to‘garaklarga faol ishtirok"
        verbose_name_plural = "5 muhim tashabbus doirasidagi to‘garaklarga faol ishtirok"

# 3. Talabaning akademik o‘zlashtirishi
class AcademicPerformance(BaseActivity):
    class Meta:
        verbose_name = "Talabaning akademik o‘zlashtirishi"
        verbose_name_plural = "Talabaning akademik o‘zlashtirishi"

# 4. Talabaning oliy ta’lim tashkilotining ichki tartib qoidalari va Odob-axloq kodeksiga rioya etishi
class DisciplineAndEthics(BaseActivity):
    class Meta:
        verbose_name = "Ichki tartib va odob-axloq kodeksiga rioya etish"
        verbose_name_plural = "Ichki tartib va odob-axloq kodeksiga rioya etish"

# 5. Xalqaro, respublika, viloyat miqyosidagi ko‘rik-tanlov, fan olimpiadalari va sport musobaqalarida erishilgan natijalar
class CompetitionAchievements(BaseActivity):
    class Meta:
        verbose_name = "Ko‘rik-tanlov va musobaqalardagi natijalar"
        verbose_name_plural = "Ko‘rik-tanlov va musobaqalardagi natijalar"

# 6. Talabaning darslarga to‘liq va kechikmasdan kelishi
class Attendance(BaseActivity):
    class Meta:
        verbose_name = "Darslarga to‘liq va kechikmasdan kelish"
        verbose_name_plural = "Darslarga to‘liq va kechikmasdan kelish"

# 7. Talabaning “Ma’rifat darslari”dagi faol ishtiroki
class EnlightenmentLessonsParticipation(BaseActivity):
    class Meta:
        verbose_name = "Ma’rifat darslaridagi faol ishtirok"
        verbose_name_plural = "Ma’rifat darslaridagi faol ishtirok"

# 8. Volontyorlik va jamoat ishlaridagi faolligi
class VolunteeringAndCommunityWork(BaseActivity):
    class Meta:
        verbose_name = "Volontyorlik va jamoat ishlaridagi faollik"
        verbose_name_plural = "Volontyorlik va jamoat ishlaridagi faollik"

# 9. Teatr va muzey, jahon, kino, tarixiy qadamjolarga tashriflar
class CulturalVisits(BaseActivity):
    class Meta:
        verbose_name = "Teatr, muzey va tarixiy qadamjolarga tashriflar"
        verbose_name_plural = "Teatr, muzey va tarixiy qadamjolarga tashriflar"

# 10. Talabalar sport bilan shug‘ullanishi va sog‘lom turmush tarziga amal qilishi
class SportsAndHealthyLifestyle(BaseActivity):
    class Meta:
        verbose_name = "Sport va sog‘lom turmush tarzi"
        verbose_name_plural = "Sport va sog‘lom turmush tarzi"

# 11. Ma’naviy-ma’rifiy sohalardagi faollik
class SpiritualAndEducationalActivity(BaseActivity):
    class Meta:
        verbose_name = "Ma’naviy-ma’rifiy sohalardagi faollik"
        verbose_name_plural = "Ma’naviy-ma’rifiy sohalardagi faollik"


# Model for storing user tokens from external authentication
class ExternalAuthToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='external_auth_token')
    token = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} token"
