Mahasiswa = ['Funny', 'Vizal', 'Gea', 'Aratia', 'Divana', 'Bagus', 'Erika', 'Efa', 'Angela', 'Atthan']

print (Mahasiswa[4])
print (Mahasiswa[6])
print (Mahasiswa[7])

Mahasiswa[3] = 'Audrey'
Mahasiswa[5] = 'Attar'
Mahasiswa[9] = 'Candrika'

Mahasiswa.append ('Zaki')
Mahasiswa.append ('Tsania')

A = 0
for Nama in range (0,12):
    print (Mahasiswa[A])
    A = A + 1
print(len(Mahasiswa))
