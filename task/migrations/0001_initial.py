# Generated by Django 3.2.12 on 2022-12-29 09:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskData', models.CharField(max_length=200)),
                ('taskID', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
    ]
