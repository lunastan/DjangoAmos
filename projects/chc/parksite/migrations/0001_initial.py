# Generated by Django 3.1.3 on 2022-01-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaceImage',
            fields=[
                ('faceId', models.AutoField(primary_key=True, serialize=False)),
                ('faceImg', models.ImageField(upload_to='images/')),
            ],
        ),
    ]