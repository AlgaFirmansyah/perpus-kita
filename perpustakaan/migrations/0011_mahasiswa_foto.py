# Generated by Django 3.0.5 on 2022-07-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0010_auto_20220724_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahasiswa',
            name='foto',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media/'),
        ),
    ]
