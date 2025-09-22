"""
Arbeidskrav1
Sist redigert 25.09.22
@author: Andreas Buskop

Verktøy regner ut årlige utgifter for elbil og bensinbil, 
samt plotter dette i en graf
"""
import numpy as np
import matplotlib.pyplot as plt

km=10000 #antall årlige kjørte km [km]
avg=8.38 #Trafikkforsikringsavgift for bil [NOK/dag]

#bensinbil
f_b=7500 #årlig forsikringspris for bensinbil [NOK/år]
bom_b=0.3 #bomavgift bensinbil [nok/km]
d_b=1.0 #drivstoff kostnad bensinbil [NOK/km]

#elbil
f_el=5000 #årlig forsikringspris for el-bil [NOK/år]
s=2.0 #strømkostnad [NOK/kWh]
f_el_forbruk=0.2 #drivstoff forbruk elbil [kWh/km]
d_el=f_el_forbruk*s #drivstoff kostnad elbil [NOK/km]
bom_el=0.1 #bomavgift bensinbil [nok/km]

#beregning av årlige kostnader
tot_b_per_ar=avg*365 + f_b + bom_b*km + d_b*km #årlige avgifter bensinbil [NOK]
tot_el_per_ar=avg*365 + f_el + bom_el*km + d_el*km #årlige avgifter bensinbil [NOK]

#lager array for akkumulerte kostnader
ar=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #år nr
tot_b = np.full_like(ar, tot_b_per_ar, dtype=float)
tot_el = np.full_like(ar, tot_el_per_ar, dtype=float)
akk_b = np.cumsum(tot_b)
akk_el = np.cumsum(tot_el) 

# plot
plt.figure()
plt.plot(ar, akk_b, marker="o", label="Bensinbil akkumulert")
plt.plot(ar, akk_el, marker="o", label="Elbil akkumulert")
plt.title("Akkumulert kostnad per år")
plt.xlabel("År")
plt.ylabel("Kostnad [NOK]")
plt.grid(True, linestyle=":")
plt.legend()
plt.show()            