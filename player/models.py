from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Player(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nickname = models.CharField(null=True, blank=True, max_length=255)
    password1 = models.CharField(null=False, blank=False, max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return f"{self.user.username}"