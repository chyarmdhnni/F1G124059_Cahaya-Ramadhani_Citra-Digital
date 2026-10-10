import cv2
import os

# Folder input dan output
input_folder = "picture"
output_folder = "hasil"

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

# Proses semua gambar
for i, filename in enumerate(files, start=1):

    # Lokasi gambar
    input_path = os.path.join(input_folder, filename)

    # Baca gambar
    image = cv2.imread(input_path)

    # Cek apakah gambar berhasil dibaca
    if image is None:
        print(f"Gambar tidak ditemukan: {filename}")
        continue

    # Buat folder khusus untuk setiap gambar
    image_folder = os.path.join(output_folder, f"{i:02d}")
    os.makedirs(image_folder, exist_ok=True)

    # ==========================================
    # 1. MEAN FILTER
    # ==========================================

    mean_filter = cv2.blur(image, (5, 5))

    mean_path = os.path.join(image_folder, "mean_filter.jpg")
    cv2.imwrite(mean_path, mean_filter)

    # ==========================================
    # 2. MEDIAN FILTER
    # ==========================================

    median_filter = cv2.medianBlur(image, 5)

    median_path = os.path.join(image_folder, "median_filter.jpg")
    cv2.imwrite(median_path, median_filter)

    # ==========================================
    # 3. GAUSSIAN FILTER
    # ==========================================

    gaussian_filter = cv2.GaussianBlur(image, (5, 5), 0)

    gaussian_path = os.path.join(image_folder, "gaussian_filter.jpg")
    cv2.imwrite(gaussian_path, gaussian_filter)

    # ==========================================
    # 4. SHARPENING
    # ==========================================

    blur_for_sharpen = cv2.GaussianBlur(image, (0, 0), 3)

    sharpened = cv2.addWeighted(
        image, 1.5,
        blur_for_sharpen, -0.5,
        0
    )

    sharpening_path = os.path.join(image_folder, "sharpening.jpg")
    cv2.imwrite(sharpening_path, sharpened)

    print(f"Gambar {i:02d} selesai diproses.")

print("\nMean Filter, Median Filter, Gaussian Filter, dan Sharpening selesai untuk semua gambar.")