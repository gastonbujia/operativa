import sys

def ady(u,E):
    A = []
    for e in E:
        if u in e:
            e1 = e[:]
            e1.remove(u)
            A.extend(e1)
    return A

def prim(n,E):
    dist=[10**8 for i in range(n)]
    T=[False for i in range(n)]
    dist[0]=0
    for i in range(n):
        u = 0
        dMin = 10**8
        for v in range (n):
            if T[v] == False:
                if dist[v] < dMin:
                    dMin = dist[v]
                    u = v
        T[u] = True
        for v in ady(u,E):
            if
