# Generated by Django 2.0.13 on 2019-02-15 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190214_1133'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostUser',
        ),
    ]