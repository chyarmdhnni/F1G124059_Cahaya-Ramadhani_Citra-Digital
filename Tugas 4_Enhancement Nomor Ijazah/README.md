# Tugas Pertemuan 4: Enhancement Nomor Ijazah

## Deskripsi
Tugas ini merupakan bagian dari mata kuliah Pengolahan Citra Digital (PCD) yang berfokus pada peningkatan kualitas citra pada area nomor ijazah agar karakter lebih mudah dikenali oleh sistem Optical Character Recognition (OCR).

Proses pengerjaan dilakukan dengan mengambil atau melakukan cropping pada area nomor ijazah dari citra ijazah. Selanjutnya, tiga metode enhancement diterapkan, yaitu brightness adjustment, contrast stretching, dan histogram equalization. Hasil dari ketiga metode dibandingkan berdasarkan tampilan citra dan distribusi intensitas piksel untuk menentukan metode yang paling sesuai bagi proses OCR.

## Tujuan
1. Mengambil area nomor ijazah dari citra melalui proses cropping.
2. Meningkatkan kualitas citra nomor ijazah menggunakan tiga metode enhancement.
3. Membandingkan hasil brightness adjustment, contrast stretching, dan histogram equalization.
4. Menampilkan citra dan histogram sebelum serta sesudah enhancement.
5. Menentukan metode enhancement yang menghasilkan citra paling baik untuk proses OCR.
6. Menganalisis pengaruh peningkatan contrast terhadap kemampuan OCR dalam mengenali karakter.
7. Menjelaskan apakah histogram equalization selalu menjadi metode terbaik berdasarkan hasil eksperimen.

## Ketentuan Tugas
Tugas ini dikerjakan melalui tahapan berikut:

1. Mengambil atau melakukan cropping pada area nomor ijazah dari citra.
2. Menerapkan brightness adjustment pada area nomor ijazah.
3. Menerapkan contrast stretching pada area nomor ijazah.
4. Menerapkan histogram equalization pada area nomor ijazah.
5. Membandingkan hasil dari ketiga metode enhancement.
6. Menampilkan citra sebelum dan sesudah enhancement.
7. Menampilkan histogram sebelum dan sesudah enhancement.
8. Menentukan metode yang paling baik untuk membantu proses OCR.
9. Menjelaskan pengaruh peningkatan contrast terhadap pengenalan karakter dan mengevaluasi histogram equalization berdasarkan hasil eksperimen.

## Metode yang Digunakan

### 1. Cropping Area Nomor Ijazah
Cropping dilakukan untuk mengambil bagian citra yang memuat nomor ijazah. Proses ini memusatkan pengolahan pada area yang menjadi objek utama sehingga analisis dan enhancement lebih terarah.

### 2. Brightness Adjustment
Brightness adjustment digunakan untuk menyesuaikan tingkat kecerahan citra. Metode ini dapat membantu memperjelas nomor ijazah ketika area tersebut terlalu gelap atau terlalu terang, bergantung pada penyesuaian yang diterapkan.

### 3. Contrast Stretching
Contrast stretching digunakan untuk memperluas rentang intensitas piksel sehingga perbedaan antara karakter dan latar belakang dapat terlihat lebih jelas.

### 4. Histogram Equalization
Histogram equalization digunakan untuk mendistribusikan intensitas piksel agar rentang keabuan lebih merata. Metode ini bertujuan meningkatkan kontras berdasarkan distribusi intensitas citra.

## Tahapan Pengerjaan

### 1. Persiapan Citra
Menyiapkan citra ijazah yang menjadi bahan pengolahan.

### 2. Cropping
Mengambil area nomor ijazah dari citra untuk dijadikan objek utama enhancement.

### 3. Penerapan Enhancement
Menerapkan brightness adjustment, contrast stretching, dan histogram equalization pada area nomor ijazah.

### 4. Perbandingan Hasil
Menampilkan dan membandingkan citra sebelum enhancement dengan hasil dari ketiga metode. Histogram sebelum dan sesudah enhancement juga ditampilkan untuk mengamati perubahan distribusi intensitas piksel.

### 5. Evaluasi untuk OCR
Menganalisis hasil enhancement untuk menentukan metode yang paling sesuai dalam membantu OCR mengenali karakter nomor ijazah. Evaluasi didasarkan pada hasil eksperimen, bukan hanya pada tampilan histogram.

## Teknologi yang Digunakan
- Python
- Pengolahan Citra Digital
- Teknik enhancement citra
- Histogram intensitas piksel
- Optical Character Recognition (OCR)

## Cara Menjalankan Program

### 1. Buka Folder Tugas
Buka folder `Tugas 4_Enhancement Nomor Ijazah` menggunakan Visual Studio Code.

### 2. Buka Terminal
Pada Visual Studio Code, pilih menu **Terminal → New Terminal** untuk membuka terminal.

### 3. Jalankan Program Python
Jalankan file Python yang digunakan dalam tugas ini menggunakan perintah:

```powershell
python nama_file.py
```

Ganti `nama_file.py` dengan nama file program Python yang tersedia di folder tugas.

### 4. Amati Hasil Program
Setelah program dijalankan, amati:
- Hasil cropping area nomor ijazah.
- Citra hasil brightness adjustment.
- Citra hasil contrast stretching.
- Citra hasil histogram equalization.
- Perbandingan citra sebelum dan sesudah enhancement.
- Histogram sebelum dan sesudah enhancement.
- Hasil evaluasi untuk menentukan metode yang paling sesuai bagi OCR.

Pastikan Python dan pustaka yang diperlukan oleh program sudah terpasang sebelum menjalankannya.

## Hasil yang Diharapkan
1. Citra hasil cropping area nomor ijazah.
2. Citra hasil brightness adjustment.
3. Citra hasil contrast stretching.
4. Citra hasil histogram equalization.
5. Perbandingan citra sebelum dan sesudah enhancement.
6. Histogram sebelum dan sesudah enhancement.
7. Analisis metode enhancement terbaik untuk proses OCR.
8. Pembahasan mengenai pengaruh contrast terhadap pengenalan karakter.
9. Penjelasan mengenai efektivitas histogram equalization berdasarkan hasil eksperimen.

## Pembahasan
Peningkatan contrast dapat membantu OCR karena perbedaan intensitas antara karakter nomor ijazah dan latar belakang menjadi lebih jelas, sehingga karakter berpotensi lebih mudah dipisahkan dan dikenali.

Histogram equalization tidak selalu menjadi metode terbaik. Hasilnya bergantung pada kondisi awal citra dan perubahan intensitas yang dihasilkan. Karena itu, ketiga metode perlu dibandingkan berdasarkan citra hasil enhancement dan kemampuan OCR mengenali karakter nomor ijazah.

## Kesimpulan
Enhancement dilakukan untuk meningkatkan kualitas area nomor ijazah agar karakter lebih mudah dikenali oleh OCR. Brightness adjustment, contrast stretching, dan histogram equalization dibandingkan melalui tampilan citra dan histogram sebelum serta sesudah pengolahan. Metode terbaik ditentukan berdasarkan hasil eksperimen dan keterbacaan karakter, bukan semata-mata berdasarkan persebaran histogram.