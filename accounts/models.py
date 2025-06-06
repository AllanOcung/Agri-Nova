from django.contrib.auth.models import User
from django.db import models

class FarmerProfile(models.Model):
    USER_ROLES = (
        ('farmer', 'Farmer'),
        ('agronomist', 'Agronomist'),
        ('extension officer', 'Extension Officer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='farmer')

    def __str__(self):
        return self.user.username

class Farm(models.Model):
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='farms')
    location = models.CharField(max_length=255)
    crops = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.location} ({self.farmer.user.username})"