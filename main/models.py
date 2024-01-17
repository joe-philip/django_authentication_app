from django.db import models


# Create your models here.
class Countries(models.Model):
    name = models.CharField(max_length=50)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)

    class Meta:
        db_table = 'country'
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class Nationalities(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Countries, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = 'nationalities'
        verbose_name = 'Nationality'
        verbose_name_plural = 'Nationalities'
