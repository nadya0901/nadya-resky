from django.shortcuts import render

# Create your views here.
def Fk(request) :
    judul = ["Prodi Kedokteran", "Prodi Keperawatan S1", "Prodi Keperawatan D3", "Prodi S1 Gizi", "Prodi Ilmu Keolahragaan"]

    konteks = {
        'jdl': judul,
    }
    return render(request, 'fk.html', konteks)