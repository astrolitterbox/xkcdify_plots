import numpy as np
from xkcdify import *
import matplotlib.pyplot as plt
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
fig = plt.figure(figsize = (16, 12))
l = np.linspace(0, 30, size)
def gauss(a, mu, sigma, x):
	return a*np.exp(-1*((x - mu)**2)/(2*sigma**2))

ax1 = fig.add_subplot(311)
ax1.plot(l, gauss(a1, mu1, sigma1, l) + gauss(a2, mu2, sigma2, l), 'b', lw=1)
ax1.set_axis_off()
ax1.text(mu1-2, -3, "Body hair")
ax1.text(mu2-4, -3, "Scalp hair")

ax1.set_title('Hair length distribution in humans')
ax1.text(mu1+1, 16, "People with uncut hair")

ax1.set_xlabel('Hair length')
ax1.set_ylabel('Hair amount')
#ax1.set_xlim(0, 26)
ax1.set_ylim(0, 20)
XKCDify(ax1, xaxis_loc=0.0, yaxis_loc=0.0,
        xaxis_arrow='+-', yaxis_arrow='+-',
        expand_axes=False)



ax2 = fig.add_subplot(312)

ax2.plot(l, gauss(a3, mu3, sigma3, l) + gauss(a4, mu4, sigma4, l), 'k', lw=1)
ax2.set_title("People with short haircuts")
ax2.set_xlabel('Hair length')
ax2.set_ylabel('Hair amount')
ax2.set_axis_off()
ax2.text(mu1-2, -1.2, "Body hair")
ax2.text(mu2-4, -1.2, "Scalp hair")

XKCDify(ax2, xaxis_loc=0.0, yaxis_loc=0.0,
        xaxis_arrow='+-', yaxis_arrow='+-',
        expand_axes=False)



ax3 = fig.add_subplot(313)

ax3.plot(l, gauss(a3, mu3, sigma3, l) + gauss(a4, mu4, sigma4, l) + gauss(a5, mu5, sigma5, l), 'r', lw=1)
ax3.set_title('Truck drivers')
ax3.set_xlabel('Hair length')
ax3.set_ylabel('Hair amount')
ax3.set_axis_off()
ax3.text(mu1-2, -1.2, "Body hair")
ax3.text(mu2-4, -1.2, "Scalp hair")

ax3.text(3, 5.2, "Finger hair")
ax3.plot([4.3, 3.3], [5, 3.5], '-k', lw=0.5)


XKCDify(ax3, xaxis_loc=0.0, yaxis_loc=0.0,
        xaxis_arrow='+-', yaxis_arrow='+-',
        expand_axes=False)


#ax.set_xlim(0, 30)
#ax.set_ylim(0, 15)

#XKCDify the axes -- this operates in-place
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.9, wspace=None, hspace=0.4)


plt.savefig('x')
