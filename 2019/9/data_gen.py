import random
import queue

def gen_random_tree(size):
    """
    start from 0
    """
    assert(size >= 2)
    prufer = []
    for i in range(size - 2):
        prufer.append(random.choice(range(size)))
    
    degree = [1 for i in range(size)]
    for exist in prufer:
        degree[exist] += 1
    
    q = queue.PriorityQueue()
    for i in range(size):
        if degree[i] == 1:
            q.put(i)
    
    ret = []
    for i in range(size - 2):
        u = q.get()
        v = prufer[i]
        ret.append((u, v))

        degree[v] -= 1
        if degree[v] == 1:
            q.put(v)
    ret.append((q.get(), q.get()))

    return ret

def tagging_tree(root, edges, labeling=lambda x: str(x)):
    ret = dict()

    def tagging(graph, u, p):
        if u not in ret:
            ret[u] = (labeling(u), [])

        for v in graph[u]:
            if v == p:
                continue
            ret[u][1].append(v)
            tagging(graph, v, u)

    graph = dict()
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    tagging(graph, root, root)

    return ret

def generate_tag(x):
    alphabetic = 'abcdefghijklmnopqrstuvwxyz'

    length = random.randint(3, 5)
    return ''.join(random.sample(alphabetic, length))

def standard_tree_edges(root, tree):
    ret = []
    def iterate(node, parent):
        ret.append((parent, node, tree[node][0]))
        for child in tree[node][1]:
            iterate(child, node)
    iterate(root, -1)
    return ret

# print(standard_tree_edges(1, tagging_tree(1, gen_random_tree(10), generate_tag)) )

n = 10000
c_lb, c_ub = 100, 500
ci = [random.randint(c_lb, c_ub) for _ in range(n)]

print(n)
print(' '.join(map(str, ci)))
for i in range(n):
    root = random.randint(0, ci[i]-1)
    for p, u, tag in standard_tree_edges(root, tagging_tree(root, gen_random_tree(ci[i]), generate_tag) ):
        print(p, u, tag)

m = 10
print(m)
root = 0
for p, u, tag in standard_tree_edges(root, tagging_tree(root, gen_random_tree(m), generate_tag)):
    print(p, u, tag)