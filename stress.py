import requests, threading, time

URL = "http://cloud.karachiwaterproject.com/api/add/"
F = ",".join(["0"]*10)
Latency = []
Threads = []

def tm(s_time):
    return ",".join([str(s_time+i/10) for i in range(10)])

def req(s):
    start = time.time()
    res = requests.get(URL+s)
    end = time.time()
    if res.status_code == 200:
        Latency.append(end-start)
    else:print(".",end="")


def test(samples):
    for sample in samples:
        t = threading.Thread(target=req, args=(sample,))
        t.start()
        Threads.append(t)
        time.sleep(1)            

curr = round(time.time())
keys = open("keys","r").readline().split(",")[:501]
reqs = {key: [f"{key}&{tm(curr+i)}&{F}" for i in range(1*60)] for key in keys}
# print(reqs)

for node in reqs:
    t = threading.Thread(target=test,args=(reqs[node],))
    t.start()
    Threads.append(t)

for t in Threads:
    t.join()

# print(Latency)
open("latency/100,10,10","w").write(",".join(map(str,Latency)))