import cv2
import pytesseract
import os

# Lokasi Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Folder
input_folder = "picture"
hasil_folder = "hasil"
ocr_folder = "ocr"

# Daftar gambar
files = [
    "01_HighQuality_Enhanced (1).jpg",
    "02_LowContrast (1).jpg",
    "03_Blurred (1).jpg",
    "04_HighNoise (1).jpg",
    "05_LowResolution_Upsampled (1).jpg",
    "06_Faded_Underexposed (1).jpg",
    "07_ColorShift_WarmTint (1).jpg",
    "08_JPEGCompression_Artifacts (1).jpg",
    "09_CombinedDegradation (1).jpg"
]

# Buat folder OCR utama
os.makedirs(ocr_folder, exist_ok=True)

# Proses semua gambar
for i, filename in enumerate(files, start=1):

    print(f"\n===== GAMBAR {i:02d} =====")

    # Buat folder OCR untuk setiap gambar
    image_ocr_folder = os.path.join(ocr_folder, f"{i:02d}")
    os.makedirs(image_ocr_folder, exist_ok=True)

    # ==========================================
    # 1. OCR ORIGINAL
    # ==========================================

    original_path = os.path.join(input_folder, filename)
    original = cv2.imread(original_path)

    if original is None:
        print(f"Original tidak ditemukan: {filename}")
        continue

    text_original = pytesseract.image_to_string(
        original,
        config="--psm 6"
    )

    # Simpan hasil OCR Original
    original_txt = os.path.join(image_ocr_folder, "original.txt")

    with open(original_txt, "w", encoding="utf-8") as f:
        f.write(text_original)

    print("Original selesai.")

    # ==========================================
    # 2. OCR HASIL FILTER
    # ==========================================

    image_folder = os.path.join(hasil_folder, f"{i:02d}")

    filter_files = [
        "mean_filter.jpg",
        "median_filter.jpg",
        "gaussian_filter.jpg",
        "sharpening.jpg"
    ]

    for filter_file in filter_files:

        filter_path = os.path.join(image_folder, filter_file)

        image = cv2.imread(filter_path)

        if image is None:
            print(f"{filter_file} tidak ditemukan.")
            continue

        text = pytesseract.image_to_string(
            image,
            config="--psm 6"
        )

        # Nama txt mengikuti nama gambar
        txt_name = filter_file.replace(".jpg", ".txt")
        txt_path = os.path.join(image_ocr_folder, txt_name)

        # Simpan hasil OCR
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"{filter_file} selesai.")

print("\n===== OCR SELESAI =====")
print("Semua hasil OCR sudah disimpan di folder 'ocr'.")