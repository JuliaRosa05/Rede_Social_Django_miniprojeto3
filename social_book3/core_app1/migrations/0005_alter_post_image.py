# Generated by Django 3.2.6 on 2021-08-29 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app1', '0004_followerscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]