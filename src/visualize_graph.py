from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

# Query Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "niraj_cair"))

def get_graph_data():
    with driver.session() as session:
        result = session.run("MATCH (n)-[r:RELATION]->(m) RETURN n, r, m")
        G = nx.DiGraph()
        for record in result:
            source = record["n"]["name"]
            target = record["m"]["name"]
            rel_type = record["r"]["type"]
            G.add_node(source)
            G.add_node(target)
            G.add_edge(source, target, label=rel_type)
        return G

# Visualize
G = get_graph_data()
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Knowledge Graph: Nepal")
plt.savefig("../visualization/graph.png")
plt.show()

driver.close()