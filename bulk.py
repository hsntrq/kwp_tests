import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.rc('font', size=12)
plt.rc('axes', titlesize=15)     # fontsize of the axes title
plt.rc('axes', labelsize=15)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=15)    # fontsize of the tick labels
plt.rc('ytick', labelsize=15)    # fontsize of the tick labels

def f(r):
    return datetime.strptime(r[:16], "%Y-%m-%d %H:%M")

def g(r):
    return str(r)

df = pd.read_csv(f'files\{22},02.csv', sep=',')
df['t'] = df.apply(lambda r: f(r["time_received"]), axis=1)
df['ti'] = df.apply(lambda r: g(r["time_sampled"]), axis=1)
#print(df["t"].value_counts()[:15])
df = df[df["t"].between(datetime(2022,2,17,8,9), datetime(2022,2,17,8,12) )]
df = df[df["node"]=="ahsan-ali"]
print(df['ti'].min(), df['ti'].max())
print(df['time_received'].min(), df['time_received'].max())
dff = df["time_received"].value_counts().rename_axis('time_received').reset_index(name='counts')
# dff['time_received'] = df.apply(lambda r: g(r["t"]), axis=1)
print(dff)
print(df)
dff.plot(kind='scatter', x='time_received', y= 'counts', color="red")

num_labels = 20
ticks = [t for t in range(len(dff)) if t % num_labels == 0]
labels = [l[11:19] for i, l in enumerate(dff['time_received']) if i % num_labels == 0]
# print(labels)
plt.xlabel("Time Received")
plt.ylabel("Number of Samples per Request")
plt.xticks(ticks, labels, rotation=0)
plt.show()
