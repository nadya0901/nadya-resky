from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def Pascasarjana(request):
    judul = ["Doktor Pendidikan", "Doktor Ilmu Akuntansi", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Teknologi Pendidikan", "Pendidikan Matematika"]

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'jdl': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'pascasarjana.html', konteks)