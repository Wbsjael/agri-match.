# Generated by Django 4.2.16 on 2024-12-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri_match_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatorlisting',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='operatorlisting',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
