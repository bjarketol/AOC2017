

import networkx as nx

g = nx.DiGraph()

with open('input.txt', 'r') as f:
    
    for line in f:
        items = line.strip().split()
        name, weight = items[0], int(items[1][1:-1])
 
        g.add_node(name, weight=weight)
            
        if len(items) > 2:
            children = [c.replace(',','') for c in items[3:]]
            
            for child in children:
                g.add_edge(name, child)

order = list(nx.topological_sort(g))
weights = {}

for node in reversed(order):
    
    total = g.nodes[node]['weight']
    
    val = None
    unbalanced = None

    print(node, total)
    for child in g[node]:
        
        if val is not None and weights[child] != val:
            
            for c in g[node]:
                print('c', c, weights[c], g.nodes[c]['weight'])

            unbalanced = child
            break

        val = weights[child]
        total += weights[child]

    if unbalanced: 
        diff = val - weights[unbalanced]
        print(diff)
        print(g.nodes[unbalanced]['weight'] + diff)
        break

    weights[node] = total



