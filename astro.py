import numpy as np
data = np.loadtxt("A2550_data.txt", delimiter=',')

#print(data)

max_value=data.max()
print(max_value)

index = np.where(data == max_value)
print(index)

center_x, center_y = index
center_x = int(center_x)
center_y = int(center_y)

print(center_x,center_y)

r = 10
total = 0.0
pixels = 0

for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        if (x-center_x)**2.0 + (y-center_y)**2.0 <= r**2.0:
            total += data[x,y]
            pixels += 1

print("total",total)
print("pixels",pixels)
print("surface brightness",total/pixels)