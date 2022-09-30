from django.shortcuts import render

# Create your views here.
def Ft(request):
    judul = ["Jurusan Teknik Elektro", "Jurusan Teknik Industri", "Jurusan Teknik Sipil", "Jurusan Teknik", "Jurusan Teknik Kimia", "Jurusan teknik Metalurgi", "Jurusan Teknik Mesin"]

    konteks = {
        'jdl': judul,
    }

    return render(request, 'ft.html', konteks)