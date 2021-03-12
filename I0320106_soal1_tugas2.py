#Nama: Utsman Arifin Al Fauzi
#NIM: I0320106
#Kelas: C

kosong=True
def start():
    pilihan= input('''
Pilih alat hitung/konversi:
    1. Penghitung luas persegi panjang
    2. Penghitung luas lingkaran
    3. Penghitung luas dan volume kubus
    4. Konversi suhu Celsius ke Fahrenheit
    5. Konversi suhu Reamur ke Kelvin
Pilihan anda (masukkan angka): ''')
    if pilihan=='1':
        print('Penghitung Luas Persegi Panjang')
        p=float(input('Masukkan panjang persegi panjang (cm): '))
        l=float(input('Masukkan lebar persegi panjang (cm): '))
        L=p*l
        print('Luas persegi panjang adalah', L, 'cm')
    elif pilihan=='2':
        print('Penghitung Luas Lingkaran')
        r=float(input('Masukkan jari-jari lingkaran (cm): '))
        L=3.14*(r**2)
        print('Luas lingkaran adalah', L, 'cm')
    elif pilihan=='3':
        print('Penghitung Luas dan Volume Kubus')
        r=float(input('Masukkan panjang rusuk kubus (cm): '))
        L=6*(r**2)
        V=r**3
        print('Luas permukaan kubus adalah', L, 'cm^2, dan volumenya', V, 'cm^3')
    elif pilihan=='4':
        print('Konversi Suhu Celcius ke Fahrenheit')
        C=float(input('Masukkan suhu (Celcius): '))
        F=9*C/5+32
        print(C, 'derajat Celsius adalah', F, 'derajat Fahrenheit')
    elif pilihan=='5':
        print('Konversi suhu Reamur ke Kelvin')
        R=float(input('Masukkan suhu (Reamur): '))
        K=5*R/4+273
        print(R, 'derajat Reamur adalah', K, 'Kelvin')
    else:
        print('Input tidak dikenal')
while kosong:
    start()
