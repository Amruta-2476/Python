import matplotlib.pyplot as plt
slices = [7, 2, 2, 13]   # sizes of each slice of the pie (in percentage)
# 7+2+2=13=24
# 7/24= 29.16%
# 2/24= 8.33%
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices, labels=activities, colors=cols, startangle=90, shadow=True, autopct='%.0f%%')

plt.title('Pie Chart')
plt.show()