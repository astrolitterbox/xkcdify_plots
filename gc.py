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
	ret = 22*np.exp(x * -0.2)
	print ret
	return ret

fig = plt.figure(figsize = (16, 12))
l = np.linspace(0, 30, size)

#flux profile

func = 22*np.exp(l * -0.2)

ax1 = fig.add_subplot(311)
ax1.plot(l, funct(l), 'b', lw=1)
ax1.set_axis_off()
#ax1.text(mu1-2, -3, "Body hair")
#ax1.text(mu2-4, -3, "Scalp hair")

ax1.set_title('Exponential flux profile')
#ax1.text(mu1+1, 16, "People with uncut hair")

ax1.set_xlabel('distance from the center')
ax1.set_ylabel('Counts')
#ax1.set_xlim(0, 26)
ax1.set_ylim(0, 20)

#xkcdify
XKCDify(ax1, xaxis_loc=0.0, yaxis_loc=0.0,
        xaxis_arrow='+-', yaxis_arrow='+-',
        expand_axes=False)

ax2 = fig.add_subplot(312)
def cumf(l):
	return scipy.integrate.quad(lambda x: funct(x), l, l+1)

cf = np.empty((l.shape))
for i, x in enumerate(l):
	print i, 'i'
	cf[i] = cumf(x)[0]
	
print cf		
ax2.plot(l, cf, 'b', lw=1)
ax2.set_axis_off()
#ax1.text(mu1-2, -3, "Body hair")
#ax1.text(mu2-4, -3, "Scalp hair")

ax2.set_title('Cumulative flux profile')
#ax1.text(mu1+1, 16, "People with uncut hair")

ax2.set_xlabel('distance from the center')
ax2.set_ylabel('Total counts inside the given ellipse')
ax2.set_ylim(0, 20)

#xkcdify
XKCDify(ax2, xaxis_loc=0.0, yaxis_loc=0.0,
        xaxis_arrow='+-', yaxis_arrow='+-',
        expand_axes=False)

plt.savefig('flux_profile')
