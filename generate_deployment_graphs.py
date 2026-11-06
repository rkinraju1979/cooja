import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import os, re

sim_dir = '/home/rkr/simulations'
output_dir = '/mnt/c/Users/Kanaka Raju/Desktop/joy29'
deployments = ['lucas29', 'hexagonal29', 'grid29', 'circular29', 'random29']
top_names = {'lucas29': 'Lucas Deployment (Golden Ratio)', 'hexagonal29': 'Hexagonal Deployment', 'grid29': 'Grid Deployment', 'circular29': 'Circular Deployment', 'random29': 'Random Deployment'}
colors = {'lucas29': '#9b59b6', 'hexagonal29': '#2ecc71', 'grid29': '#3498db', 'circular29': '#e74c3c', 'random29': '#f1c40f'}

plt.style.use('dark_background')

print("=== GENERATING HIGH-RESOLUTION SPATIAL DEPLOYMENT GRAPHS ===")

# Create combined 5-panel figure
fig_all, axes = plt.subplots(2, 3, figsize=(18, 11))
axes_flat = axes.flatten()

for idx, top in enumerate(deployments):
    csc_path = f"{sim_dir}/{top}.csc"
    if not os.path.exists(csc_path):
        continue
    
    with open(csc_path, 'r') as f:
        xml_content = f.read()
    
    coords = {}
    mote_blocks = xml_content.split('<mote>')
    for m_idx, block in enumerate(mote_blocks[1:], 1):
        x_match = re.search(r'<x>([0-9\.\-]+)</x>', block)
        y_match = re.search(r'<y>([0-9\.\-]+)</y>', block)
        id_match = re.search(r'<id>([0-9]+)</id>', block)
        
        m_id = int(id_match.group(1)) if id_match else m_idx
        x_val = float(x_match.group(1)) if x_match else (m_idx * 5.0)
        y_val = float(y_match.group(1)) if y_match else (m_idx * 5.0)
        coords[m_id] = np.array([x_val, y_val])
        
    num_nodes = len(coords)
    node_ids = sorted(coords.keys())
    
    all_x = [coords[i][0] for i in node_ids]
    all_y = [coords[i][1] for i in node_ids]
    span_x = max(all_x) - min(all_x)
    span_y = max(all_y) - min(all_y)
    bbox_diameter = np.sqrt(span_x**2 + span_y**2)
    tx_range = max(45.0, bbox_diameter * 0.38)

    # --- Individual High-Res Plot ---
    fig_ind, ax_ind = plt.subplots(figsize=(8, 8))
    
    # Draw wireless communication edges
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            id_i, id_j = node_ids[i], node_ids[j]
            d = np.linalg.norm(coords[id_i] - coords[id_j])
            if d <= tx_range and d > 0:
                ax_ind.plot([coords[id_i][0], coords[id_j][0]], [coords[id_i][1], coords[id_j][1]],
                            color='#2c3e50', alpha=0.4, linewidth=1.0, zorder=1)

    # Draw client nodes (2 to 29)
    client_x = [coords[i][0] for i in node_ids if i > 1]
    client_y = [coords[i][1] for i in node_ids if i > 1]
    ax_ind.scatter(client_x, client_y, c=colors[top], s=180, label='Client Motes (2-29)', edgecolors='white', linewidth=1.5, zorder=3)
    
    # Draw Sink Root node (Node 1)
    sink_x, sink_y = coords[1][0], coords[1][1]
    ax_ind.scatter(sink_x, sink_y, c='#f1c40f', s=450, marker='*', label='RPL Root Sink (Node 1)', edgecolors='white', linewidth=2.0, zorder=4)

    # Add node ID labels
    for i in node_ids:
        offset = 2.5 if top == 'lucas29' else 1.2
        ax_ind.text(coords[i][0], coords[i][1] + offset, str(i), color='white', fontsize=9, fontweight='bold', ha='center', zorder=5)

    ax_ind.set_title(f"{top_names[top]}\nSpan: {span_x:.1f}m x {span_y:.1f}m (29 Motes)", fontsize=14, fontweight='bold', color='white', pad=15)
    ax_ind.set_xlabel('X Position (meters)', fontsize=11)
    ax_ind.set_ylabel('Y Position (meters)', fontsize=11)
    ax_ind.grid(True, linestyle='--', alpha=0.2)
    ax_ind.legend(frameon=True, facecolor='#151b26', edgecolor='#263347', loc='upper right')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/deployment_{top}.png", dpi=300)
    plt.close(fig_ind)

    # --- Draw onto Combined Multi-Panel Figure ---
    ax_curr = axes_flat[idx]
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            id_i, id_j = node_ids[i], node_ids[j]
            d = np.linalg.norm(coords[id_i] - coords[id_j])
            if d <= tx_range and d > 0:
                ax_curr.plot([coords[id_i][0], coords[id_j][0]], [coords[id_i][1], coords[id_j][1]],
                            color='#34495e', alpha=0.4, linewidth=0.8, zorder=1)

    ax_curr.scatter(client_x, client_y, c=colors[top], s=100, edgecolors='white', linewidth=1.0, zorder=3)
    ax_curr.scatter(sink_x, sink_y, c='#f1c40f', s=280, marker='*', edgecolors='white', linewidth=1.5, zorder=4)
    
    for i in node_ids:
        ax_curr.text(coords[i][0], coords[i][1] + 1.5, str(i), color='white', fontsize=7, ha='center', zorder=5)

    ax_curr.set_title(top_names[top], fontsize=12, fontweight='bold', color='white')
    ax_curr.grid(True, linestyle='--', alpha=0.2)

# Hide 6th unused subplot in 2x3 grid
axes_flat[5].axis('off')
fig_all.suptitle('Spatial Network Deployment Comparison (29 Motes, UDGM Radio Medium)', fontsize=18, fontweight='bold', color='white', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(f"{output_dir}/deployment_all_5_comparison.png", dpi=300)
plt.close(fig_all)

print("[+] Spatial deployment graph images generated successfully!")
