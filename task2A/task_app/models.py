from django.db import models
class UserProfile(models.Model):
    f_name = models.CharField(max_length=20, blank=True)
    l_name = models.CharField(max_length=20, blank=True)
    ph_no = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.f_name + ' ' + self.l_name
# Create your models here.
