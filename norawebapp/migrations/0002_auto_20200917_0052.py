# Generated by Django 3.1.1 on 2020-09-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norawebapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
