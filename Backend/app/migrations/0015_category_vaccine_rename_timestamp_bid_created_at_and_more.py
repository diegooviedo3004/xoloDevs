# Generated by Django 5.1.2 on 2024-11-11 16:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_post_phone_number_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='post',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='post',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
        migrations.AddField(
            model_name='bid',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('Auction', 'Subasta'), ('Post', 'Anuncio')], default='Post', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='postimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postimage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='breed',
            field=models.CharField(choices=[('Angus', 'Angus'), ('Holstein', 'Holstein'), ('Charolais', 'Charolais'), ('Brahman', 'Brahman'), ('Limousin', 'Limousin'), ('Simmental', 'Simmental'), ('Hereford', 'Hereford'), ('Pardo suizo', 'Pardo Suizo'), ('Santa gertrudis', 'Santa Gertrudis'), ('Gyr', 'Gyr'), ('Girolando', 'Girolando'), ('Others', 'Otros')], default='Others', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='lat',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='long',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='app.post')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='app.auction'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(choices=[('A', 'Plan A'), ('B', 'Plan B'), ('C', 'Plan C')], max_length=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stripe_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='app.post')),
            ],
        ),
        migrations.CreateModel(
            name='Traceability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chapa_code', models.CharField(max_length=20)),
                ('record', models.ImageField(blank=True, null=True, upload_to='record/')),
                ('breed_M', models.CharField(blank=True, choices=[('Angus', 'Angus'), ('Holstein', 'Holstein'), ('Charolais', 'Charolais'), ('Brahman', 'Brahman'), ('Limousin', 'Limousin'), ('Simmental', 'Simmental'), ('Hereford', 'Hereford'), ('Pardo suizo', 'Pardo Suizo'), ('Santa gertrudis', 'Santa Gertrudis'), ('Gyr', 'Gyr'), ('Girolando', 'Girolando'), ('Others', 'Otros')], default='Others', max_length=20, null=True)),
                ('breed_P', models.CharField(blank=True, choices=[('Angus', 'Angus'), ('Holstein', 'Holstein'), ('Charolais', 'Charolais'), ('Brahman', 'Brahman'), ('Limousin', 'Limousin'), ('Simmental', 'Simmental'), ('Hereford', 'Hereford'), ('Pardo suizo', 'Pardo Suizo'), ('Santa gertrudis', 'Santa Gertrudis'), ('Gyr', 'Gyr'), ('Girolando', 'Girolando'), ('Others', 'Otros')], default='Others', max_length=20, null=True)),
                ('health_status', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('category', models.ManyToManyField(blank=True, to='app.category')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='traceabilities', to='app.post')),
                ('vaccines', models.ManyToManyField(blank=True, to='app.vaccine')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReproductiveData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('last_calving', models.DateField(blank=True, null=True)),
                ('beeding_date', models.DateField(blank=True, null=True)),
                ('last_heat_date', models.DateField(blank=True, null=True)),
                ('days_pregnant', models.IntegerField(blank=True, default=0, null=True)),
                ('expected_calving_date', models.DateField(blank=True, null=True)),
                ('milk_production_in_liters', models.IntegerField(blank=True, default=0, null=True)),
                ('traceability', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.traceability')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DairyCowData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('daily_milk_production_in_liters', models.IntegerField(blank=True, default=0, null=True)),
                ('days_in_milk', models.IntegerField(blank=True, default=0, null=True)),
                ('traceability', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.traceability')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]