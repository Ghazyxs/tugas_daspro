"""Rafi Ghazy Athallah
    1B RPL
    2405433"""

def hitung_nilai(*nilai):
    total = sum(nilai)
    rata_rata = total / len(nilai)
    return total, rata_rata

total_angka = int(input("masukan jumlah angka: "))

nilai = []
print("Masukkan nilai")
for i in range(total_angka):
    angka = int(input(f"masukan angka {i + 1}: "))
    nilai.append(int(angka))

# Hitung total dan rata-rata
total, rata_rata = hitung_nilai(*nilai)

# Tampilkan hasil
print("\nTotal:", end=" ")
for i, n in enumerate(nilai):
    if i == len(nilai) - 1:
        print(f"{n} = {total}")
    else:
        print(f"{n} +", end=" ")

print(f"Rata-rata: {total}/{len(nilai)} = {rata_rata}")