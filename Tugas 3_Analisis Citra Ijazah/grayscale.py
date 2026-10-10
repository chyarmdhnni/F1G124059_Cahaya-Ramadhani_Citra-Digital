import cv2
from pathlib import Path
import os


# Folder tempat gambar
folder_picture = Path("picture")


# Mencari semua gambar
ekstensi = [
    "*.jpg",
    "*.jpeg",
    "*.png",
    "*.bmp"
]

files = []

for ext in ekstensi:
    files.extend(folder_picture.glob(ext))

# Mengurutkan gambar
files = sorted(files)


# Membuat folder untuk hasil grayscale
os.makedirs("hasil_grayscale", exist_ok=True)


# Mengecek jumlah gambar
print(f"Jumlah gambar ditemukan: {len(files)}")


# Memproses semua gambar
for file in files:

    # Membaca gambar
    img = cv2.imread(str(file))

    # Mengecek apakah gambar berhasil dibaca
    if img is None:
        print(f"Gagal membaca: {file}")
        continue

    # Mengubah gambar menjadi grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mengambil nama file asli
    nama_file = os.path.basename(file)

    # Membuat nama hasil
    nama_hasil = f"grayscale_{nama_file}"

    # Lokasi penyimpanan
    output = os.path.join("hasil_grayscale", nama_hasil)

    # Menyimpan gambar grayscale
    cv2.imwrite(output, gray)

    print(f"Berhasil: {nama_file}")


print("\nSemua gambar berhasil diubah menjadi grayscale!")