from dataclasses import fields
from pyexpat import model
from statistics import mode
from django import forms
from.models import buku, mahasiswa, pinjam
from django.contrib.auth.models import  Group, User

class form_mhs(forms.ModelForm):
    class Meta:
        model = mahasiswa
        fields = "__all__"
        
class Form_buku(forms.ModelForm):
    class Meta:
        model = buku
        fields = "__all__"

class Form_pinjam(forms.ModelForm):
    class Meta:
        model = pinjam
        fields = "__all__"
        
class Form_user(forms.ModelForm):
    class meta:
        model = User
        fields = "__all__"