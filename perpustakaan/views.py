
from xml.etree.ElementInclude import include
from django.shortcuts import render, redirect
from .forms import Form_buku, Form_pinjam, Form_user, form_mhs, form_mhs
from perpustakaan.models import buku ,mahasiswa , pinjam
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import  Group
import perpustakaan

# Create your views here.

#dashboard_
def index(request):
    testgrup = Group.objects.get(name='super admin')
    gr = request.user.groups.all()
    grp = None
    if testgrup in gr:
        grp = "Super Admin"
        navbar = "perpustakaan/navbaradmin.html"
    else: 
        grp = " Operator"
        navbar = "perpustakaan/navbar.html"
    return render(request,'perpustakaan/index.html', {'grp':grp , 'navbar':navbar} )

#daftarbuku
def daftarbuku(request):
    bk = buku.objects.all()
    context ={
        
        'daftar_buku': bk,
    }
    return render(request, 'perpustakaan/daftarbk.html' ,context)

#Daftar mahasiswa
def daftarmhs(request):
    mhs = mahasiswa.objects.all()
    context ={
        
        'data': mhs,
    }
    return render(request, 'perpustakaan/daftarmahasiswa.html' ,context)

#daftar pinjaman buku
def daftarpinjam(request):
    list_pinjam = pinjam.objects.all()

    context = {
       'pinjam' : list_pinjam,
    }
    return render(request, 'perpustakaan/daftarpinjam.html', context)

#form pengisian mahasiswa
def form_mahasiswa(request):
    mahasiswa_form = form_mhs(request.POST or None)
    if request.method == 'POST':
        mahasiswa_form = form_mhs(request.POST, request.FILES)
        if mahasiswa_form.is_valid():
            mahasiswa_form.save()
            img = mahasiswa_form.instance
            messages.success(request, "Mahasiswa Berhasil Di tambahkan", {'img': img})
            
            return redirect ('/form_mhs')
        else:
            messages.error(request, "Gagal Menambahkan Mahasiswa")
    context = {

        'form': mahasiswa_form,
    }

    return render(request, 'perpustakaan/mhsform.html', context)

#form pengisisan buku
def formbuku (request):
    formbk = Form_buku(request.POST or None)
    if request.method == 'POST':
        formbk = Form_buku(request.POST, request.FILES)
        if formbk.is_valid():
            formbk.save()
            img_obj = formbk.instance
            messages.success(request, "Buku Berhasil Di tambahkan")
            return redirect('/formbuku', {'omg_obj' : img_obj})
        else:
            messages.error(request, "Gagal Menambahkan Buku")
    context = {
        'buku': formbk,
    }
    return render(request, 'perpustakaan/formbuku.html' , context)
    
def formpinjam (request):
    formpj = Form_pinjam(request.POST or None)
    if request.method == 'POST':
        if formpj.is_valid():
            formpj.save()
            messages.success(request, "Pinjaman Berhasil Di tambahkan")
            return redirect('/formpinjam')
        else:
            messages.error(request, "Gagal menambahkan Pinjaman")
            return redirect('/formpinjam')
    context = {
        'pinjam': formpj,
    }
    return render(request, 'perpustakaan/formpinjam.html' , context)

def hapusbuku(request,idbuku):
    delbuku = buku.objects.get(idbuku = idbuku)
    delbuku.delete()
    return redirect('/list_buku')

def hapuspinjam(request,idpinjam):
    delpinjam = pinjam.objects.get(idpinjam = idpinjam)
    delpinjam.delete()
    return redirect('/list_pinjaman')

def hapusmhs(request,npm):
    delmhs = mahasiswa.objects.get(npm = npm)
    delmhs.delete()
    return redirect('/list_mahasiswa')
    
def login_user(request):
    context = {
        
    }
    if request.method == 'POST':
        userna = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=userna, password=password)
        context = {
            "login": user
        }
        if user is not None:
            login(request, user)
            return redirect('/perpuskita')

        else : 
            messages.error(request, 'username atau password yang anda masukkan salah')          
            return redirect('/')

    return render(request, 'perpustakaan/login.html')

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')

    return render(request ,'perpustakaan/logout.html')

def editmhs(request, npm):
    editmaha = mahasiswa.objects.get(npm = npm)
    context = {'editmhs': editmaha}
    updatemhs = form_mhs(request.POST, instance=editmaha)
    if updatemhs.is_valid():
        updatemhs.save()
        messages.success(request, 'update mahasiswa berhasil')

    return render(request ,'perpustakaan/editmhs.html', context)

def editbuku(request, idbuku):
    editbk = buku.objects.get(idbuku = idbuku)
    context = {'editbuku': editbk}
    updatebk = Form_buku(request.POST, instance=editbk)
    if updatebk.is_valid():
        updatebk.save()
        messages.success(request, 'update Buku berhasil')

    return render(request ,'perpustakaan/editbuku.html', context)

def lihatbuku(request,idbuku):
    lihatbk = buku.objects.get(idbuku=idbuku)
    context = {'lihatbuku': lihatbk}

    return render(request, 'perpustakaan/lihatbuku.html', context)

def lihatmahasiswa(request,npm):
    lihatmhs = mahasiswa.objects.get(npm = npm)
    img_obj = request
    context = {'lihatmhs': lihatmhs}
    return render(request, 'perpustakaan/lihatmhs.html', context)

def form_user_sss(request):
    formuser = Form_user(request.POST or None)
    if request.method == 'POST':
        formuser = Form_user(request.POST)
        if formuser.is_valid():
            formuser.save()
            messages.success(request, "Berhasil menambahkan")
            return redirect('/formbuku')
        else:
            messages.error(request, "Gagal Menambahkan")
    context = {
        'user': formuser,
    }
    return render(request, 'perpustakaan/formuser.html' , context)