import numpy as np
import scipy.integrate
from xkcdify import *
import matplotlib.pyplot as plt

#def gauss(a, mu, sigma, x):
 #       return a*np.exp(-1*((x - mu)**2)/(2*sigma**2))


#parameters of the first bimodal Gaussian distribution
size = 1000
a1 = 10
mu1 = 8
sigma1 = 2

a2 = 13
mu2 = 22
sigma2 = 5 

#the second distribution
a3 = 5
mu3 = 10
sigma3 = 3

a4 = 7
mu4 = 18
sigma4 = 2

#the third distribution

a5 = 3
mu5 = 3
sigma5 = 1

def funct(x):
	ret = np.exp(x * -0.2)
	print ret
	return ret

fig = plt.figure(figsize = (12, 12))
l = np.linspace(0, 30, size)

#flux profile

flux = funct(l)/np.max(funct(l))

ax1 = fig.add_subplot(311)
ax1.plot(l, flux, 'b', lw=1)
ax1.set_axis_off()
#ax1.text(mu1-2, -3, "Body hair")
#ax1.text(mu2-4, -3, "Scalp hair")

ax1.set_title('Exponential flux profile')
#ax1.text(mu1+1, 16, "People with uncut hair")

ax1.set_xlabel('distance from the center')
ax1.set_ylabel('Counts')
#ax1.set_xlim(0, 26)
ax1.set_ylim(0, 1)

#xkcdify
XKCDify(ax1, xaxis_loc=0.0, yaxis_loc=0.0,
        xaxis_arrow='+-', yaxis_arrow='+-',
        expand_axes=False)

ax2 = fig.add_subplot(312)
		
		
ax2.plot(l, np.cumsum(flux)/np.max(np.cumsum(flux)), 'b', lw=1)
ax2.set_axis_off()
#ax1.text(mu1-2, -3, "Body hair")
#ax1.text(mu2-4, -3, "Scalp hair")

ax2.set_title('Cumulative flux profile')
#ax1.text(mu1+1, 16, "People with uncut hair")

ax2.set_xlabel('Distance from the center')
ax2.set_ylabel('Cumulative counts')
ax2.set_ylim(0, 1)

#xkcdify
XKCDify(ax2, xaxis_loc=0.0, yaxis_loc=0.0,
        xaxis_arrow='+-', yaxis_arrow='+-',
        expand_axes=False)

plt.savefig('flux_profile', bbox_inches='tight')
