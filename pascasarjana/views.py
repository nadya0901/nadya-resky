from django.shortcuts import render

# Create your views here.
def Pascasarjana(request):
    judul = ["Doktor Pendidikan", "Doktor Ilmu Akuntansi", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Teknologi Pendidikan", "Pendidikan Matematika"]

    konteks = {
        'jdl': judul,
    }
    return render(request, 'pascasarjana.html', konteks)