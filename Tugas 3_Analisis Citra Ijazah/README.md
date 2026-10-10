# Tugas Pertemuan 3: Analisis Citra Ijazah

## Deskripsi
Tugas ini merupakan bagian dari mata kuliah Pengolahan Citra Digital (PCD). Tugas ini membahas analisis kualitas citra dokumen ijazah yang memiliki kondisi pencahayaan dan kualitas berbeda.

Setiap citra RGB diubah menjadi grayscale, kemudian histogram citra asli dan citra grayscale ditampilkan untuk menganalisis distribusi intensitas piksel. Berdasarkan hasil pengamatan, permasalahan pada setiap citra diidentifikasi dan metode enhancement yang sesuai ditentukan beserta alasannya.

## Tujuan
1. Mengubah citra RGB menjadi grayscale.
2. Menampilkan histogram citra asli dan citra grayscale.
3. Menganalisis distribusi intensitas piksel pada setiap citra.
4. Mengidentifikasi permasalahan kualitas citra.
5. Menentukan metode enhancement yang sesuai untuk setiap citra beserta alasannya.
6. Memahami hubungan antara distribusi histogram dan kualitas citra.

## Ketentuan Tugas
Diberikan beberapa citra dokumen ijazah dengan kondisi pencahayaan dan kualitas yang berbeda. Setiap citra dianalisis melalui tahapan berikut:

1. Mengubah setiap citra RGB menjadi grayscale.
2. Menampilkan histogram dari citra asli dan citra grayscale.
3. Menganalisis distribusi intensitas piksel pada masing-masing citra.
4. Mengidentifikasi permasalahan citra, seperti terlalu gelap, terlalu terang, contrast rendah, pencahayaan tidak merata, atau noise.
5. Menentukan metode enhancement yang paling sesuai untuk setiap citra dan memberikan alasannya.
6. Menjelaskan apakah citra dengan histogram yang lebih tersebar selalu memiliki kualitas yang lebih baik.

## Tahapan Analisis

### 1. Konversi RGB ke Grayscale
Citra ijazah berwarna dikonversi dari RGB menjadi grayscale untuk menyederhanakan informasi warna menjadi tingkat keabuan. Hasil konversi digunakan untuk mengamati distribusi intensitas piksel pada dokumen.

### 2. Analisis Histogram
Histogram citra asli dan citra grayscale ditampilkan untuk mengetahui distribusi intensitas piksel. Pada citra grayscale, intensitas piksel berada pada rentang 0–255, mulai dari hitam hingga putih.

Analisis histogram membantu mengidentifikasi karakteristik kecerahan dan kontras pada setiap citra.

### 3. Identifikasi Permasalahan Citra
Permasalahan kualitas citra diidentifikasi berdasarkan tampilan visual dan distribusi intensitas piksel, antara lain:

- **Terlalu gelap:** sebagian besar piksel memiliki intensitas rendah.
- **Terlalu terang:** sebagian besar piksel memiliki intensitas tinggi.
- **Contrast rendah:** perbedaan intensitas antara bagian gelap dan terang relatif kecil.
- **Pencahayaan tidak merata:** terdapat bagian citra yang memiliki tingkat kecerahan berbeda secara signifikan.
- **Noise:** terdapat gangguan berupa variasi intensitas piksel yang dapat mengurangi kejelasan citra.

### 4. Penentuan Metode Enhancement
Metode enhancement ditentukan berdasarkan permasalahan yang ditemukan pada setiap citra. Pemilihan metode disertai alasan yang menjelaskan kesesuaiannya dengan karakteristik citra yang dianalisis.

### 5. Evaluasi Histogram dan Kualitas Citra
Distribusi histogram digunakan sebagai salah satu indikator untuk menganalisis kualitas citra. Histogram yang lebih tersebar tidak selalu menunjukkan kualitas citra yang lebih baik karena kualitas juga dipengaruhi oleh kontras, noise, pencahayaan, dan keterbacaan informasi pada dokumen.

## Teknologi yang Digunakan
- Python
- Pengolahan Citra Digital
- Visualisasi histogram

## Cara Menjalankan Program

### 1. Buka Folder Tugas
Buka folder `Tugas 3_Analisis Citra Ijazah` menggunakan Visual Studio Code.

### 2. Buka Terminal
Pada Visual Studio Code, pilih menu **Terminal → New Terminal** untuk membuka terminal.

### 3. Jalankan Program Python
Jalankan file program Python menggunakan perintah berikut:

```powershell
python nama_file.py
```

Ganti `nama_file.py` dengan nama file Python yang digunakan pada tugas ini.

Jika Python belum dikenali oleh terminal, pastikan Python sudah terpasang dan dapat diakses melalui terminal.

### 4. Amati Hasil Program
Setelah program dijalankan, amati hasil konversi citra RGB menjadi grayscale, histogram citra asli dan grayscale, serta hasil analisis distribusi intensitas piksel pada setiap citra.

Perhatikan juga hasil identifikasi permasalahan citra dan rekomendasi metode enhancement yang sesuai dengan karakteristik setiap citra.

## Hasil yang Diharapkan
Hasil pengerjaan tugas ini meliputi:

1. Citra ijazah dalam format grayscale.
2. Histogram citra asli dan citra grayscale.
3. Analisis distribusi intensitas piksel pada setiap citra.
4. Identifikasi permasalahan kualitas citra.
5. Penentuan metode enhancement yang sesuai beserta alasannya.
6. Pembahasan mengenai hubungan distribusi histogram dengan kualitas citra.

## Kesimpulan
Analisis citra ijazah dilakukan untuk memahami karakteristik intensitas piksel dan mengidentifikasi permasalahan kualitas citra. Histogram membantu proses analisis, sedangkan pemilihan metode enhancement disesuaikan dengan kondisi setiap citra agar informasi pada dokumen dapat terlihat dengan lebih jelas.