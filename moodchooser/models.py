from django.db import models

# Create your models here.


class MoodEntry(models.Model):
    mood = models.CharField(max_length=1)
    date = models.DateField(auto_now_add=False)
    
    def __str__(self):
        return "mood " + self.date.isoformat()[0:10]