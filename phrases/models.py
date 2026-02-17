from django.db import models


class Phrase(models.Model):
    text = models.CharField(max_length=255)
    translation = models.CharField(max_length=255, blank=True)
    is_fake = models.BooleanField(default=False)

    def __str__(self):
        return self.text
