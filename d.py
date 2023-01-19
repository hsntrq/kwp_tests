import pandas as pd

df = pd.read_csv("c_logs.csv", index_col="id")

df = df[df.node=="asamad_test3"]

df = df[df.time.between(1650518534, 1650635028)]

# 1650608244

print(df.size)
