from django.db import models

# Create your models here.
class  Profil_Model(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    year = models.IntegerField()
    bio = models.TextField()
    address = models.TextField()
    image = models.ImageField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Profil_Model'

    def  __str__(self):
        return self.name
