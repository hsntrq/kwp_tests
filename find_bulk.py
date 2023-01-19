import pandas as pd
import matplotlib.pyplot as plt

data = {
    "N00":	"Drivers Area",
    "N01":	"Dr Hassaan Khan",
    "N02":	"Abdul Rehman",
    "N03":	"Ahsan Ali",
    "N04":	"Markhan Mushtaque",
    "N05":	"Junaid Ahmed-M",
    "N06":	"Junaid Ahmed-K",
    "N07":	"Muhammad Arif",
    "N08":	"Dr Anzar",
    "N09":	"Azmat Ali",
    "N10":	"Fahad Hussain",
    "N11":	"Waseem",
    "N12":	"M. Junaid G-Floor",
    "N13":	"M. Junaid F-Floor",
    "N14":	"Shehroz G-Floor",
    "N15":	"Shehroz F-Floor",
    "N16":	"Aamir",
    "N17":	"Javed",
    "N18":	"Hassaan",
    "N19":	"M. Ashraf",
    "N20":	"Tasneem",
    "N21":	"Shabaz 1",
    "N22":	"Shabaz 2",
    "N23":	"Shabaz 3",
    "N24":	"Shabaz 5",
    "N25":	"Umar",
    "N26":	"Nasir"
}

for d in data:
    df = pd.read_csv(f"d\\{d}.csv")
    dff = df["time_received"].value_counts().rename_axis('time_received').reset_index(name='counts')
    dff = dff[dff.counts >=30].sort_values(by="time_received")
    # dff.plot(y="counts", x="time_received", kind="scatter")
    # plt.show()
    dff['ti'] = pd.to_datetime(dff["time_received"], unit="s")
    dff.to_csv(f"bulk\\{data[d]}.csv")