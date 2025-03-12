
# Dynamic Multilingual Knowledge Graph Builder and Visualizer 🌍

Welcome to the **Dynamic Multilingual Knowledge Graph Builder and Visualizer**, a scalable and interactive system designed to extract structured knowledge (triples) from unstructured text in multiple languages, store them in a graph database, and visualize them dynamically. This project is built for researchers, developers, and enthusiasts interested in Natural Language Processing (NLP), knowledge graphs, and graph visualization.

 This project has been scaled into a robust system that processes text from multiple countries and supports real-time updates via a web interface. It’s a perfect showcase of NLP, graph database management, and web development skills, with applications in multilingual data processing, semantic web research, and knowledge discovery.

---

## Project Overview

This project extracts relational triples (subject → predicate → object) from English text (with potential for Nepali and other languages) using a lightweight LLM (BERT), stores them in a Neo4j graph database, and visualizes the resulting knowledge graph interactively using Cytoscape.js. It supports dynamic updates, allowing users to upload new text files and see the graph expand in real-time. The current dataset includes data about countries like Nepal, India, Canada, Brazil, and Japan, yielding a graph with **[UPDATE HERE: e.g., 60 nodes and 62 relationships]** after recent expansions.

### Key Features
- **Multilingual Triple Extraction**: Extracts triples from English text using BERT-based NLP, with extensible support for Nepali and other languages.
- **Scalable Graph Storage**: Stores triples in Neo4j with a schema to ensure uniqueness and efficiency.
- **Dynamic Visualization**: Interactive graph visualization with Cytoscape.js, supporting **[UPDATE HERE: e.g., 60+ nodes and relationships]** with optimized layouts.
- **Real-Time Updates**: Upload new text via a web interface to dynamically update the graph.
- **Extensibility**: Designed to support additional languages (e.g., Hindi) and data sources (e.g., Wikipedia dumps).
-

### Technologies Used
- **NLP**: Transformers (BERT via Hugging Face) for entity and relation extraction.
- **Graph Database**: Neo4j for storing and querying the knowledge graph.
- **Web Interface**: Flask for dynamic updates and file uploads.
- **Visualization**: Cytoscape.js for interactive graph rendering.
- **Backend**: Python for extraction, loading, and querying.

---


## Getting Started

### Prerequisites
- **Python 3.8+**
- **Neo4j Desktop** (or Docker for Neo4j)
- **Node.js** (optional, for development)
- A web browser (e.g., Chrome, Firefox)
- 

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nirajkark/LLM-Powered_Knowledge_Graph.git
   cd dynamic-knowledge-graph



## Setup
1. Install Python deps:
2.   ```bash
     pip install -r requirements.txt
3. Install Neo4j Desktop (password: "password").
4. Install Node.js deps:
5.    ```bash
6.       cd visualization && npm install

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
