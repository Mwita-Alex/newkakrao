# Generated by Django 4.0 on 2021-12-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='image',
            field=models.ImageField(null=True, upload_to='pages/images/'),
        ),
        migrations.AddField(
            model_name='registration',
            name='pdf',
            field=models.FileField(null=True, upload_to='pages/pdfs/'),
        ),
    ]
