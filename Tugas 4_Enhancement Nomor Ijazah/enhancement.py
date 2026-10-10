import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

# Folder input dan output
input_folder = "picture"
output_folder = "hasil"

os.makedirs(output_folder, exist_ok=True)

# Proses 9 gambar
for i in range(1, 10):

    filename = f"{i:02d}_Ijazah.jpg"
    image_path = os.path.join(input_folder, filename)

    image = cv2.imread(image_path)

    if image is None:
        print(f"Gagal membaca: {filename}")
        continue

    print(f"Memproses: {filename}")

    # Crop area nomor ijazah
    crop = image[2200:3450, 1400:2450]

    # Grayscale
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

    # Brightness Adjustment
    brightness = cv2.convertScaleAbs(gray, alpha=1.0, beta=40)

    # Contrast Stretching
    min_val = np.min(gray)
    max_val = np.max(gray)

    if max_val > min_val:
        contrast = ((gray - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    else:
        contrast = gray.copy()

    # Histogram Equalization
    equalized = cv2.equalizeHist(gray)

    # Folder khusus untuk setiap ijazah
    image_output_folder = os.path.join(output_folder, f"{i:02d}_Ijazah")
    os.makedirs(image_output_folder, exist_ok=True)

    # Simpan citra
    cv2.imwrite(os.path.join(image_output_folder, "crop.jpg"), crop)
    cv2.imwrite(os.path.join(image_output_folder, "grayscale.jpg"), gray)
    cv2.imwrite(os.path.join(image_output_folder, "brightness.jpg"), brightness)
    cv2.imwrite(os.path.join(image_output_folder, "contrast_stretching.jpg"), contrast)
    cv2.imwrite(os.path.join(image_output_folder, "histogram_equalization.jpg"), equalized)

    # Histogram
    plt.figure(figsize=(10, 6))

    plt.hist(gray.ravel(), 256, [0, 256], label="Sebelum Enhancement")
    plt.hist(brightness.ravel(), 256, [0, 256], label="Brightness")
    plt.hist(contrast.ravel(), 256, [0, 256], label="Contrast Stretching")
    plt.hist(equalized.ravel(), 256, [0, 256], label="Histogram Equalization")

    plt.title(f"Perbandingan Histogram - {filename}")
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")
    plt.legend()

    plt.savefig(
        os.path.join(image_output_folder, "histogram_perbandingan.jpg")
    )

    plt.close()

    # Perbandingan citra
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Sebelum Enhancement")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(brightness, cmap="gray")
    plt.title("Brightness Adjustment")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(contrast, cmap="gray")
    plt.title("Contrast Stretching")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(equalized, cmap="gray")
    plt.title("Histogram Equalization")
    plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        os.path.join(image_output_folder, "perbandingan.jpg")
    )

    plt.close()
    
print("Semua gambar selesai diproses.")