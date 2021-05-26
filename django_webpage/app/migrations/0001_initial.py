# Generated by Django 3.2 on 2021-04-22 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continents',
            fields=[
                ('continent_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'continents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('national_day', models.DateField(blank=True, null=True)),
                ('country_code2', models.CharField(max_length=2, unique=True)),
                ('country_code3', models.CharField(max_length=3, unique=True)),
            ],
            options={
                'db_table': 'countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('guest_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'guests',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'languages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegionAreas',
            fields=[
                ('region_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('region_area', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'db_table': 'region_areas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'regions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vips',
            fields=[
                ('vip_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vips',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CountryLanguages',
            fields=[
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.countries')),
                ('official', models.IntegerField()),
            ],
            options={
                'db_table': 'country_languages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CountryStats',
            fields=[
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.countries')),
                ('year', models.IntegerField()),
                ('population', models.IntegerField(blank=True, null=True)),
                ('gdp', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
            ],
            options={
                'db_table': 'country_stats',
                'managed': False,
            },
        ),
    ]
