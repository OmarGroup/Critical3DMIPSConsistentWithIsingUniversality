from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams,rc
from matplotlib.ticker import FixedLocator,FixedFormatter,NullLocator,NullFormatter
import numpy as np
from matplotlib.lines import Line2D
from scipy import optimize
import matplotlib.ticker as ticker

def func(x,a,b):
    return a*x+b

lx=np.array([0.6,1.1,1.6,2.1])/18.9
values=[[0.12948066791407467, 0.14850298129091094, 0.17277958914544764, 0.18876120351427272],[0.124583243016213, 0.15185181077078802, 0.17427212021340563, 0.1913177583101941],[0.12442152280728036, 0.15212724126436628, 0.17462873372951315, 0.19097992020418636],[0.12438399461141443, 0.15227426386384108, 0.1733214759790634, 0.19274450098973167]]
err=[0.0024101536558973815, 0.0011571681826864364, 0.0009819617330979458, 0.000677355683523807]

color_list=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#7f7f7f', '#bcbd22', '#17becf']
# marker_list=['o','p','s','D','v','^']
# s_list=[55,75,50,50,60,60]
rcParams["font.family"] = "Times New Roman"
rcParams["font.weight"] = "bold"
rcParams["mathtext.fontset"] = 'stix'

fig,ax=plt.subplots(figsize=(7.5, 6.5))

x2=np.linspace(0.03,0.12,num=100)
L=[1,2**(1/3),4**(1/3),8**(1/3)]

log_uncertainties=5

# popt, pcov = optimize.curve_fit(func,np.log(L[:]),np.log(values[:]),maxfev=10000,sigma=[log_uncertainties]*4)
popt=[[0.30418487206020955, -1.9041614046127762],[0.34348048618674004, -1.910536207079835],[0.3438525003273855, -1.910412767945565],[0.3473309502787693, -0.8896565926462812]]
# print(np.sqrt(np.diag(pcov)))
error=[0.02828727,0.00617901,0.0051536,0.0076824 ]

for axis in [ 'bottom', 'left']:
    ax.spines[axis].set_linewidth(2.5)
for axis in [ 'top', 'right']:
    ax.spines[axis].set_linewidth(0)

# ax.errorbar(L,values,yerr=err,linestyle='',marker='o',mfc='w',markersize=5,)
# for i in range(4):
ax.errorbar(lx,values[3],yerr=err,marker='o',mfc='w',elinewidth=2,markeredgewidth=2,linestyle='',markersize=10,capsize=7,)
ax.plot(x2,np.exp(popt[3][0]*np.log(x2)+popt[3][1]),label='$\\beta={0:.3f} \pm {1:.3f}$'.format(popt[3][0],error[3]),linewidth=2,linestyle='--')
# ax.plot(x2,np.exp(-0.5181492481399939*np.log(x2)-2.05),label='$\\beta/\\nu=0.518$',linestyle='-')

print(popt)
# Add legend to the plot
# ax.legend(handles=legend_handles, loc='best',frameon=False,fontsize='18')

# ax.yaxis.set_minor_locator(FixedLocator([k*10 for k in range(2,19)]))

# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
# ax.get_yaxis().set_major_formatter(ticker.ScalarFormatter())
# ax.set_yticks([20,50,100,150])
# ax.get_yaxis().get_major_formatter().labelOnlyBase = False
ax.set_xscale('log')
ax.set_yscale('log')
# ax.xaxis.set_major_locator(FixedLocator([1,10]))
# ax.yaxis.set_major_locator(FixedLocator([0.1]))
# ax.set_ylim(0.1,0.27)
# ax.set_xlim(0.,0.645)
# ax.set_ylim(17.5,190)
# plt.gca().set_yticklabels(minor='off',labels=['','0.12','','','','0.16','','','','0.20'])
# plt.gca().set_xticklabels(minor='off',labels=['','','','',''])
# plt.ylim(0.15,0.28)
# ax.set_xticks([16,17,18,19,20,21,22])
ax.set_xlabel('$\lambda$',fontsize=32)
ax.set_ylabel('$m$',fontsize=32)
ax.tick_params(axis='both', which='major', labelsize=28)
# ax.tick_params(axis='both', which='minor', labelsize=25)
ax.tick_params(axis='both', which='minor', width=2.5,length=3.5)
ax.tick_params(axis='both', which='major', width=2.5,length=7)
ax.yaxis.set_major_locator(FixedLocator([0.12,0.16,0.2]))
ax.yaxis.set_major_formatter(FixedFormatter(['0.12','0.16','0.20']))
ax.yaxis.set_minor_locator(FixedLocator([0.13,0.14,0.15,0.17,0.18,0.19]))
ax.yaxis.set_minor_formatter(NullFormatter())
ax.xaxis.set_major_locator(FixedLocator([0.03,0.1]))
ax.xaxis.set_major_formatter(FixedFormatter(['0.03','0.1']))
ax.xaxis.set_minor_locator(FixedLocator([0.04,0.05,0.06,0.07,0.08,0.09]))
ax.xaxis.set_minor_formatter(NullFormatter())

ax.legend(fontsize='23',frameon=False)
# plt.legend(loc='lower left',fontsize='15',frameon=False)
plt.savefig('hh.png',dpi=600,bbox_inches='tight')
plt.show()