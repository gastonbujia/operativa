#Algoritmo para detectar Bicoloring
import sys
from collections import deque

# Función auxiliar para cargar los datos
def load_num():
    num_str = sys.stdin.readline()
    if num_str == '\n' or num_str=='':
        return None
    return list(map(int, num_str.rstrip().split()))

# Cargaremos el grafo en una lista de adyacencias
def load_graph():
    vertices = load_num()[0]
    if vertices==0:
        return None
    edges = load_num()[0]
    adjList = [list() for v in range(vertices)]
    for i in range(edges):
        s, e = load_num()
        adjList[s].append(e)
        adjList[e].append(s)
    return adjList

def bicoloreo(E):
    n = len(E)
    procesado = [False for i in range(n)]
    descubierto = [False for i in range(n)]
    color = [0 for i in range(n)]
    u = 0
    descubierto[0] = True
    color[0] = 1
    Q = deque()
    Q.append(u)
    while len(Q) > 0:
        u = Q[0]
        Q.popleft()
        for v in E[u]:
            if procesado[v] == False:
                Q.append(v)
                procesado[v] = True
                color[v] = (-1)*color[u]
            elif color[u]==color[v]:
                return False
    return True

while True:
    adj = load_graph()
    if not adj:
        break

    if bicoloreo(adj):
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")

exit(0)
