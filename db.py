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
with open("db.sh", "w") as f:
    for d in data:
        f.write(f"sudo -u postgres psql -d kwp -c \"\COPY (select api_reading.id,name as node,time_sampled,time_received,battery_level,flow_rate,temperature,flow_count,signal_strength,api_development.total_flow from api_reading join api_node on node_id=api_node.id join api_development on api_reading.id=reading_id where name='{data[d]}' order by time_sampled desc) TO '/home/kwpt-api/static/csv/{d}.csv' csv header;\"\n")