# Tugas Pertemuan 5 Enhancement untuk OCR

**Topik:** Filtering, Noise Reduction, dan Sharpening

## Deskripsi Tugas

Diberikan citra nomor ijazah yang memiliki noise atau kualitas rendah. Tugas ini bertujuan untuk membandingkan beberapa metode enhancement dan mengetahui pengaruhnya terhadap hasil Optical Character Recognition (OCR).

## Metode yang Digunakan

1. **Mean Filter** — mengurangi noise dengan menghitung rata-rata nilai piksel di sekitarnya.
2. **Median Filter** — mengurangi noise dengan mengganti nilai piksel menggunakan median dari piksel di sekitarnya.
3. **Gaussian Filter** — menghaluskan citra untuk mengurangi noise menggunakan distribusi Gaussian.
4. **Sharpening** — mempertajam detail dan tepi karakter agar lebih mudah dikenali.

## Langkah Pengerjaan

1. Menggunakan citra nomor ijazah sebagai citra input.
2. Menerapkan mean filter, median filter, Gaussian filter, dan sharpening.
3. Membandingkan hasil citra dari setiap metode enhancement.
4. Menggunakan citra hasil enhancement sebagai input OCR.
5. Membandingkan hasil pengenalan karakter dari setiap metode.
6. Menganalisis metode yang memberikan hasil OCR terbaik berdasarkan hasil eksperimen.

## Hasil OCR

Hasil OCR setiap metode dicatat untuk dibandingkan, meliputi teks yang dikenali, jumlah karakter yang benar, dan akurasi pengenalan. Nilai diisi berdasarkan hasil eksperimen yang sebenarnya.

## Pertanyaan Analisis

**1. Mengapa median filter dapat memberikan hasil OCR yang lebih baik pada citra yang mengandung salt-and-pepper noise?**

Median filter menggunakan nilai tengah dari piksel di sekitar suatu piksel sehingga dapat mengurangi noise berupa titik hitam dan putih tanpa terlalu menghilangkan tepi karakter.

**2. Apakah citra yang paling bagus secara visual selalu menghasilkan OCR dengan akurasi tertinggi? Jelaskan.**

Tidak selalu. Hasil visual yang terlihat lebih halus atau tajam belum tentu mempertahankan seluruh detail karakter yang dibutuhkan OCR. Karena itu, hasil setiap metode perlu dibandingkan berdasarkan kualitas citra dan akurasi pengenalan karakter.

## Cara Menjalankan Program

Jalankan program melalui terminal pada folder tugas menggunakan perintah berikut:

```bash
python nama_file.py
```

Ganti `nama_file.py` dengan nama file Python yang digunakan dalam tugas ini.

## Kesimpulan

Melalui tugas ini, dilakukan perbandingan metode filtering, noise reduction, dan sharpening untuk meningkatkan kualitas citra nomor ijazah. Efektivitas setiap metode dinilai berdasarkan perubahan kualitas citra serta hasil pengenalan karakter menggunakan OCR.