# Generated by Django 5.0.5 on 2024-05-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_quarto_nome_alter_quarto_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='logo',
        ),
        migrations.AddField(
            model_name='hotel',
            name='foto_hotel',
            field=models.ImageField(default=0, upload_to='Foto_Hotel/'),
            preserve_default=False,
        ),
    ]