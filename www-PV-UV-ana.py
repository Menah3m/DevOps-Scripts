from collections import Counter

ips=[]
c= Counter()
with open('/www/wwwlogs/mi2m.cn.log','r') as f:
    for line in f:
        ips.append(line.split()[0])
        c[line.split()[0]] += 1
print("PV is {}".format(len(ips)))
print("UV is {}".format(len(set(ips))))
print("Most Linked IP : {}".format(c.most_common(10)))
