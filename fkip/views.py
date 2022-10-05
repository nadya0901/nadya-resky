from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff


# Create your views here.

def Fkip(request):
    judul = ["Jurusan Pendidikan Nonformal", "Jurusan Pendidikan Bahasa Indonesia", "Jurusan Pendidikan Bahasa Inggris", "Jurusan Pendidikan Biologi", "Jurusan Pendidikan Matematika", "Jurusan Pendidikan Guru Sekolah Dasar", "Jurusan Pendidikan Guru PAUD", "Jurusan Bimbingan dan Konseling", "Jurusan Pendidikan Fisika", "Jurusan Pendidikan Ilmu Pengetahuan Alam", "Jurusan Pendidikan Kimia", "Jurusan Pendidikan Khusus", "Jurusan Pendidikan Pancasila dan Kewarganegaraan", "Jurusan Pendidikan Sejarah", "Jurusan Pendidikan Seni dan Pertunjukan", "Jurusan Pendidikan Sosiologi", "Jurusan Pendidikan Vokasional Teknik Elektro", "Jurusan Pendidikan Vokasional Teknik Mesin"]

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'jdl': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,

    }

    return render(request, 'fkip.html', konteks)