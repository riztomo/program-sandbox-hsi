import random

sel = [10, 10]
jawaban = ['Z', 'Z']
benar = 0
salah = 0

soal = (
    '\tDalam Python, apa nama daftar yang isinya tidak dapat diubah kembali setelah diinisialisasi?\n\tA. Tuple\n\t'
    'B. List\n\tC. Dictionary\n\tD. Array',
    '\tVersi Python berapakah yang paling baru?\n\tA. Versi 1\n\tB. Versi 2\n\tC. Versi 3\n\tD. Versi 4',
    '\tApa hukum menuntut ilmu (agama) bagi setiap muslim?\n\tA. Wajib\n\tB. Sunnah\n\tC. Mubah\n\tD. Makruh',
    '\tApa tiga pertanyaan yang diajukan nanti di alam kubur?\n\tA. Tuhan, Rasul, Agama\n\tB. Tuhan, Rasul, Kiblat'
    '\n\tC. Rasul, Saudara, Kitab\n\tD. Rasul, Saudara, Kiblat',
    '\tApa istilah yang digunakan bagi orang yang terlihat beriman namun hatinya tidak?\n\tA. Fasik\n\tB. Kafir\n\t'
    'C. Musyrik\n\tD. Munafik'
)

answers = {
    0: 'A',
    1: 'C',
    2: 'A',
    3: 'A',
    4: 'D'
}

print("-----------------------")
print("|SIMULASI EVALUASI HSI|")
print("-----------------------")

print('\nMasukkan jawaban dengan sebuah huruf sesuai pilihan yang diberikan, yaitu A, B, C atau D.')
print('Ingat, hanya masukkan sebuah huruf, jangan masukkan karakater lain.')
print("\nPertanyaan pertama:")

selection = random.randint(0, 4)
sel[0] = selection

print(soal[sel[0]])
jawaban[0] = input('\n\tJawaban Anda: ')

if jawaban[0].upper() != "A" and jawaban[0].upper() != "B" and jawaban[0].upper() != "C" and jawaban[0].upper() != "D":
    print('\n\tJawaban Anda bukanlah pilihan yang terdapat di dalam pertanyaan.')
    jawaban[0] = input('\tJawaban Anda: ')

print("\nPertanyaan kedua:")

while selection == sel[0]:
    selection = random.randint(0, 4)
sel[1] = selection

print(soal[sel[1]])
jawaban[1] = input('\n\tJawaban Anda: ')

for x in range(2):
    if jawaban[x].upper() == answers.get(sel[x]):
        benar += 1
    else:
        salah += 1

print('\nBerikut adalah hasil Anda:')
print(f'Benar: {benar}')
print(f'Salah: {salah}')

print('\n')
print("--------------------")
print("|AKHIR DARI PROGRAM|")
print("--------------------")
