import requests, threading

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

s = "http://cloud.karachiwaterproject.com/static/csv/"

def d(a):
    print(f"attempting for",data[a])
    res = requests.get(s+a+".csv")
    if res.status_code == 200:
        open(f"d\{a}.csv", "wb").write(res.content)
    print("done for",data[a])

for d_ in data:
    t = threading.Thread(target=d, args=(d_,))
    t.start()
