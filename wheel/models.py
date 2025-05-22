from django.db import models
from django.contrib.auth.models import User

class Wheel(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WheelItem(models.Model):
    wheel = models.ForeignKey(Wheel, related_name='items', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    weight = models.IntegerField(default=1)
    color = models.CharField(max_length=7, default='#FF0000')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text