from django.shortcuts import render

# Create your views here.
def Fisip(request):
    judul = ["Program Studi Administrasi Publik", "Program Studi Ilmu Komunikasi", "Program Studi Ilmu Pemerintahan"]

    konteks = {
        'jdl': judul,
    }
    return render(request, 'fisip.html', konteks)