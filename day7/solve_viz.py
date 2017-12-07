from graphviz import Digraph
import matplotlib.pyplot as plt


g = Digraph('G', filename='graph.gv', format='png')

with open('input.txt', 'r') as f:
    
    for line in f:
        items = line.strip().split()
        name, weight = items[0], int(items[1][1:-1])
 
        g.node(name, weight=str(weight))
            
        print(name)
        if len(items) > 2:
            children = [c.replace(',','') for c in items[3:]]
            
            for child in children:
                print(child)
                g.edge(name, child)


g.view()

    
