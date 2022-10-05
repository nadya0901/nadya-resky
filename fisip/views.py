from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def Fisip(request):
    judul = ["Program Studi Administrasi Publik", "Program Studi Ilmu Komunikasi", "Program Studi Ilmu Pemerintahan"]

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'jdl': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fisip.html', konteks)