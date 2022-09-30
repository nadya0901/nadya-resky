from django.shortcuts import render

# Create your views here.
def Fh(request):
    judul = ["Ilmu Hukum"]

    konteks = {
        'jdl': judul,
    }
    return render(request, 'fh.html', konteks)