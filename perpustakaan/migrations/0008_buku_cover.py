# Generated by Django 3.0.5 on 2022-07-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0007_auto_20220723_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='cover',
            field=models.ImageField(default=1, upload_to='static'),
            preserve_default=False,
        ),
    ]
