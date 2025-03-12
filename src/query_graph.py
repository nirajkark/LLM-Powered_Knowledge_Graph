from neo4j import GraphDatabase
import json

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "niraj_cair"))

def query_graph_to_json():
    with driver.session() as session:
        result = session.run("MATCH (n)-[r:RELATION]->(m) RETURN n, r, m")
        nodes = {}
        edges = []
        for record in result:
            # Nodes
            source = record["n"]["name"]
            target = record["m"]["name"]
            if source not in nodes:
                nodes[source] = {"id": source, "label": source}
            if target not in nodes:
                nodes[target] = {"id": target, "label": target}
            # Edges
            edges.append({
                "source": source,
                "target": target,
                "label": record["r"]["type"]
            })
        # Format for Cytoscape.js
        graph_data = {
            "nodes": list(nodes.values()),
            "edges": edges
        }
        with open("../visualization/graph_data.json", "w") as f:
            json.dump(graph_data, f, indent=2)
        return graph_data

print("Exporting graph data:", query_graph_to_json())
driver.close()