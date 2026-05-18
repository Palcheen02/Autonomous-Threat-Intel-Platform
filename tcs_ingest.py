from neo4j import GraphDatabase

# --- 1. CREDENTIALS ---
NEO4J_URI = "neo4j+s://90871c2a.databases.neo4j.io"
NEO4J_USER = "90871c2a"
NEO4J_PASSWORD = "1WDq6qoG6pKwkxiUtRl0_sRlvafCfhsBKOa1mjbL2TQ" 

print("--------------------------------------------------")
print("[*] INITIATING CLEAN SLATE SCRIPT...")
print("--------------------------------------------------")

# --- 2. CONNECT & VERIFY ---
try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    driver.verify_connectivity()
    print("[*] SUCCESS: Connected to Neo4j Cloud!")
except Exception as e:
    print("\n[X] CONNECTION FAILED. The password is likely incorrect.")
    print(f"Error details: {e}")
    exit()

# --- 3. THE GRAPH QUERY ---
query = """
MERGE (actor:ThreatActor {name: $author_name})
MERGE (ioc:Indicator {value: $indicator, type: $indicator_type})
MERGE (actor)-[:USES]->(ioc)
"""

# --- 4. INJECT DATA ---
mock_pulses = [
    {"author_name": "APT29 (Cozy Bear)", "indicator": "185.11.125.40", "type": "IPv4"},
    {"author_name": "Lazarus Group", "indicator": "103.208.220.120", "type": "IPv4"}
]

print("[*] Pushing threat data to the graph...")

for pulse in mock_pulses:
    # Using the modern Neo4j execution method
    driver.execute_query(
        query,
        author_name=pulse["author_name"],
        indicator=pulse["indicator"],
        indicator_type=pulse["type"],
        database_="90871c2a"
    )

print("\n[SUCCESS] Script complete! Check your Neo4j browser.")