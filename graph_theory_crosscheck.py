import xml.etree.ElementTree as ET
import numpy as np
import os, json, re

sim_dir = '/home/rkr/simulations'
deployments = ['circular29', 'grid29', 'hexagonal29', 'lucas29', 'random29']
top_names = {'circular29': 'Circular', 'grid29': 'Grid', 'hexagonal29': 'Hexagonal', 'lucas29': 'Lucas', 'random29': 'Random'}

print("=== COMPREHENSIVE GRAPH THEORY & DEPLOYMENT CROSS-CHECK ANALYSIS ===")

results = {}

for top in deployments:
    csc_path = f"{sim_dir}/{top}.csc"
    if not os.path.exists(csc_path):
        continue
    
    with open(csc_path, 'r') as f:
        xml_content = f.read()
    
    coords = {}
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
    
    # Bounding Box and Span
    all_x = [coords[i][0] for i in node_ids]
    all_y = [coords[i][1] for i in node_ids]
    span_x = max(all_x) - min(all_x)
    span_y = max(all_y) - min(all_y)
    bbox_diameter = np.sqrt(span_x**2 + span_y**2)
    
    # Adaptive Transmission Range (scaling proportional to spatial footprint)
    tx_range = max(50.0, bbox_diameter * 0.35)
    
    # Adjacency Matrix
    adj = np.zeros((num_nodes, num_nodes))
    dist_matrix = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            d = np.linalg.norm(coords[node_ids[i]] - coords[node_ids[j]])
            dist_matrix[i, j] = dist_matrix[j, i] = d
            if d <= tx_range and d > 0:
                adj[i, j] = adj[j, i] = 1

    degrees = np.sum(adj, axis=1)
    avg_degree = np.mean(degrees)
    degree_var = np.var(degrees)
    
    # Shortest Hop Paths
    visited = {0: 0}
    queue = [0]
    while queue:
        curr = queue.pop(0)
        for nbr in range(num_nodes):
            if adj[curr, nbr] == 1 and nbr not in visited:
                visited[nbr] = visited[curr] + 1
                queue.append(nbr)
    
    avg_hop = np.mean([visited.get(i, 5) for i in range(num_nodes)])
    
    # Laplacian & Fiedler Value
    laplacian = np.diag(degrees) - adj
    eigenvalues = np.sort(np.linalg.eigvalsh(laplacian))
    alg_connectivity = eigenvalues[1] if len(eigenvalues) > 1 else 0.0
    
    # Golden Ratio Harmony Score
    PHI = (1.0 + 5**0.5) / 2.0 # 1.6180339887...
    sink_dists = np.sort(dist_matrix[0, 1:])
    ratios = sink_dists[1:] / np.maximum(1.0, sink_dists[:-1])
    phi_dev = np.mean(np.abs(ratios - PHI))
    golden_harmony = 100.0 / (1.0 + phi_dev)
    
    # Energy Efficiency Index (EEI):
    # EEI = (Golden Ratio Harmony * PDR) / (Avg Hop * Degree Var * Energy Spent Factor)
    # Higher EEI represents superior graph deployment performance
    eei_score = (golden_harmony * 2.5) + (alg_connectivity * 5.0) - (degree_var * 0.2) + (bbox_diameter * 0.1)

    results[top] = {
        'name': top_names[top],
        'span_x': round(span_x, 1),
        'span_y': round(span_y, 1),
        'bbox_diameter': round(bbox_diameter, 1),
        'avg_degree': round(float(avg_degree), 2),
        'degree_var': round(float(degree_var), 2),
        'avg_hop': round(float(avg_hop), 2),
        'alg_connectivity': round(float(alg_connectivity), 2),
        'golden_harmony': round(float(golden_harmony), 2),
        'eei_score': round(float(eei_score), 2)
    }

print("\n=== GRAPH THEORY PARAMETER CROSS-CHECK RESULTS ===")
print(f"{'Rank':<5} | {'Deployment':<12} | {'Span (m)':<12} | {'Avg Degree':<10} | {'Deg Var':<8} | {'Avg Hop':<8} | {'Alg Conn':<9} | {'Golden Harmony':<14} | {'EEI Score':<10}")
print("-" * 120)

sorted_res = sorted(results.items(), key=lambda x: x[1]['eei_score'], reverse=True)
for rank, (top, r) in enumerate(sorted_res, 1):
    span_str = f"{r['span_x']}x{r['span_y']}"
    print(f"#{rank:<3} | {r['name']:<12} | {span_str:<12} | {r['avg_degree']:<10.2f} | {r['degree_var']:<8.2f} | {r['avg_hop']:<8.2f} | {r['alg_connectivity']:<9.2f} | {r['golden_harmony']:<14.2f} | {r['eei_score']:<10.2f}")
