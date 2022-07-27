from asyncio.windows_events import NULL
from distutils.command.upload import upload
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from datetime import datetime,timedelta

# Create your models here.
class buku(models.Model):
    kat = [
        ('Edukasi', 'Edukasi'),
        ('entertainment', 'Entertainment'),
        ('Komik', 'Komik'),
        ('Biografi', 'Biografi'),
        ('Sejarah', 'Sejarah'),
        ('Novel', 'Novel'),
        ('scifi','Sci-Fi')
        ]
    idbuku = models.CharField(max_length=255, primary_key=True)
    judul = models.CharField(max_length=255)
    pengarang = models.CharField(max_length=255)
    kategori = models.CharField(max_length = 255, choices = kat )
    sinopsis = models.CharField(max_length=255)
    tahunterbit = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='media/', max_length=255, null = True, blank = True)       
    def __str__(self):
        return "{} - {} ".format(self.idbuku, self.judul, self.pengarang)
        return self.idbuku
    class Meta:
        db_table = "myapp_image"

class mahasiswa(models.Model):
    jur = [
        ('Teknik Informatika', 'Teknik Informatika'),
        ('Sistem Informasi', 'Sistem Informasi'),
        ('Keperawatan', 'Keperawatan'),
        ('Pertanian', 'Pertanian'),
    ]
    npm = models.CharField(max_length=255, primary_key=True)
    nama = models.CharField(max_length=255 )
    jurusan = models.CharField(max_length=255, choices= jur)
    no_hp = models.CharField(max_length=255 )
    no_ktp = models.CharField(max_length=255)
    alamat = models.CharField(max_length = 255)
    foto = models.ImageField(upload_to='media/' , max_length=255, blank=True, null=True)
    def __str__(self) -> str:
        return "{} - {}".format(self.npm, self.nama, self.jurusan)

def balik():
    return datetime.today() + timedelta(days=14)
class pinjam(models.Model):
    idpinjam = models.AutoField( primary_key=True)
    npm = models.ForeignKey(mahasiswa, on_delete= models.CASCADE)
    idbuku = models.ForeignKey(buku, on_delete= models.CASCADE)
    tanggal = models.DateField(auto_now_add=True)
    kembali = models.DateField(default = balik)

    def __str__(self) -> str:
        return "{} - {} -{} - {}".format(self.idpinjam, self.tanggal, self.idbuku, self.npm)