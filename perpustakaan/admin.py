from django.contrib import admin

# Register your models here.
from .models import buku, mahasiswa, pinjam

admin.site.register(buku)
admin.site.register(mahasiswa)
admin.site.register(pinjam)