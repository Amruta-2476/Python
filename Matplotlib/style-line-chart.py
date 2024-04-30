import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]
z = [1,8,27,64,125]

plt.plot(x,y,color='red',marker='o',markersize=10,label='Line1')
plt.plot(x,z,color='blue',marker='o',markersize=10,label='Line2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.grid(True)
plt.legend()  # This will show the labels of the lines

plt.show()