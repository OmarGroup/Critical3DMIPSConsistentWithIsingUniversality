from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams,rc
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FixedLocator,LogLocator
import numpy as np
from matplotlib.lines import Line2D
from scipy import optimize
import matplotlib.ticker as ticker



data0=[0.0008002664060001335, 0.0022331577667190593, 0.001919185396111965, 0.003902797893084908, 0.007758211127016543, 0.01114810159682807, 0.007612300649817164, 0.009354554272780594, 0.008675694248944916, 0.0036178979080551976, 0.0033775228711505124, 0.0021838082080346023, 0.003945491800197733]
data1=[0.0015117336721393185, 0.0024375120162349277, 0.003233506203040711, 0.003988910735743929, 0.005679802417057879, 0.010038107308045172, 0.008964926207017982, 0.009035157384981557, 0.010606960143425492, 0.00447224649272, 0.0028325926370423673, 0.0030871134206465214, 0.002735329511326811]
data2=[0.00220204299851086, 0.0022674661780627266, 0.0035267376550114863, 0.003423188110738138, 0.006249353618730278, 0.008256221623499056, 0.011556411061327196, 0.010252515782666574, 0.012696581327679736, 0.0042180678144618676, 0.002927967231132341, 0.002871025963048316, 0.0022850866921936335]
data3=[0.002102986620042608, 0.002242720903379983, 0.0028838673359824806, 0.0034578727630447796, 0.005134353647531434, 0.008142954080744563, 0.010803674287261002, 0.011019563392298858, 0.012073831549180198, 0.004489860623601853, 0.0028163449562093766, 0.002994820693707762, 0.0024252331478455723]


datas=[data0,data1,data2,data3]

x=np.linspace(16,22,num=13)


color_list=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#7f7f7f', '#bcbd22', '#17becf']
# marker_list=['o','p','s','D','v','^']
# s_list=[55,75,50,50,60,60]
rcParams["font.family"] = "Times New Roman"
rcParams["font.weight"] = "bold"
rcParams["mathtext.fontset"] = 'stix'

fig,ax=plt.subplots(figsize=(7.5, 6.5))

tau=[5,10,20,40]

marker_list=['o','p','s','D','v','^']
labels=[15,16,17,18,19,20]

for axis in [ 'bottom', 'left']:
    ax.spines[axis].set_linewidth(2.5)
for axis in [ 'top', 'right']:
    ax.spines[axis].set_linewidth(0)

for i in range(4):
    ax.plot(x, datas[i],linestyle='--')
    ax.scatter(x,datas[i],label='$n$='+str(tau[i]),s=40,marker=marker_list[i])

# Add legend to the plot
# ax.legend(handles=legend_handles, loc='best',frameon=False,fontsize='18')

# ax.yaxis.set_minor_locator(FixedLocator([k*10 for k in range(2,19)]))

# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
# ax.get_yaxis().set_major_formatter(ticker.ScalarFormatter())
# ax.set_yticks([20,50,100,150])
# ax.get_yaxis().get_major_formatter().labelOnlyBase = False
# ax.set_xscale('log')
# ax.set_yscale('log')
# ax.xaxis.set_major_locator(FixedLocator([1,10]))
# ax.yaxis.set_major_locator(FixedLocator([0.1]))
# ax.set_ylim(0.1,0.27)
# ax.set_xlim(0.,0.645)
# ax.set_ylim(17.5,190)
# plt.gca().set_yticklabels(minor='off',labels=['0.12','','','','0.2','','','','0.28'])
# plt.gca().set_xticklabels(minor='off',labels=['','','1.4','','1.8'])

# ax.set_xticks([16,17,18,19,20,21,22])
plt.yticks([0,0.004,0.008,0.012])
plt.xticks([16,17,18,19,20,21,22])
ax.set_xlabel('$\ell_0/\sigma$',fontsize=30)
ax.set_ylabel('$\sigma$',fontsize=30)

# ax.set_yscale('log')
ax.tick_params(axis='both', which='major', labelsize=25)
# ax.tick_params(axis='both', which='minor', labelsize=25)
ax.tick_params(axis='both', which='minor', width=2.5,length=3.5)
ax.tick_params(axis='both', which='major', width=2.5,length=7)

# ax.set_ylim(0.01,1)
# ax.set_xlim(0,75)
# ax.set_xticks([0.45,0.48,0.51])
# ax.set_yticks([0.48,0.52,0.56])
ax.legend(fontsize='17',frameon=False)
# plt.legend(loc='lower left',fontsize='15',frameon=False)
plt.savefig('hh.png',dpi=600,bbox_inches='tight')
plt.show()