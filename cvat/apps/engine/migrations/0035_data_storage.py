# Generated by Django 3.1.1 on 2020-12-02 06:47

import cvat.apps.engine.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0034_auto_20201125_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='storage',
            field=models.CharField(choices=[('local', 'LOCAL'), ('share', 'SHARE')], default=cvat.apps.engine.models.StorageChoice['LOCAL'], max_length=15),
        ),
    ]