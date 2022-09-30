from django.shortcuts import render

# Create your views here.
def Faperta(request):
    judul = ["Program Studi Agribisnis", "Program Studi Agroekoteknologi", "Program Studi Ilmu Perikanan", "Program Studi Teknologi Pangan"]

    konteks = {
        'jdl': judul,
    }
    return render(request,'faperta.html', konteks)