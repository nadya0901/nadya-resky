from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def Fh(request):
    judul = ["Ilmu Hukum"]

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()


    konteks = {
        'jdl': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fh.html', konteks)