# Generated by Django 2.0.6 on 2018-08-12 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swimmer',
            name='numbervalue',
        ),
        migrations.RemoveField(
            model_name='swimmer',
            name='stringvalue',
        ),
        migrations.AddField(
            model_name='swimmer',
            name='graduation_year',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumni',
            name='graduated',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='alumni', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='swimmer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='swimmer', to=settings.AUTH_USER_MODEL),
        ),
    ]