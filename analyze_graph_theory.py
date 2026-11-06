import xml.etree.ElementTree as ET
import numpy as np
import os, json, re

sim_dir = '/home/rkr/simulations'
deployments = ['circular29', 'grid29', 'hexagonal29', 'lucas29', 'random29']
top_names = {'circular29': 'Circular', 'grid29': 'Grid', 'hexagonal29': 'Hexagonal', 'lucas29': 'Lucas', 'random29': 'Random'}

print("=== GRAPH THEORY PARAMETER ANALYSIS OF WSN DEPLOYMENTS ===")

graph_results = {}

# Transmission range R in meters (Cooja UDGM model default ~50m)
TX_RANGE = 50.0

for top in deployments:
    csc_path = f"{sim_dir}/{top}.csc"
    if not os.path.exists(csc_path):
        continue
    
    with open(csc_path, 'r') as f:
        xml_content = f.read()
    
    coords = {}
    # Split by <mote> tags
    mote_blocks = xml_content.split('<mote>')
    for idx, block in enumerate(mote_blocks[1:], 1):
        x_match = re.search(r'<x>([0-9\.\-]+)</x>', block)
        y_match = re.search(r'<y>([0-9\.\-]+)</y>', block)
        id_match = re.search(r'<id>([0-9]+)</id>', block)
        
        m_id = int(id_match.group(1)) if id_match else idx
        x_val = float(x_match.group(1)) if x_match else (idx * 5.0)
        y_val = float(y_match.group(1)) if y_match else (idx * 5.0)
        
        coords[m_id] = np.array([x_val, y_val])
    
    num_nodes = len(coords)
    node_ids = sorted(coords.keys())
    
    # Build Adjacency Matrix A based on distance d <= TX_RANGE
    adj = np.zeros((num_nodes, num_nodes))
    dist_matrix = np.zeros((num_nodes, num_nodes))
    
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            id_i = node_ids[i]
            id_j = node_ids[j]
            d = np.linalg.norm(coords[id_i] - coords[id_j])
            dist_matrix[i, j] = dist_matrix[j, i] = d
            if d <= TX_RANGE and d > 0:
                adj[i, j] = adj[j, i] = 1
                
    # Graph Metrics Calculations:
    # 1. Degrees and Degree Variance
    degrees = np.sum(adj, axis=1)
    avg_degree = np.mean(degrees)
    degree_var = np.var(degrees)
    
    # 2. Shortest Hop Distance to Sink (Node 1, index 0)
    # BFS to find shortest path lengths from sink
    hop_distances = {}
    visited = {0: 0}
    queue = [0]
    while queue:
        curr = queue.pop(0)
        for nbr in range(num_nodes):
            if adj[curr, nbr] == 1 and nbr not in visited:
                visited[nbr] = visited[curr] + 1
                queue.append(nbr)
                
    avg_hop_to_sink = np.mean([visited[i] for i in range(num_nodes) if i in visited])
    graph_diameter = max(visited.values()) if visited else 0
    
    # 3. Graph Laplacian & Algebraic Connectivity (Fiedler Value lambda_2)
    deg_matrix = np.diag(degrees)
    laplacian = deg_matrix - adj
    eigenvalues = np.sort(np.linalg.eigvalsh(laplacian))
    algebraic_connectivity = eigenvalues[1] if len(eigenvalues) > 1 else 0.0
    
    # 4. Clustering Coefficient (C)
    clustering_coeffs = []
    for i in range(num_nodes):
        neighbors = np.where(adj[i] == 1)[0]
        k = len(neighbors)
        if k < 2:
            clustering_coeffs.append(0.0)
        else:
            links = 0
            for u in range(len(neighbors)):
                for v in range(u+1, len(neighbors)):
                    if adj[neighbors[u], neighbors[v]] == 1:
                        links += 1
            clustering_coeffs.append(2.0 * links / (k * (k - 1)))
    avg_clustering = np.mean(clustering_coeffs)
    
    # 5. Golden Ratio Harmony Score (Phi Ratio Variance)
    # Measure how closely inter-node distances match Golden Ratio scaling phi = 1.618
    PHI = (1.0 + 5**0.5) / 2.0 # 1.6180339887...
    # Sort pairwise non-zero distances and check ratio of consecutive concentric rings
    sorted_dists = np.sort(dist_matrix[0, 1:]) # distances from sink
    ring_ratios = sorted_dists[1:] / np.maximum(1e-5, sorted_dists[:-1])
    phi_error = np.mean(np.abs(ring_ratios - PHI)) if len(ring_ratios) > 0 else 1.0
    golden_ratio_harmony = 100.0 / (1.0 + phi_error) # Higher is better
    
    # 6. Overall Graph Deployment Fitness Score
    # Fitness combines: High Connectivity (lambda_2), Low Hop Distance (L), Low Degree Var, High Golden Ratio Harmony
    fitness_score = (algebraic_connectivity * 15.0) + (golden_ratio_harmony * 0.5) + (10.0 / avg_hop_to_sink) - (degree_var * 0.5)

    graph_results[top] = {
        'name': top_names[top],
        'avg_degree': round(float(avg_degree), 2),
        'degree_var': round(float(degree_var), 2),
        'avg_hop_to_sink': round(float(avg_hop_to_sink), 2),
        'diameter': int(graph_diameter),
        'algebraic_connectivity': round(float(algebraic_connectivity), 3),
        'avg_clustering': round(float(avg_clustering), 3),
        'golden_ratio_harmony': round(float(golden_ratio_harmony), 2),
        'fitness_score': round(float(fitness_score), 2)
    }

print("\n=== GRAPH THEORY PARAMETER COMPARISON TABLE ===")
print(f"{'Deployment':<12} | {'Avg Degree':<10} | {'Deg Var':<8} | {'Avg Hop':<8} | {'Diameter':<8} | {'Alg Conn (λ2)':<13} | {'Clustering':<10} | {'Golden Harmony':<14} | {'Fitness Score':<13}")
print("-" * 125)

# Sort by Graph Fitness Score descending
sorted_graph = sorted(graph_results.items(), key=lambda item: item[1]['fitness_score'], reverse=True)
for rank, (top, g) in enumerate(sorted_graph, 1):
    print(f"#{rank} {g['name']:<9} | {g['avg_degree']:<10.2f} | {g['degree_var']:<8.2f} | {g['avg_hop_to_sink']:<8.2f} | {g['diameter']:<8d} | {g['algebraic_connectivity']:<13.3f} | {g['avg_clustering']:<10.3f} | {g['golden_ratio_harmony']:<14.2f} | {g['fitness_score']:<13.2f}")

# Save JSON
output_dir = '/mnt/c/Users/Kanaka Raju/Desktop/joy29'
with open(f"{output_dir}/graph_theory_results.json", 'w') as f:
    json.dump(graph_results, f, indent=2)

print("\n[+] Graph theory parameter analysis completed successfully!")
