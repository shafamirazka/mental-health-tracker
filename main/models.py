from django.db import models

# Create your models here.
class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
    

# models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
# MoodEntry adalah nama model yang kamu definisikan.
# mood, time, feelings, dan mood_intensity adalah atribut atau field pada model. Setiap field memiliki tipe data yang sesuai seperti CharField, DateField, IntegerField, dan TextField.
# Decorator @property digunakan untuk menambahkan atribut read-only yang tidak disimpan ke dalam basis data, namun merupakan hasil derivasi/perhitungan dari atribut lain. Dalam hal ini, fungsi is_mood_strong() yang diberikan decorator @property mengukur apakah mood pengguna pada saat itu tergolong "kuat" berdasarkan mood_intensity.