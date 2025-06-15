from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Har bir user uchun bitta profil
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)  # Profil rasmi
    phone = models.CharField(max_length=20, blank=True)  # Telefon raqami
    address = models.CharField(max_length=255, blank=True)  # Manzil
    birth_date = models.DateField(blank=True, null=True)  # Tug‘ilgan sana
    bio = models.TextField(blank=True)  # O‘zi haqida qisqacha

    class Meta:
        verbose_name = 'Profile'
        ordering = ['user__username']

    def __str__(self):
        return f" {self.user.username} profili"
