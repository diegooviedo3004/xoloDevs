# Generated by Django 5.1.2 on 2024-10-22 07:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_user_phone_numbers_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='CowBreed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('age', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CowImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='images/vendetuvaca/cows/')),
                ('cow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.cow')),
            ],
        ),
        migrations.CreateModel(
            name='CowLifeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('vaccinated', models.BooleanField(default=False)),
                ('for_sale', models.BooleanField(default=False)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('last_parturition_date', models.DateField(blank=True, null=True)),
                ('expected_parturition_date', models.DateField(blank=True, null=True)),
                ('last_heat_date', models.DateField(blank=True, null=True)),
                ('pregnancy_date', models.DateField(blank=True, null=True)),
                ('days_of_pregnancy', models.IntegerField(blank=True, null=True)),
                ('milk_production', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('days_of_lactation', models.IntegerField(blank=True, null=True)),
                ('milk_control', models.BooleanField(default=False)),
                ('brucellosis_application', models.BooleanField(default=False)),
                ('father', models.CharField(blank=True, max_length=50, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('cow', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='life_record', to='app.cow')),
                ('mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calves', to='app.cow')),
            ],
        ),
        migrations.CreateModel(
            name='CowBreedDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait', models.CharField(blank=True, max_length=10, null=True)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cowbreed')),
                ('life_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breeds', to='app.cowliferecord')),
            ],
        ),
    ]
