from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def Ft(request):
    judul = ["Jurusan Teknik Elektro", "Jurusan Teknik Industri", "Jurusan Teknik Sipil", "Jurusan Teknik", "Jurusan Teknik Kimia", "Jurusan teknik Metalurgi", "Jurusan Teknik Mesin"]

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()


    konteks = {
        'jdl': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }

    return render(request, 'ft.html', konteks)