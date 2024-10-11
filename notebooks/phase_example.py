import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

  n = 5000
  x = np.linspace(-4,4,n)
  period = 1.5
  t0 = 0.6

  ph = ( (x-t0)/period ) % 1.

  y = 2.1 * np.sin( 2.*np.pi*(1./period)*x + 0.6)
  yerr = np.random.normal(0.,0.1,n)
  y += yerr

  fig, axes = plt.subplots(1,2, figsize=(15,7))

  axes[0].plot([0.2,0.2+period],[2.5,2.5], '-', color='dodgerblue')
  axes[0].errorbar(x,y,yerr=abs(yerr),linestyle='',color='black')
  axes[0].axvline(t0,color='darkorange',ls='--',alpha=0.7)
  axes[0].set_ylabel(r'${\rm Y}$',fontsize=18)
  axes[0].set_xlabel(r'${\rm Time~[d]}$',fontsize=18)


  axes[1].errorbar(ph,y,yerr=abs(yerr),linestyle='',color='black')
  axes[1].set_ylabel(r'${\rm Y}$',fontsize=18)
  axes[1].set_xlabel(r'${\rm Phase}$',fontsize=18)

  fig.tight_layout()
  plt.show()
