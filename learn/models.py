from django.db import models

# Create your models here.
class Blog(models.Model):

    class Meta:
        verbose_name = "MODELNAME"
        verbose_name_plural = "MODELNAMEs"

    def __str__(self):
        pass