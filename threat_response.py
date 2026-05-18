from neo4j import GraphDatabase

# --- 1. CREDENTIALS ---
NEO4J_URI = "neo4j+s://90871c2a.databases.neo4j.io"
NEO4J_USER = "90871c2a"
NEO4J_PASSWORD = "1WDq6qoG6pKwkxiUtRl0_sRlvafCfhsBKOa1mjbL2TQ"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# --- 2. THE THREAT SCORING ENGINE ---
def analyze_threats():
    print("--------------------------------------------------")
    print("[*] INITIATING AI THREAT SCORING ENGINE...")
    print("--------------------------------------------------")

    # This query searches your graph for any IP addresses connected to known hackers
    query = """
    MATCH (actor:ThreatActor)-[:USES]->(ioc:Indicator)
    RETURN actor.name AS Hacker, ioc.value AS IP_Address, ioc.type AS Type
    """

    print("[*] Scanning Neo4j Graph for active threats...\n")
    
    # Executing the search
    records, summary, keys = driver.execute_query(
        query,
        database_="90871c2a"
    )

    # --- 3. AUTOMATED RESPONSE LOGIC (SOAR) ---
    for record in records:
        hacker = record["Hacker"]
        ip = record["IP_Address"]
        
        print(f"[!] ALERT: Malicious activity detected from IP: {ip}")
        print(f"    -> Associated with known group: {hacker}")
        
        # Simulating the Machine Learning Scoring Algorithm
        if "APT29" in hacker:
            score = 98
            severity = "CRITICAL"
            action = "AUTOMATIC BAN: Pushing IP to AWS WAF Firewall to block traffic."
        elif "Lazarus" in hacker:
            score = 85
            severity = "HIGH"
            action = "ISOLATION: Restricting Endpoint Access immediately."
        else:
            score = 60
            severity = "MEDIUM"
            action = "LOGGING: Flagged for SOC Analyst Review."

        print(f"    -> Threat Score Calculated: {score}/100 ({severity})")
        print(f"    -> Autonomous Response Triggered: {action}")
        print("-" * 50)

if __name__ == "__main__":
    analyze_threats()