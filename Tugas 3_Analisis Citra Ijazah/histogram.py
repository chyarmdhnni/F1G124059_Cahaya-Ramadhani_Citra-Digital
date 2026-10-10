import cv2
from pathlib import Path
import matplotlib.pyplot as plt


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


# Membuat folder hasil histogram
folder_hasil = Path("hasil_histogram")
folder_hasil.mkdir(exist_ok=True)


# Mengecek jumlah gambar
print(f"Jumlah gambar ditemukan: {len(files)}")


# Memproses semua gambar
for nomor, file in enumerate(files, start=1):

    # Membaca gambar
    img = cv2.imread(str(file))

    # Mengecek apakah gambar berhasil dibaca
    if img is None:
        print(f"Gagal membaca: {file.name}")
        continue


    # Mengubah BGR menjadi RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # Mengubah gambar menjadi grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # ==================================================
    # HISTOGRAM RGB
    # ==================================================

    plt.figure(figsize=(10, 5))

    plt.hist(
        img_rgb[:, :, 0].ravel(),
        bins=256,
        color="red",
        alpha=0.5,
        label="Red"
    )

    plt.hist(
        img_rgb[:, :, 1].ravel(),
        bins=256,
        color="green",
        alpha=0.5,
        label="Green"
    )

    plt.hist(
        img_rgb[:, :, 2].ravel(),
        bins=256,
        color="blue",
        alpha=0.5,
        label="Blue"
    )

    plt.title(f"Histogram RGB - {file.name}")
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")
    plt.legend()

    # Menyimpan histogram RGB
    path_rgb = folder_hasil / f"histogram_rgb_{nomor}.png"

    plt.savefig(path_rgb)

    # Menutup agar tidak membuka Figure
    plt.close()


    # ==================================================
    # HISTOGRAM GRAYSCALE
    # ==================================================

    plt.figure(figsize=(10, 5))

    plt.hist(
        gray.ravel(),
        bins=256,
        range=[0, 256],
        color="black"
    )

    plt.title(f"Histogram Grayscale - {file.name}")
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")

    # Menyimpan histogram grayscale
    path_gray = folder_hasil / f"histogram_grayscale_{nomor}.png"

    plt.savefig(path_gray)

    # Menutup agar tidak membuka Figure
    plt.close()


    print(f"Berhasil membuat histogram: {file.name}")


print("\nSemua histogram berhasil dibuat!")