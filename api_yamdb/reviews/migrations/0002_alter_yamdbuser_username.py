# Generated by Django 3.2 on 2023-02-20 22:54

import django.core.validators
from django.db import migrations, models
import reviews.services


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yamdbuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[reviews.services.validate_name_me, django.core.validators.RegexValidator(message='Некорректный username.', regex='^[\\w.@+-]+\\z')], verbose_name='Имя пользователя'),
        ),
    ]