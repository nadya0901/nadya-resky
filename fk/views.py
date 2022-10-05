from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def Fk(request) :
    judul = ["Prodi Kedokteran", "Prodi Keperawatan S1", "Prodi Keperawatan D3", "Prodi S1 Gizi", "Prodi Ilmu Keolahragaan"]

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()


    konteks = {
        'jdl': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fk.html', konteks)