from astro2 import sur_bri_list
from astro2 import radius_list
import numpy as np # import numpy to use in our code
import matplotlib.pyplot as plt # import matplotlib to create our plot
from scipy.optimize import curve_fit


y_data = np.asarray(sur_bri_list)
x_data = np.asarray(radius_list)

def beta(r, s0, rc, b, c):
    return s0 * (1.0 + (r/rc)**2.0)**(-3*b + 0.5) + c


parameters, covariance = curve_fit(beta, x_data, y_data)

fit_s0 = parameters[0]
fit_rc= parameters[1]
fit_b = parameters[2]
fit_c = parameters[3]

print(fit_rc)
print(fit_s0)
print(fit_b)
print(fit_c)

fit_y = beta(x_data, fit_s0, fit_rc, fit_b, fit_c)
plt.plot(x_data, y_data, 'o', label='data')
plt.plot(x_data, fit_y, '-', label='fit')
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.show()