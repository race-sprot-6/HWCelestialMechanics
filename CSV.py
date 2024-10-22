import csv
import matplotlib.pyplot as plt

x, y = [], []
with open('C:/Users/ivank/Documents/light_curve_404c05f5-3ba6-4f3c-a664-5f08059d69b6.csv') as File:
    lines = csv.reader(File, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(row[5])

xt = []
yt = []
for i in range(1,8):
    xt.append(x[i*100])
for i in range(1,8):
    yt.append(y[i*100])


plt.scatter(x, y, color='g', label="///", s = 5)

plt.xticks(xt, rotation = 45)
#plt.yticks(yt)
plt.ylim (17, 13.5)
plt.gca().invert_yaxis()
#plt.xlabel('Dates')
#plt.ylabel('Temperature(°C)')
#plt.title('Weather Report', fontsize=20)
#plt.grid()
#plt.legend()
plt.show()