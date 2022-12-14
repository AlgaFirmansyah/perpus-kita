# Generated by Django 3.0.5 on 2022-07-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0006_auto_20220723_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahasiswa',
            name='alamat',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='no_hp',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='no_ktp',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buku',
            name='kategori',
            field=models.CharField(choices=[('Edukasi', 'Edukasi'), ('entertainment', 'Entertainment'), ('Komik', 'Komik'), ('Biografi', 'Biografi'), ('Sejarah', 'Sejarah'), ('Novel', 'Novel'), ('scifi', 'Sci-Fi')], max_length=255),
        ),
        migrations.AlterField(
            model_name='buku',
            name='penerbit',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='buku',
            name='sinopsis',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='buku',
            name='tahunterbit',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='jurusan',
            field=models.CharField(choices=[('Teknik Informatika', 'Teknik Informatika'), ('Sistem Informasi', 'Sistem Informasi'), ('Keperawatan', 'Keperawatan'), ('Pertanian', 'Pertanian')], max_length=255),
        ),
    ]
