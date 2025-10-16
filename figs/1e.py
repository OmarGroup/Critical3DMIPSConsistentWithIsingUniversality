from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams,rc
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FixedLocator,LogLocator
import numpy as np
from matplotlib.lines import Line2D

y1=[2.547388099527962, 2.920959356844363, 3.2822299467440303, 4.1456666900192936, 4.938405408934112, 6.298723851196781, 8.33638893456119, 11.504460937832587, 14.37626926203257, 18.331938410941632, 21.5991163361467, 24.621868229141747, 28.121059727135354]
y2=[3.325004346010587, 3.76555320964492, 4.351887888918184, 5.29259103487094, 6.765809377914929, 9.355189954357991, 13.728246306192142, 20.570452512567357, 28.301809097277065, 36.02318609192518, 42.90993191706306, 49.61354807919836, 56.767294088322636]
y3=[4.209551575224475, 4.86217706475674, 5.706151429865441, 6.792751453499723, 9.23344975913407, 13.813862241485703, 23.251475515472134, 39.06381783884915, 55.468374746440944, 71.02222138655654, 84.2208079103535, 98.53183613436167, 110.91201619524682]
y4=[5.112168118913458, 6.085037965984435, 6.890076442191448, 9.230255905394477, 12.793132786150045, 18.566727621542988, 34.502410893413455, 75.04643207780033, 107.18056794380679, 137.77984983470634, 169.17979950602535, 197.05207042594046, 218.67783063906973]

err1=[0.03237159539002412, 0.037520213859332255, 0.040070190907777005, 0.08022876202930068, 0.11772242629837126, 0.11961038054426988, 0.15838668457584432, 0.19075767570590255, 0.22994910750120082, 0.15768759313771966, 0.18461560245010145, 0.19120152056204565, 0.15706726576476768]
err2=[0.041070299541561106, 0.054342523357214526, 0.08260926618775925, 0.12236918363573786, 0.16767277743825373, 0.25696170302320837, 0.4052037895119947, 0.4119815061566315, 0.35828122704047166, 0.35909455425118564, 0.31814806819837255, 0.3909051431703199, 0.26311351825083157]
err3=[0.0645425490104094, 0.06290515595416045, 0.13705666870083924, 0.1380267869251595, 0.30677632471729904, 0.5206263372576746, 0.7949263359028709, 0.8771349153452935, 1.1060054240237815, 0.7011671059490474, 0.5871892637225634, 0.6527103537982217, 0.580367594949138]
err4=[0.08077810395805557, 0.09479360405194547, 0.11912128744596252, 0.28754421708543015, 0.5044632622470945, 0.8540764482952897, 1.6502557168074414, 2.0746601617170213, 1.3167811064714796, 1.2838412833720467, 1.0738927653131072, 1.1073671278667239, 1.605620176978618]

x11=np.linspace(16,22,num=13)

x1=[(i-18.9)*(1**(1/3))**(1/0.629971) for i in x11]
x2=[(i-18.9)*(2**(1/3))**(1/0.629971) for i in x11]
x3=[(i-18.9)*(4**(1/3))**(1/0.629971) for i in x11]
x4=[(i-18.9)*(8**(1/3))**(1/0.629971) for i in x11]

y2=[i*(2**(1/3))**(-1.96370) for i in y2]
y3=[i*(4**(1/3))**(-1.96370) for i in y3]
y4=[i*(8**(1/3))**(-1.96370) for i in y4]

err2=[i*(2**(1/3))**(-1.96370) for i in err2]
err3=[i*(4**(1/3))**(-1.96370) for i in err3]
err4=[i*(8**(1/3))**(-1.96370) for i in err4]

x=[x1,x2,x3,x4]

y=[y1,y2,y3,y4]
err=[err1,err2,err3,err4]
marker_list=['o','D','s','^','p']
s_list=[6.5,5.5,5.5,6.5]

labels=['$N=16000$','$N=32000$','$N=64000$','$N=128000$','$0.04$','$0.05$']

color_list=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#7f7f7f', '#bcbd22', '#17becf']
# marker_list=['o','p','s','D','v','^']
# s_list=[55,75,50,50,60,60]
rcParams["font.family"] = "Times New Roman"
rcParams["font.weight"] = "bold"
rcParams["mathtext.fontset"] = 'stix'

fig,ax=plt.subplots(figsize=(7.5, 6.5))

for i in range(4):
    ax.errorbar(x[i],y[i],yerr=np.array(err[i]),linestyle='',marker=marker_list[i],mfc='w',markersize=s_list[i],linewidth=0.75,markeredgewidth=1.5,elinewidth=1.5,color=color_list[i],capsize=3)



for axis in [ 'bottom', 'left']:
    ax.spines[axis].set_linewidth(2.5)
for axis in [ 'top', 'right']:
    ax.spines[axis].set_linewidth(0)


# ax.yaxis.set_minor_locator(FixedLocator([k*10 for k in range(2,19)]))

# ax.yaxis.set_major_locator(FixedLocator([20,50,100,150]))
# ax.get_yaxis().set_major_formatter(ticker.ScalarFormatter())
# ax.set_yticks([20,50,100,150])
# ax.get_yaxis().get_major_formatter().labelOnlyBase = False
ax.set_yscale('log')
# ax.set_xlim(0.,0.645)
# ax.set_ylim(17.5,190)
# plt.gca().set_yticklabels(minor='off',labels=['','','','','','','','','','','','','','','','',''])
ax.set_xticks([-9,-6,-3,0,3,6,9])
ax.set_xlabel('$\left( \ell_0/\sigma-\ell_{\\rm c}/\sigma \\right) L^{1/\\nu}$',fontsize=30)
ax.set_ylabel('$\chi L^{-\gamma/\\nu}$',fontsize=30)
ax.tick_params(axis='both', which='major', labelsize=25)
ax.tick_params(axis='both', which='minor', width=2.5,length=3.5)
ax.tick_params(axis='both', which='major', width=2.5,length=7)
# ax.set_xticks([0.0,0.1,0.2,0.3,0.4,0.5,0.6])


# plt.legend(loc='lower left',fontsize='15',frameon=False)
# plt.savefig('hh.png',dpi=600,bbox_inches='tight')
plt.show()