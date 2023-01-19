import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

l = ["N01", "N18", "N09", "N17", "N26"]

df = pd.DataFrame()
for d in l:
    df = df.append(pd.read_csv(f"d/{d}.csv"))
df['timestamp'] = pd.to_datetime(df['time_sampled'], unit='s')
df['flow'] = df['flow_rate']/2
df = df[["node","flow","timestamp"]]
df.set_index('timestamp', inplace=True)
df = df.sort_index().loc['2022-12-15':'2023-01-14']
df = df.groupby("node").resample("1D").sum().reset_index()
df["Flow Meter"] = df["node"].map(dict(zip(df.node.unique(), [f"House {i}" for i in range(1,6)])))
fig, ax = plt.subplots()
fig = sns.barplot(x="timestamp",y="flow",hue="Flow Meter",data=df,ax=ax,palette=sns.color_palette("Set2"),lw=0.3)
x_dates = df['timestamp'].dt.strftime('%Y-%m-%d').sort_values().unique()
ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
ax.set_xlabel("Date")
ax.set_ylabel("Daily Flow (Liters)")
ax.set_title("Total Daily Water Consumption")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
sns.despine()
plt.show()