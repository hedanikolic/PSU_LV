import matplotlib.pyplot as plt
import numpy as np

jedinice = 0
dvojke = 0
trojke = 0
cetvorke = 0
petice = 0
sestice = 0

for count in range(0,100):
    broj = np.random.randint(low = 1, high = 7)
    
    if broj == 1:
        jedinice += 1
    elif broj == 2:
        dvojke += 1
    elif broj == 3:
        trojke += 1
    elif broj == 4:
        cetvorke += 1
    elif broj == 5:
        petice += 1
    else:
        sestice += 1


print('1: ', jedinice, '\n2: ', dvojke, '\n3: ', trojke, '\n4: ', cetvorke, '\n5: ', petice, '\n6: ', sestice)

bacanja = [jedinice, dvojke, trojke, cetvorke, petice, sestice]


x = np.arange(6)
plt.hist(x)
plt.bar(x, height=[jedinice, dvojke, trojke, cetvorke, petice, sestice])
plt.xticks(x, ['1', '2', '3', '4', '5', '6'])
plt.ylim(0, 50)
plt.title('Histogram')
plt.ylabel('Pojavljivanje broja')
plt.xlabel('Broj')


plt.show()
