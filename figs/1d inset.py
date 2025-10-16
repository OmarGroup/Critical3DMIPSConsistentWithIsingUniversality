from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams,rc
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FixedLocator,LogLocator
import numpy as np
from matplotlib.lines import Line2D
from scipy import optimize
import matplotlib.ticker as ticker


def func(x,a,b):
    return a*x+b

values=[0.1245149974889781,0.1737496617907106,0.24162233216482587,0.30411801740316813]
err=[0.0169513,0.01604536,0.02196173,0.02466432]

color_list=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#7f7f7f', '#bcbd22', '#17becf']
# marker_list=['o','p','s','D','v','^']
# s_list=[55,75,50,50,60,60]
rcParams["font.family"] = "Times New Roman"
rcParams["font.weight"] = "bold"
rcParams["mathtext.fontset"] = 'stix'

fig,ax=plt.subplots(figsize=(7.5, 6.5))

x2=np.linspace(1,2,num=100)
L=[1,2**(1/3),4**(1/3),8**(1/3)]


popt, pcov = optimize.curve_fit(func,np.log(L[:]),np.log(values[:]),maxfev=10000)

print(np.sqrt(np.diag(pcov)))

for axis in [ 'bottom', 'left']:
    ax.spines[axis].set_linewidth(2.5)
for axis in [ 'top', 'right']:
    ax.spines[axis].set_linewidth(0)


ax.plot(x2,np.exp(popt[0]*np.log(x2)+popt[1]),label='$1/\\nu=1.302 \pm 0.076$',linestyle='--',linewidth=3)
ax.plot(x2,np.exp(1.5873746569286524*np.log(x2)-2.14),label='$1/\\nu=1.587$',linestyle='-',linewidth=3)
ax.errorbar(L,values,yerr=err,linestyle='',marker='o',mfc='w',markersize=10,markeredgewidth=2,capsize=7,linewidth=2)
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
# plt.gca().set_yticklabels(minor='off',labels=['','','','','','','','',''])
# plt.gca().set_xticklabels(minor='off',labels=['','','','','','$2\\times 10^0$'])
plt.minorticks_off()
# ax.set_xticks([16,17,18,19,20,21,22])
ax.set_xlabel('$L$',fontsize=45)
ax.set_ylabel('$\partial_{\\ell} B|_{\\ell=\\ell_{\\rm c}}$',fontsize=45)
ax.tick_params(axis='both', which='both',   bottom=False, top=False,labelbottom=False)
# ax.tick_params(axis='both', which='minor', labelsize=35)
# ax.tick_params(axis='both', which='minor', width=2.5,length=3.5)
# ax.tick_params(axis='both', which='major', width=2.5,length=7)


ax.legend(fontsize='30',frameon=False,loc='upper left')
# plt.legend(loc='lower left',fontsize='15',frameon=False)
# plt.savefig('hh.png',dpi=600,bbox_inches='tight')
plt.show()