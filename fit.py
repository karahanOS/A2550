from astro2 import sur_bri_list
from astro2 import radius_list
import numpy as np # import numpy to use in our code
import matplotlib.pyplot as plt # import matplotlib to create our plot
from scipy.optimize import curve_fit


y_data = np.asarray(sur_bri_list)
x_data = np.asarray(radius_list)

def beta(r, s0, rc, b):
    return s0 * (1.0 + (r/rc)**2.0)**(-3*b + 0.5)


parameters, covariance = curve_fit(beta, x_data, y_data)

fit_A = parameters[0]
fit_B = parameters[1]

print(fit_A)
print(fit_B)

fit_y = beta(x_data, fit_A, fit_B)
plt.plot(x_data, y_data, 'o', label='data')
plt.plot(x_data, fit_y, '-', label='fit')
plt.legend()