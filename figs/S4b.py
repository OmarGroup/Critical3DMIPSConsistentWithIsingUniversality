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

x_data = np.array([18,18.5,19,19.5])
y_data = np.array([0.4261387886572384, 0.48899519302094185, 0.5961052198972304, 0.7412540852417452])
y_data_2 = np.array([0.42316363482973945, 0.46653028206326297, 0.605773336183246, 0.7877362389085671])
er=np.array([0.005134353647531434, 0.008142954080744563, 0.010803674287261002, 0.011019563392298858])
er2=np.array([0.006211835727926516, 0.0094530388498461, 0.014969051372848282, 0.013306182158984685])


color_list=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#7f7f7f', '#bcbd22', '#17becf']
# marker_list=['o','p','s','D','v','^']
# s_list=[55,75,50,50,60,60]
rcParams["font.family"] = "Times New Roman"
rcParams["font.weight"] = "bold"
rcParams["mathtext.fontset"] = 'stix'

fig,ax=plt.subplots(figsize=(7.5, 6.5))

x2=np.linspace(0.45,0.51,num=100)
L=[1,2**(1/3),4**(1/3),8**(1/3)]


xx=np.arange(18.5,19.005,0.01)
xx2=np.arange(18.,19.5,0.01)
y1=0.20889861333954418*xx-3.38377210784137
y2=0.21954149416561008*xx-3.5643794949621

y3=0.2674540831939617*xx-4.490823295874875
y4=0.28951813328597054*xx-4.8801021448773465


for axis in [ 'bottom', 'left']:
    ax.spines[axis].set_linewidth(2.5)
for axis in [ 'top', 'right']:
    ax.spines[axis].set_linewidth(0)

ax.errorbar(x_data,y_data,yerr=er,marker='o',mfc='w',markersize=7.5,color=color_list[2])
ax.errorbar(x_data,y_data_2,yerr=er2,marker='o',mfc='w',markersize=7.5,color=color_list[3])
ax.errorbar(x_data,y_data,yerr=er,marker='o',mfc='w',markersize=7.5,linestyle='',color=color_list[2])

ax.fill_between(xx,y1,y2,alpha=0.4, color=color_list[2], edgecolor='none')
ax.fill_between(xx,y3,y4,alpha=0.4, color=color_list[3], edgecolor='none')
ax.fill_between(xx2,0.550568779486257,0.577187590208637,alpha=0.3,color='gray', edgecolor='none')
ax.fill_between(xx,0.4,0.550568779486257,where=(xx >= 18.803590185998893) & (xx <= 18.899324401252745),alpha=0.3,color='gray', edgecolor='none')
ax.fill_between(xx,0.577187590208637,0.7,where=(xx >= 18.803590185998893) & (xx <= 18.899324401252745),alpha=0.3,color='gray', edgecolor='none')
# Add legend to the plot
# ax.legend(handles=legend_handles, loc='best',frameon=False,fontsize='18')


# ax.set_xticks([16,17,18,19,20,21,22])
ax.set_xlabel('$\ell_0/\sigma$',fontsize=30)
ax.set_ylabel('$\langle \Delta \\rho^2 \\rangle^2/\langle \Delta \\rho^4 \\rangle$',fontsize=30)
ax.tick_params(axis='both', which='major', labelsize=25)
ax.tick_params(axis='both', which='minor', labelsize=25)
ax.tick_params(axis='both', which='minor', width=2.5,length=3.5)
ax.tick_params(axis='both', which='major', width=2.5,length=7)

plt.xlim(18.3,19.15)
plt.ylim(0.43,0.64)
plt.plot([18,19.5],[0.5638781848474479,0.5638781848474479],color='black')
plt.plot([18.849561072900276,18.849561072900276],[0.4,0.67],color='black')
# ax.set_xticks([0.45,0.48,0.51])
# ax.set_yticks([0.48,0.52,0.56])
# ax.legend(fontsize='15',frameon=False)
# plt.legend(loc='lower left',fontsize='15',frameon=False)
plt.savefig('hh.png',dpi=600,bbox_inches='tight')
plt.show()