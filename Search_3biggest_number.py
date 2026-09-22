a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

print("Angka terbesar adalah:", terbesar)
#catatan sudah menyelesaikan pencarian angka terbesar dari tiga angka yang dimasukkan oleh pengguna. Program ini menggunakan struktur percabangan if-elif-else untuk membandingkan ketiga angka dan menentukan angka terbesar di antara mereka.