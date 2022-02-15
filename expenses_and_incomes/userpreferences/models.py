from django.contrib.auth.models import User
from django.db import models


class UserPreference(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=250, blank=True, null=True)


    def __str__(self):
        return f'{str(self.user)}s preferences'
