# Generated by Django 3.1.6 on 2021-02-02 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendfiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='user',
        ),
    ]