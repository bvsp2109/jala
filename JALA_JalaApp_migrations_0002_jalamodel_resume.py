# Generated by Django 2.2.4 on 2019-09-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JalaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jalamodel',
            name='Resume',
            field=models.FileField(blank='True', null='True', upload_to=''),
            preserve_default='True',
        ),
    ]
