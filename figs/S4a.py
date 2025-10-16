from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams,rc
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FixedLocator,LogLocator
import numpy as np
from matplotlib.lines import Line2D
from scipy import optimize
import matplotlib.ticker as ticker

def func(x,a,b,c):
    return a*(x-b)**2+c

x_data = np.array([0.45,0.46,0.47,0.48,0.49,0.5,0.51])
y_data = np.array([0.48442998445754615, 0.5318481974136298, 0.5602193076722966, 0.5382667559108424, 0.5250268014743729, 0.5019138087101792, 0.46368327470821524])  # Replace this with your actual data.txt points
er=[0.010383306142541831, 0.00575139411977279, 0.007524370747665283, 0.010017556504998923, 0.011823055944416634, 0.009320994474452443, 0.009224446987063466]


color_list=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#7f7f7f', '#bcbd22', '#17becf']
# marker_list=['o','p','s','D','v','^']
# s_list=[55,75,50,50,60,60]
rcParams["font.family"] = "Times New Roman"
rcParams["font.weight"] = "bold"
rcParams["mathtext.fontset"] = 'stix'

fig,ax=plt.subplots(figsize=(7.5, 6.5))

x2=np.linspace(0.45,0.51,num=100)
L=[1,2**(1/3),4**(1/3),8**(1/3)]



popt, pcov = optimize.curve_fit(func,x_data[:],y_data[:],maxfev=100000,p0=[1,0.48,1],sigma=[0.010383306142541831, 0.00575139411977279, 0.007524370747665283, 0.010017556504998923, 0.011823055944416634, 0.009320994474452443, 0.009224446987063466],absolute_sigma=True)

print(np.sqrt(np.diag(pcov)))

for axis in [ 'bottom', 'left']:
    ax.spines[axis].set_linewidth(2.5)
for axis in [ 'top', 'right']:
    ax.spines[axis].set_linewidth(0)

ax.errorbar(x_data,y_data,yerr=er,linestyle='',marker='o',mfc='w',markersize=7.5,)
ax.plot(x2,popt[0]*(x2-popt[1])**2+popt[2],label='$1/\\nu=1.168 \pm 0.154$',linestyle='--',linewidth=2)

print(popt)
# Add legend to the plot
# ax.legend(handles=legend_handles, loc='best',frameon=False,fontsize='18')


# ax.set_xticks([16,17,18,19,20,21,22])
ax.set_xlabel('$\langle \phi \\rangle$',fontsize=30)
ax.set_ylabel('$\langle \Delta \\rho^2 \\rangle^2/\langle \Delta \\rho^4 \\rangle$',fontsize=30)
ax.tick_params(axis='both', which='major', labelsize=25)
ax.tick_params(axis='both', which='minor', labelsize=25)
ax.tick_params(axis='both', which='minor', width=2.5,length=3.5)
ax.tick_params(axis='both', which='major', width=2.5,length=7)

ax.set_xticks([0.45,0.48,0.51])
ax.set_yticks([0.45,0.5,0.55])
# ax.legend(fontsize='15',frameon=False)
# plt.legend(loc='lower left',fontsize='15',frameon=False)
plt.savefig('hh.png',dpi=600,bbox_inches='tight')
plt.show()