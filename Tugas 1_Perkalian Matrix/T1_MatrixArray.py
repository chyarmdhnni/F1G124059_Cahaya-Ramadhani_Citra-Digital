def input_array(nama, jumlah, baris, kolom):
    array = []

    print(f"\n--- Input Array {nama} ---")

    for i in range(jumlah):
        print(f"Matrix {i + 1}")

        matrix = []

        for j in range(baris):
            data = list(map(int, input(f"  Baris {j + 1}: ").split()))
            matrix.append(data)

        array.append(matrix)

    return array


def perkalian_3d(A, B):
    hasil = []

    for k in range(len(A)):
        matrix = []

        for i in range(len(A[k])):
            baris = []

            for j in range(len(B[k][0])):
                total = 0

                for l in range(len(A[k][0])):
                    total += A[k][i][l] * B[k][l][j]

                baris.append(total)

            matrix.append(baris)

        hasil.append(matrix)

    return hasil


def tampilkan(array, nama):
    print(f"\n{nama}")

    for i in range(len(array)):
        print(f"Matrix {i + 1}:")
        for baris in array[i]:
            print(" ".join(map(str, baris)))
        print()


# Program utama
print("=" * 40)
print("     PERKALIAN ARRAY MATRIX 3D")
print("=" * 40)

jumlah = int(input("Jumlah lapisan matrix : "))

print("\nUkuran Matrix A")
baris_A = int(input("Jumlah baris  : "))
kolom_A = int(input("Jumlah kolom : "))

print("\nUkuran Matrix B")
baris_B = int(input("Jumlah baris  : "))
kolom_B = int(input("Jumlah kolom : "))

A = input_array("A", jumlah, baris_A, kolom_A)
B = input_array("B", jumlah, baris_B, kolom_B)

hasil = perkalian_3d(A, B)

print("\n" + "=" * 40)
print("             HASIL")
print("=" * 40)

tampilkan(A, "Array A")
tampilkan(B, "Array B")
tampilkan(hasil, "Hasil A x B")