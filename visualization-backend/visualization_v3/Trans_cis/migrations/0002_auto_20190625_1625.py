# Generated by Django 2.2 on 2019-06-25 16:25

import Trans_cis.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trans_cis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadmodel',
            name='file',
            field=models.FileField(upload_to=Trans_cis.models.Trans_save_path),
        ),
    ]
