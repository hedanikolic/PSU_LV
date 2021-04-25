suma = 0.0
brojac = 0

print('Ime datoteke: ')
file = input()

with open(file, 'r') as read:
    for line in read:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            start = line.find(":")
            number = float(line[(start+2):])
            suma += number
            brojac += 1

print("Srednja vrijednost je ", float(suma/brojac))