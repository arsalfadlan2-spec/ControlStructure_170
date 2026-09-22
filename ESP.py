while True:
    nilai = float(input("Masukkan nilaimu Rakyatku: "))

    if nilai >= 90:
        print("Excellent performance")
        print("Selamat ya Rakyatku, kamu hebat!")
    elif nilai >= 80:
        print("Very Good performance")
        print("Selamat ya Rakyatku, kamu hebat!")
    elif nilai >= 70:
        print("Good performance")
        print("Semangat ya Rakyatku, kamu bisa lebih baik lagi!")
    elif nilai >= 60:
        print("Average performance")
        print("Semangat ya Rakyatku, kamu bisa lebih baik lagi!")
    else:
        print("Below average performance")
        print("Belajar lagi ya Rakyatku, jangan menyerah!")

    ulang = input("Apakah Anda ingin memasukkan nilai lagi? (y/n): ")
    if ulang.lower() != 'y':
        print("Terima kasih ya rakyatku ini 50 $ untukmu, semoga bermanfaat")
        break
    # finish
    # membuat program untuk menentukan kinerja berdasarkan nilai persentase yang dimasukkan oleh pengguna. Program ini menggunakan struktur percabangan if-elif-else untuk mengevaluasi nilai dan memberikan output yang sesuai.