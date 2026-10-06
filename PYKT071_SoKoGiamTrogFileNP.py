import pickle
from collections import Counter


def khong_giam(n):
    s = str(n)

    if len(s) < 2:
        return False

    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False

    return True


with open("DATA1.in", "rb") as f:
    data1 = pickle.load(f)

with open("DATA2.in", "rb") as f:
    data2 = pickle.load(f)


c1 = Counter(data1)
c2 = Counter(data2)

common = c1.keys() & c2.keys()

result = []

for x in common:
    if khong_giam(x):
        result.append(x)

result.sort()

for x in result:
    print(x, c1[x], c2[x])