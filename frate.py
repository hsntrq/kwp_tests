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
fig = sns.catplot(y="flow_rate",x="Flow Meter",data=df,kind="violin",palette=sns.color_palette("Set2"))
plt.ylabel("Flow Rate (Liter/min)")
# plt.title("Total Daily Water Consumption")
plt.tight_layout()
plt.show()