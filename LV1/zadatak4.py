import sys

count = 0
suma = 0
min = sys.maxsize
max = 0 - min
unos = ''

while unos != 'Done':
    try:
        unos = input()
        broj = float(unos)

        count += 1
        suma += broj
    
        if broj < min:
            min = broj
        if broj > max:
            max = broj

    except:
        print('Unesite broj ili "Done".')

srv = suma / count

print('Broj unesenih brojeva: ', count, '\nSrednja vrijednost: ', srv, '\nMinimalna vrijednost: ', min, '\nMaksimalna vrijednost: ', max)
