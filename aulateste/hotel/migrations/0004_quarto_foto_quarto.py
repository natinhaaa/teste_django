# Generated by Django 5.0.5 on 2024-05-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_hotel_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarto',
            name='foto_quarto',
            field=models.ImageField(default=0, upload_to='Foto_Quarto/'),
            preserve_default=False,
        ),
    ]
