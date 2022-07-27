from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from. import views

app_name = 'perpustakaan'

urlpatterns = [
    path('formuser', views.form_user_sss, name='formuser'),
    path('formpinjam/', views.formpinjam, name='formpinjam'),
    path('formbuku/', views.formbuku , name='formbuku'),
    path('list_pinjaman/', views.daftarpinjam , name='list_pinjam'),
    path('list_mahasiswa/', views.daftarmhs, name='list_mhs'),
    path('list_buku/', views.daftarbuku , name='list_buku'),
    path('form_mhs/', views.form_mahasiswa, name='formmhs'),
    path('hapusbuku/<str:idbuku>', views.hapusbuku , name='hapusbuku'),
    path('hapuspinjam/<str:idpinjam>', views.hapuspinjam , name='hapuspinjam'),
    path('hapusmhs/<str:npm>', views.hapusmhs , name='hapusmhs'),
    path('editmhs/<str:npm>', views.editmhs , name='editmhs'),
    path('editbuku/<str:idbuku>', views.editbuku , name='editbuku'),
    path('lihatbuku/<str:idbuku>', views.lihatbuku , name='lihatbuku'),
    path('lihatmhs/<str:npm>', views.lihatmahasiswa , name='lihatmhs'),
    path('logout/', views.logoutuser, name='logout'),
    path('', views.login_user, name='login'),
    path('perpuskita/',views.index, name='index'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)