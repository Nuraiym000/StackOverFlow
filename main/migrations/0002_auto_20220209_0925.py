# Generated by Django 3.1 on 2022-02-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='image',
            field=models.ImageField(null=True, upload_to='reply_images'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
