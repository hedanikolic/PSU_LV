broj = 2

while broj < 0 or broj > 1:
    try:
        broj = float(input('Upisite ocjenu(od 0.0 do 1.0): '))
        if broj > 1:
            print('Broj mora biti u zadanom intervalu.')
        elif broj >= 0.9:
            print('A')
        elif broj >= 0.8:
            print('B')
        elif broj >= 0.7:
            print('C')
        elif broj >= 0.6:
            print('D')
        else:
            print('F')

    except:
         print('Ocjena mora biti broj.')