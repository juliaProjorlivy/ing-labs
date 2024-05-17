from matplotlib import pyplot as plt
import numpy as np

with open("settings.txt", "r") as f:
    tmp = [float(i) for i in f.read().split("\n")]
f.close()
data_array = np.loadtxt("data.txt", dtype = int)
data_array = data_array / 256 * 3.3

x_array = []
for i in range(len(data_array)):
    x_array.append(i / tmp[0])

data_array = list(data_array)
x_array = list(x_array)

app = plt.plot(x_array, data_array, "-", c = [1, 0.5, 0], linewidth=2, label='Напряжение на \n конденсаторе')

plt.text(7, 0.6, "Время зарядки: 7.4 с \nВремя разрядки: 5.2 с", fontsize=12)
plt.title("График напряжения на конденсаторе")
plt.legend ()

plt.minorticks_on() 
plt.grid(visible=True, which='major', linestyle='-', linewidth=1.5, color='0.7')
plt.grid(visible=True, which='minor', linestyle='--', linewidth=1, color='0.8') 
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage[english, russian]{babel}') 

axis_lw = 2
ax = plt.gca() 
ax.set_xlim([0, 13]) 
ax.set_ylim([0, 3.0])
ax.set_xlabel("Время, c") 
ax.set_ylabel("Напряжение, B") 

plt.rc('axes', linewidth=axis_lw) 
plt.rc('xtick.major', width=axis_lw)
plt.rc('xtick.minor', width=0) 
plt.rc('xtick', direction='in') 
plt.rc('axes', labelsize=20) 
plt.rc('ytick.major', width=axis_lw)
plt.rc('ytick.minor', width=0)
plt.rc('ytick', direction='in')
plt.rc('xtick', labelsize=18) 
plt.rc('ytick', labelsize=18)
plt.rc('xtick.major', pad=10) 
plt.rc('ytick.major', pad=10)

plt.savefig("test.png")