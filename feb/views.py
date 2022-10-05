from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def Feb(request):
    judul = ["Program Sarjana Managemen", "Program Sarjana Akuntansi", "Program Sarjana Ilmu Ekonomi Pembangunan", "Program Sarjana Ekonomi Syariah", "Program Diploma III Akuntansi", "Program Diploma III Marketing", "Program Diploma III Perpajakan", "Program Diiploma III Keuangan Perbankan"]

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()


    konteks = {
        'jdl': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'feb.html', konteks)
    