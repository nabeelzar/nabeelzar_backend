# Generated by Django 4.1.1 on 2022-10-05 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_projectimages_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimages',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]
