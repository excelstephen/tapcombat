from django.db import models

# Create your models here.
class PlayerScore(models.Model):
    user_id = models.CharField(max_length=150)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user_id} - {self.score} points"