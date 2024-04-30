import matplotlib.pyplot as plt
ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]
bins = [0, 20, 40, 60, 80, 100, 120, 140]  #ranges
plt.hist(ages, bins, histtype='bar', rwidth=0.9)

plt.show()