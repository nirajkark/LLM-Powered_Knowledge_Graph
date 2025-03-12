from neo4j import GraphDatabase

# Connect to Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "niraj_cair"))

def add_triple(tx, subject, predicate, object_):
    query = (
        "MERGE (s:Entity {name: $subject}) "
        "MERGE (o:Entity {name: $object}) "
        "MERGE (s)-[r:RELATION {type: $predicate}]->(o)"
    )
    tx.run(query, subject=subject, predicate=predicate, object=object_)

# Load triples
with driver.session() as session:
    with open("triples.txt", "r") as f:
        for line in f:
            subject, predicate, object_ = line.strip().split(',')
            session.write_transaction(add_triple, subject, predicate, object_)

driver.close()
print("Triples loaded into Neo4j.")