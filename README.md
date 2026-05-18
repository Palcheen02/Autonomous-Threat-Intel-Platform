# Autonomous-Threat-Intel-Platform
A Python-based Autonomous Threat Intelligence Platform (ATIP) that leverages a Neo4j Knowledge Graph to ingest OSINT data, score threat severity, and trigger automated SOAR responses.
# Autonomous Threat Intelligence Platform (ATIP) 🛡️

An automated security architecture that replaces manual SOC analysis with a Graph-Based detection engine. This platform utilizes Neo4j cloud infrastructure to map complex threat relationships and a Python-based execution engine to automate the "Observe, Orient, Decide, Act" (OODA) loop.

## ⚙️ Core Features
* **Automated OSINT Ingestion:** Fetches active malicious indicators (IPs, Domains) from simulated threat feeds.
* **Graph-Based Threat Mapping:** Normalizes unstructured data into a Neo4j Knowledge Graph, creating physical links between Threat Actors (e.g., APT29, Lazarus Group) and their infrastructure.
* **Algorithmic Threat Scoring:** Continuously polls the graph to calculate severity scores (0-100) based on actor profiles.
* **Autonomous SOAR Response:** Triggers simulated defensive actions without human intervention, such as AWS WAF IP bans for critical threats and endpoint isolation for high-level threats.

## 🛠️ Technologies Used
* **Python 3.x:** Core logic and automation engine.
* **Neo4j Aura:** Cloud-based graph database for relationship mapping.
* **Cypher Query Language:** Parameterized data injection and threat hunting queries.
* **Neo4j Python Driver:** Secure database connectivity and execution.

## 📂 Project Structure
* `tcs_ingest.py`: The data pipeline script that connects to the cloud database and structures the STIX-like threat data.
* `threat_response.py`: The AI scoring engine that queries the graph for active indicators and executes simulated containment protocols.

## 🚀 How to Run Locally
1. Clone this repository.
2. Ensure you have the `neo4j` Python library installed: `pip install neo4j`.
3. You must have an active Neo4j Aura database instance. 
4. Update the `NEO4J_URI`, `NEO4J_USER` (Instance ID), and `NEO4J_PASSWORD` variables in both Python scripts with your own credentials.
5. Run the ingestion pipeline first to build the graph: `python tcs_ingest.py`
6. Run the scoring engine to trigger the automated responses: `python threat_response.py`

---
*This project was developed as an Industry Project prototype to demonstrate automated threat detection and response architectures.*
