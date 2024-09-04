from django.shortcuts import render

# from django.shortcuts import render berguna untuk mengimpor fungsi render dari modul django.shortcuts.
# Fungsi render akan digunakan untuk render tampilan HTML dengan menggunakan data yang diberikan.

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306214025',
        'name': 'Shafa Amira Azka',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)


# Penjelasan Kode:

# Potongan kode di atas mendeklarasikan fungsi show_main, yang menerima parameter request. Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.

# context adalah dictionary yang berisi data untuk dikirimkan ke tampilan. Pada saat ini, terdapat tiga data yang disertakan, yaitu:

# npm: Data npm-mu.
# name: Data namamu.
# class: Data kelasmu.
# return render(request, "main.html", context) berguna untuk me-render tampilan main.html dengan menggunakan fungsi render. Fungsi render mengambil tiga argumen:

# request: Ini adalah objek permintaan HTTP yang dikirim oleh pengguna.
# main.html: Ini adalah nama berkas template yang akan digunakan untuk me-render tampilan.
# context: Ini adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.