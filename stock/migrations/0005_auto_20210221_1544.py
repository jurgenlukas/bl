# Generated by Django 3.1.6 on 2021-02-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20210220_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(null=True, upload_to='blog_images/'),
        ),
    ]
