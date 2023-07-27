from collections import defaultdict

def main():
    r = open("input.txt", "r")
    w = open("output.txt", "w")

    n = int(r.readline()[:-1])

    l = list(map(int, r.readline().strip().split()))

    d = defaultdict(int)
    idxmap = defaultdict(list)

    for idx, i in enumerate(l):
        d[i] += 1
        idxmap[i].append(idx + 1)

    if any(map(lambda s: s & 1, d.values())):
        print(-1, file = w)
        raise SystemExit(0)

    for k, v in idxmap.items():
        for i in range(0, len(v), 2):
            print(v[i], v[i+1], file = w)

main()
