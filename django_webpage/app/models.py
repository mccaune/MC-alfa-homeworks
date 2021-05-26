# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Continents(models.Model):
    continent_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'continents'


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    national_day = models.DateField(blank=True, null=True)
    country_code2 = models.CharField(unique=True, max_length=2)
    country_code3 = models.CharField(unique=True, max_length=3)
    region = models.ForeignKey('Regions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'countries'
    


class CountryStats(models.Model):
    country = models.OneToOneField(Countries, models.DO_NOTHING, primary_key=True,)
    year = models.IntegerField()
    population = models.IntegerField(blank=True, null=True)
    gdp = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'country_stats'
        unique_together = (('country', 'year'),)
        

class Regions(models.Model):
    region_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(Continents, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'regions'

    def __str__(self):
        return self.name
