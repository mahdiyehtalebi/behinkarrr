# Generated by Django 4.2.5 on 2023-09-30 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('create_at', models.DateTimeField(default=datetime.datetime(2023, 9, 29, 23, 31, 38, 178590))),
            ],
        ),
    ]