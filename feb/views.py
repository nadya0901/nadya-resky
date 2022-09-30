from django.shortcuts import render

# Create your views here.
def Feb(request):
    judul = ["Program Sarjana Managemen", "Program Sarjana Akuntansi", "Program Sarjana Ilmu Ekonomi Pembangunan", "Program Sarjana Ekonomi Syariah", "Program Diploma III Akuntansi", "Program Diploma III Marketing", "Program Diploma III Perpajakan", "Program Diiploma III Keuangan Perbankan"]

    konteks = {
        'jdl': judul,
    }
    return render(request, 'feb.html', konteks)
    