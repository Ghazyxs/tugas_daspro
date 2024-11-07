"""Rafi Ghazy Athallah
    1B RPL
    2405433"""

def hitung_nilai(*nilai):
    total = sum(nilai)
    rata_rata = total / len(nilai)
    return total, rata_rata

# Minta jumlah angka, pastikan input positif dan berupa angka
total_angka = input("Masukkan jumlah angka: ")
while not total_angka.isdigit() or int(total_angka) <= 0:
    print("Input harus berupa angka positif!")
    total_angka = input("Masukkan jumlah angka: ")
total_angka = int(total_angka)

nilai = []
print("Masukkan nilai:")

# Loop untuk meminta input angka dari pengguna
for i in range(total_angka):
    angka = input(f"Masukkan angka {i + 1}: ")
    while not angka.isdigit():
        print("Input harus berupa angka!")
        angka = input(f"Masukkan angka {i + 1}: ")
    nilai.append(int(angka))

# Hitung total dan rata-rata
total, rata_rata = hitung_nilai(*nilai)

# Tampilkan hasil total dengan format yang rapi
print("\nTotal:", end=" ")
for i, n in enumerate(nilai):
    if i == len(nilai) - 1:
        print(f"{n} = {total}")
    else:
        print(f"{n} +", end=" ")

# Tampilkan hasil rata-rata
print(f"Rata-rata: {total}/{len(nilai)} = {rata_rata}")