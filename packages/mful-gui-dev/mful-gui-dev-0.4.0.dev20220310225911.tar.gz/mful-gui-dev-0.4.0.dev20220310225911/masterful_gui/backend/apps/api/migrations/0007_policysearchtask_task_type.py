# Generated by Django 3.2.8 on 2022-02-24 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220214_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='policysearchtask',
            name='task_type',
            field=models.CharField(default='COMPUTER_VISION_TASK_UNKNOWN', max_length=250),
        ),
    ]
