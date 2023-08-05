# Generated by Django 3.2 on 2021-08-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PolicySearchTask',
            fields=[
                ('policy_name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('approach_name', models.CharField(max_length=120)),
                ('customer_model_metrics', models.JSONField(default=dict)),
                ('node_search_tasks', models.JSONField(default=dict)),
            ],
        ),
    ]
