#menampilkan informasi program
print('Konversi suhu (Fahrenheit ke Celcius)')

#input suhu dalam fahrenheit
F = float(input('Masukkan suhu (Fahrenheit): '))

#melakukan konversi suhu ke celsius
C = 5 * (F-32) / 9

#menampilkan konversi ke layar
print('Fahrenheit: ', F)
print('Celcius', C)