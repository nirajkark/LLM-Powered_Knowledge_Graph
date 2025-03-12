# LLM-Powered_Knowledge_Graph# LLM-Powered Knowledge Graph Demo
Extracts triples from Nepal text using DistilBERT, stores them in Neo4j, and visualizes with Neovis.js.

## Setup
1. Install Python deps: `pip install -r requirements.txt`
2. Install Neo4j Desktop (password: "password").
3. Install Node.js deps: `cd visualization && npm install`

## Run
1. Extract triples: `python src/extract_triples.py`
2. Load to Neo4j: `python src/load_to_neo4j.py`
3. Visualize: `cd visualization && node server.js` (visit `http://localhost:3000`)
4. Query: `python src/query_graph.py`
## Visualization
- Interactive graph using Cytoscape.js at `http://localhost:3000`.
- Run `python src/query_graph.py` to export data, then `cd visualization && node server.js`.
## Results

- Triples: Nepal → capital → Kathmandu, etc.
- Interactive graph at `http://localhost:3000`.
