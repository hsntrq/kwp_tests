import requests, threading

s = "http://cloud.karachiwaterproject.com/static/csv/"

def d(a):
    print(f"attempting for",a)
    res = requests.get(s+a+".csv")
    if res.status_code == 200:
        open(f"files\{a}.csv", "wb").write(res.content)
    print("done for",a)

l = []
for i in range(21,23):
    for j in range(1,13):
        a = str(i) + "," + ("0"+str(j))[-2:]
        t = threading.Thread(target=d, args=(a,))
        t.start()
        l.append(t)