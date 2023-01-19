import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

l = ["N01", "N18", "N09", "N17", "N26"]

df = pd.DataFrame()
for d in l:
    df = df.append(pd.read_csv(f"d/{d}.csv"))
df['timestamp'] = pd.to_datetime(df['time_sampled'], unit='s')
df = df[df.flow_rate>=0.25]
df = df[["node","flow_rate","timestamp"]]
df.set_index('timestamp', inplace=True)
df = df.sort_index().loc['2022-12-15':'2023-01-14']
df["Flow Meter"] = df["node"].map(dict(zip(df.node.unique(), [f"House {i}" for i in range(1,6)])))
# fig = sns.histplot(x="flow_rate",hue="Flow Meter",data=df,stat="density",palette=sns.color_palette("Set2"))
fig = sns.kdeplot(x="flow_rate",hue="Flow Meter",data=df,clip=(0,None),palette=sns.color_palette("Set2"))
plt.xlabel("Flow Rate (Liter/min)")
# ax.set_title("Flow Rate Distribution")
plt.tight_layout()
sns.despine()
plt.show()