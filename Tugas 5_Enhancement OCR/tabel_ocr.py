import os
import difflib

# Ground Truth
ground_truth = "Nomor ijazah: 571012022000056"

ocr_folder = "ocr"
output_file = "tabel_ocr.txt"

methods = {
    "Original": "original.txt",
    "Mean Filter": "mean_filter.txt",
    "Median Filter": "median_filter.txt",
    "Gaussian Filter": "gaussian_filter.txt",
    "Sharpening": "sharpening.txt"
}


# Menghapus spasi karena spasi tidak dihitung sebagai karakter
def bersihkan_teks(text):
    return "".join(text.split())


# Menghitung jumlah karakter yang benar
def hitung_karakter_benar(hasil, asli):

    hasil = bersihkan_teks(hasil)
    asli = bersihkan_teks(asli)

    matcher = difflib.SequenceMatcher(None, hasil, asli)

    karakter_benar = 0

    for block in matcher.get_matching_blocks():
        karakter_benar += block.size

    return karakter_benar


# Ground Truth tanpa spasi
ground_truth_bersih = bersihkan_teks(ground_truth)


# Membuat file hasil evaluasi
with open(output_file, "w", encoding="utf-8") as output:

    output.write("HASIL EVALUASI OCR\n\n")

    output.write(f"Ground Truth : {ground_truth}\n\n")

    output.write("Spasi tidak dihitung sebagai karakter.\n")
    output.write(
        "Akurasi dihitung berdasarkan karakter yang berhasil "
        "dikenali sesuai dengan Ground Truth.\n\n"
    )

    # Memproses Citra 01 sampai Citra 09
    for image_number in range(1, 10):

        nomor_citra = f"{image_number:02d}"

        output.write(f"CITRA {nomor_citra}\n\n")

        output.write(
            "| Metode          | Hasil OCR                              | Karakter Benar | Akurasi |\n"
        )

        output.write(
            "|-----------------|----------------------------------------|----------------|---------|\n"
        )

        # Memproses setiap metode
        for method, filename in methods.items():

            file_path = os.path.join(
                ocr_folder,
                nomor_citra,
                filename
            )

            # Jika file OCR tidak ditemukan
            if not os.path.exists(file_path):

                hasil_ocr = "File tidak ditemukan"
                karakter_benar = 0
                akurasi = 0

            else:

                # Membaca hasil OCR
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read()

                # Membersihkan hasil OCR untuk ditampilkan
                hasil_ocr = " ".join(text.split())

                # Menghitung karakter yang benar
                karakter_benar = hitung_karakter_benar(
                    text,
                    ground_truth
                )

                # Menghitung akurasi
                akurasi = (
                    karakter_benar /
                    len(ground_truth_bersih)
                ) * 100

            # Menulis hasil ke tabel
            output.write(
                f"| {method:<15} | "
                f"{hasil_ocr:<38} | "
                f"{karakter_benar:<14} | "
                f"{akurasi:.2f}% |\n"
            )

        output.write("\n\n")


print("HASIL EVALUASI OCR SELESAI")
print(f"Ground Truth : {ground_truth}")
print("Spasi tidak dihitung sebagai karakter.")
print(f"File hasil : {output_file}")