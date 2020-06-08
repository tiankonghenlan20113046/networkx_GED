#构建多层论文中俩个图的GED
nodes = [(1,{'label':'C1'}),
         (2,{'label':'C2'}),
         (3,{'label':'C3'}),
         (4,{'label':'C4'}),
         (5,{'label':'N'})]
edges = [(1,2,{'label':'1'}),
         (2,4,{'label':'1'}),
         (4,5,{'label':'1'}),
         (5,3,{'label':'1'}),
         (3,1,{'label':'2'})]
g2 = nx.Graph()
g2.add_nodes_from(nodes)
g2.add_edges_from(edges)

nodes = [(1,{'label':'C1'}),
         (2,{'label':'C2'}),
         (3,{'label':'C3'}),
         (4,{'label':'C4'}),
         (5,{'label':'N'})]
edges = [(1,2,{'label':'1'}),
         (2,4,{'label':'1'}),
         (4,5,{'label':'1'}),
         (5,3,{'label':'1'}),
         (3,1,{'label':'1'}),
         (3,4,{'label':'1'})]
q = nx.Graph()
q.add_nodes_from(nodes)
q.add_edges_from(edges)

GED_q_g2 = nx.graph_edit_distance(g2, q)

GED_q_g2


