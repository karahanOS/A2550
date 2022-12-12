"""
The named A2550_data.txt file contains x-ray observation datas of a galaxy called A2550.
This data is a two dimensional tableau and every value in the tableau
gives us that how many fotons have hit exact pixel on the observation camera.
"""
import numpy as np # import numpy to use in our code
import matplotlib.pyplot as plt # import matplotlib to create our plot

data = np.loadtxt("A2550_data.txt", delimiter=',')

total = 0.0             #Gives us sum of the the number of fotons
pixels = 0              # Gives how many pixels are there
sur_bri = 0             # Surface Brigthness
sur_bri_list = []       # This list is for surface brightness of certian intervals
radius_list = []        
radius_error_list = []  # This is the probable error we might get when we calculate
sur_bri_error_list = [] #

def galaxy(center_x, center_y, r1, r2): 
    # center_x and center_y are selected coordinates.
    # r1 and r2 are our radiuses to create intervals
    
    global sur_bri ; 0
    global total ; 0.0
    global pixels ; 0

    for x in range(data.shape[0]): # data.shape[0] gives the information of x coordinates which means zeroth index of the data  
        for y in range(data.shape[1]): # data.shape[1] gives the information of y coordinates which means 1 index of the data 
            if (x-center_x)**2.0 + (y-center_y)**2.0 > r1**2.0 and (x-center_x)**2.0 + (y-center_y)**2.0 <= r2**2.0: # Here we create our interval 
                total += data[x,y] # This part is about summation of obtained foton one by one 
                pixels += 1 # Here, we obtain how many pixels are there in the data
    
    sur_bri = total/pixels

    return total, pixels, sur_bri

n=1 # n is the determınes thıckness of ınterval
for i in range(0, 100, n):
    total, pixels, sur_bri = galaxy(74, 76, i, i+n) # calling galaxy func 

    radius_list.append((i + i+n)/2.0)
    radius_error_list.append(n/2)

    sur_bri_list.append(sur_bri)
    sur_bri_error_list.append(total**0.5 / pixels)

print(sur_bri_list)
print(sur_bri_error_list)
print(radius_list)
print(radius_error_list)


"""
.errorbar(x axis, y axis, error of x axis, error of surface brightness, fmt changes which sign you use, size of the sing) 
"log" statement makes our scale logarithmic
.show prints our plot 
"""
plt.errorbar(radius_list, sur_bri_list, xerr=radius_error_list, yerr=sur_bri_error_list, fmt=".", ms=0.1)
plt.xscale("log")
plt.yscale("log")
plt.show()

