from networkx.algorithms import betweenness_centrality

bet_fortaleza = betweenness_centrality( fortaleza_subgraph )
cc_fortaleza = nx.clustering(fortaleza_subgraph)
degrees_fortaleza = fortaleza_subgraph.degree()
# Plot the clustering coefficient per degree
plt.figure(figsize=(15, 6))
plt.grid(True, linewidth=0.1, color='#100000', linestyle='-')
plt.title('\n Clustering Coefficients and Betweeness.')
plt.xlabel('k')
plt.ylabel('Clustering coefficients')
plt.xticks(rotation=-90)
plt.tick_params(labelsize=5)

lists = cc_fortaleza.items()
x, y = zip(*lists) 

lists2 = sorted(bet_fortaleza.items(), key=lambda item: item[1], reverse=True) 
x2, y2 = zip(*lists2)

plt.plot(x2,y2,  'o',  label='Betweenness') 
plt.plot(x, y, 'o',  label='Clustering')

plt.legend()