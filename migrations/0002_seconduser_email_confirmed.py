# Generated by Django 2.0.5 on 2018-05-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_seconduser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seconduser',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]