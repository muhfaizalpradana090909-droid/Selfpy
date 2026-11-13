nilai1 = int(input('nilai ujian pertama')) 
nilai2 = int(input('nilai ujian kedua')) 
nilai3 = int(input('nilai ujian ketiga'))
kehadiran = int(input('rasio kehadiran ='))
nilairata_rata = (nilai1 + nilai2 + nilai3)/3

print('nila rata - rata = ', nilairata_rata)
print('syarat nilai =', nilairata_rata >= 90)
print('syarat kehadiran = ', kehadiran >= 90) 

#syarat kelulusan 
kehadiran2 = kehadiran >= 90
nilairata2 = nilairata_rata >= 90
kelulusan = kehadiran2 and nilairata2
print('lulus = ',kelulusan)


syarat_alternatif = kehadiran >= 100 or nilairata_rata >= 75
print('syrat alternatif = ', kelulusan)
