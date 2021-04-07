import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv ('mtcars.csv')
#1.
prvi = mtcars.sort_values(by = 'mpg').head(5)
#print('5 automobila koji imaju najveću potrosnju:\n', prvi,'\n')

#2.
mt = mtcars[(mtcars.cyl == 8)]
drugi = mt.sort_values(by = 'mpg', ascending = False).head(3)
#print('Tri automobila s 8 cilindara koji imaju najmanju potrosnju:\n', drugi,'\n')

#3.
mt6cyl = mtcars[(mtcars.cyl == 6)]
treci = mt6cyl.mean().mpg
#print('Srednja potrosnja automobila sa 6 cilindara: ', treci, '\n')

#4.
mt4cyl = mtcars[(mtcars.cyl == 4) & (mtcars.wt > 2) & (mtcars.wt < 2.2)]
cetvrti = mt4cyl.mean().mpg
#print('Srednja potrosnja automobila s 4 cilindra mase između 2000 i 2200 lbs: ', cetvrti, '\n')

#5.
rucni = len(mtcars[mtcars.am == 1])
#print('Broj automobila s rucnim mjenjacem:',rucni)

automatik = len(mtcars[mtcars.am == 0])
#print('Broj automobila s automatskim mjenjacem:',automatik, '\n')

#6.
sesti = len(mtcars[(mtcars.am == 0) & (mtcars.hp > 100)])
#print('Broj automobila s automatskim mjenjacem i snagom preko 100 konjskih snaga: ', sesti, '\n')

#7.
kg = mtcars.wt*1000.0*0.453592
mtcars.wt = kg
print('Masa svakog automobila u kilogramima:\n', mtcars)