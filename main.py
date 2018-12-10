import networkx as nx

#%%
politicians = [
    'larsloekke',
    'mettefrederiks',
    'anderssamuelsen',
    'oestergaard',
    'kristianthdahl',
    'uffeelbaek',
    'sorenpape',
    'pskipperel',
    'piaolsen'
]

#%% Read edge file
with open('data/graph_file.edges', 'rb') as edge_file:
    edges = edge_file.readlines()
    edge_file.close()

edges = [edge.decode('utf-8').rstrip() for edge in edges]


#%% Create the directed graph
G = nx.DiGraph()
G.add_edges_from([tuple(edge.lower().split(' ')) for edge in edges])


#%% Preprocess
for degree in G.copy().in_degree():
    if degree[1] < 1.0:
        G.remove_node(degree[0])


#%% Degree centrality
in_degree_centrality = nx.in_degree_centrality(G)


#%%
print('In degree centrality for politicians')
for user, rank in in_degree_centrality.items():
    if user in politicians:
        print(user, rank)


#%% Compute page rank score
page_rank_score = nx.pagerank(G)


#%%
print('Politicians page rank')
for user, rank in page_rank_score.items():
    if user in politicians:
        print(user, rank)

