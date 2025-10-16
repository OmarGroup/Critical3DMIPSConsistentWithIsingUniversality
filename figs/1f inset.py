from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams,rc
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FixedLocator,LogLocator,NullLocator
import numpy as np
from matplotlib.lines import Line2D
from scipy import optimize
import matplotlib.ticker as ticker

'''
def func(x,A1,A2,A3,A4,w,theta,x0):
    return A1+A2/(A3+A4*np.exp(-(x-x0)/w))**(1/theta)

def derivative_func(x1, A1, A2, A3, A4, w, theta, x0):
    h = 1e-5  # A small step size for numerical differentiation
    # Use central difference method to compute the derivative
    derivative = (func(x1 + h, A1, A2, A3, A4, w, theta, x0) - func(x1 - h, A1, A2, A3, A4, w, theta, x0)) / (2 * h)
    return derivative
'''
def func(x,a,b):
    return a*x+b

values=[0.09765107054809519,0.08748915502942244,0.07971215987653181,0.06563106702273855]
err=[0.001569782913353199,0.0021563298137379184,0.0023958629227493386,0.002942488933306096]

color_list=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#7f7f7f', '#bcbd22', '#17becf']
# marker_list=['o','p','s','D','v','^']
# s_list=[55,75,50,50,60,60]
rcParams["font.family"] = "Times New Roman"
rcParams["font.weight"] = "bold"
rcParams["mathtext.fontset"] = 'stix'

fig,ax=plt.subplots(figsize=(7.5, 6.5))

x2=np.linspace(1,2,num=100)
L=[1,2**(1/3),4**(1/3),8**(1/3)]

log_uncertainties=5

popt, pcov = optimize.curve_fit(func,np.log(L[:]),np.log(values[:]),maxfev=10000,sigma=[log_uncertainties]*4)

print(np.sqrt(np.diag(pcov)))

for axis in [ 'bottom', 'left']:
    ax.spines[axis].set_linewidth(2.5)
for axis in [ 'top', 'right']:
    ax.spines[axis].set_linewidth(0)


ax.plot(x2,np.exp(popt[0]*np.log(x2)+popt[1]),label='$\\beta/\\nu=0.556 \pm 0.068$',linestyle='--',linewidth=3)
ax.plot(x2,np.exp(-0.5181492481399939*np.log(x2)-2.28),label='$\\beta/\\nu=0.518$',linestyle='-',linewidth=3)
ax.errorbar(L,values,yerr=err,linestyle='',marker='o',markersize=10,markeredgewidth=2,mfc='w',capsize=7,linewidth=2)
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
plt.minorticks_off()
# ax.xaxis.set_major_locator(FixedLocator([1,10]))
# ax.yaxis.set_major_locator(FixedLocator([0.1]))
# ax.set_ylim(0.1,0.27)
# ax.set_xlim(0.,0.645)
# ax.set_ylim(17.5,190)
# plt.gca().set_yticklabels(minor='off',labels=['','','','','','','','',''])
# plt.gca().set_xticklabels(minor='off',labels=['','','','','','$2\\times 10^0$'])
ax.yaxis.set_major_locator(NullLocator())

# ax.set_xticks([16,17,18,19,20,21,22])
ax.set_xlabel('$L$',fontsize=45)
ax.set_ylabel('$(\phi_{\\rm liq} -\phi_{\\rm gas})|_{\\ell=\\ell_{\\rm c}}$',fontsize=45)
# ax.tick_params(axis='both', which='major', labelsize=35)
# ax.tick_params(axis='both', which='minor', labelsize=35)
# ax.tick_params(axis='both', which='minor', width=2.5,length=3.5)
# ax.tick_params(axis='both', which='major', width=2.5,length=7)
ax.tick_params(axis='both', which='both',   bottom=False, top=False,labelbottom=False)


ax.legend(fontsize='29',frameon=False,loc='lower left')
# plt.legend(loc='lower left',fontsize='15',frameon=False)
# plt.savefig('hh.png',dpi=600,bbox_inches='tight')
plt.show()