import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

  t1, rv1, e1 = np.loadtxt('hd_46052_RV_c1.dat').T
  t2, rv2, e2 = np.loadtxt('hd_46052_RV_c2.dat').T
  period = 2.525
  t0 = 2459800.535

  ph1 = ( (t1-t0)/period ) % 1.
  ph2 = ( (t2-t0)/period ) % 1.


  fig, ax = plt.subplots(1,1, figsize=(6,6))

  ax.errorbar(ph1,rv1,yerr=e1,linestyle='',color='dodgerblue')
  ax.errorbar(ph2,rv2,yerr=e2,linestyle='',color='darkorange')
  ax.set_ylabel(r'${\rm Radial~Velocity~[km\,s^{-1}]}$',fontsize=18)
  ax.set_xlabel(r'${\rm Phase}$',fontsize=18)

  fig.tight_layout()
  plt.show()
