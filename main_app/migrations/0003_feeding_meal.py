# Generated by Django 3.1.3 on 2020-11-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='meal',
            field=models.CharField(default='B', max_length=1),
            preserve_default=False,
        ),
    ]
