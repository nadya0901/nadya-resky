from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def Faperta(request):
    judul = ["Program Studi Agribisnis", "Program Studi Agroekoteknologi", "Program Studi Ilmu Perikanan", "Program Studi Teknologi Pangan"]

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'jdl': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request,'faperta.html', konteks)