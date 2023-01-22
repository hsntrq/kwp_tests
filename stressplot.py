import matplotlib.pyplot as plt
import seaborn as sns

lat = list(map(float,open("latency/100,10,10","r").readline().split(",")))
fig, ax = plt.subplots(2,2)
sns.scatterplot(lat,ax=ax[0,0])
sns.kdeplot(lat,ax=ax[0,1])
sns.boxplot(lat,ax=ax[1,0])
sns.violinplot(lat,ax=ax[1,1])
plt.show()
