import matplotlib.pyplot as plt
import matplotlib.style

# Use the 'ggplot' style
plt.style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'green',label='Line1',linewidth=5)
plt.plot(x2,y2,'blue',label='Line2',linewidth=5)
plt.legend()  # This will show the labels of the lines

plt.grid(True,color='red')

plt.show()