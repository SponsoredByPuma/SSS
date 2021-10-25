import matplotlib.pyplot as plt
from pylab import *
 

# with open('./70cm/70cm_01.csv', 'w', newline ='') as csvfile:
#     filewriter = csv.writer(csvfile, deli)


cm70 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\70cm\\70cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))

cm67 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\67cm\\67cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm64 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\64cm\\64cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm61 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\61cm\\61cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm58 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\58cm\\58cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm55 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\55cm\\55cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm52 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\52cm\\52cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm49 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\49cm\\49cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm46 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\46cm\\46cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm43 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\43cm\\43cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm40 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\40cm\\40cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm37 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\37cm\\37cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm34 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\34cm\\34cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm31 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\31cm\\31cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm28 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\28cm\\28cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm25 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\25cm\\25cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm22 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\22cm\\22cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm19 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\19cm\\19cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm16 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\16cm\\16cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm13 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\13cm\\13cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))
cm10 = np.genfromtxt('C:\\Users\\ti741wan\\Desktop\\versuch1\\10cm\\10cm_10.csv', dtype=float, delimiter=',', skip_header=1050, usecols=(2))

data_list = [cm70, cm67, cm64, cm61, cm58, cm55, cm52, cm49, cm46, cm43, cm40, cm37, cm34, cm31, cm28, cm25, cm22, cm19, cm16, cm13, cm10]
messdistanz = [70, 67, 64, 61, 58, 55, 52, 49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10]

data_mean = []
data_std = []
count = 0


for i in data_list:
    data_mean_lokal = np.mean(i, dtype=float)
    data_std_lokal = np.std(i, dtype=float)
    
    count = count +1
    #file_mean.write("%d. Mean: %1.5f\n" % (count, data_mean) )
    #file_std.write("%d. std: %1.5f\n" % (count, data_std) )
    
    data_mean.append(data_mean_lokal)
    data_std.append(data_std_lokal)
    

# PLOT
fig, ax = plt.subplots()

ax.plot(messdistanz[:], data_mean[:])
ax.set_xlabel('Abstand cm')
ax.set_ylabel('Spannung in v')
ax.set_title('Kennlinie')
show()
