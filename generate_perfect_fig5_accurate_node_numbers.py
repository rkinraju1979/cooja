import os
import matplotlib.pyplot as plt
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"

plt.style.use('default')

def generate_fig5_accurate_node_numbers():
    fig, ax = plt.subplots(figsize=(10.5, 10), dpi=250)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axis('off')
    
    pos = {}
    
    # 1. Dedicated RPL-UDP Sink Node (DODAG Root)
    sink_x, sink_y = 0.0, 7.8
    ax.scatter(sink_x, sink_y, c='#ef4444', s=380, marker='*', zorder=10, edgecolors='white', linewidths=2.0, label='RPL-UDP Sink Node (DODAG Root)')
    ax.text(sink_x, sink_y + 0.5, "RPL-UDP Sink Node (DODAG Root)", color='#dc2626', fontsize=10.5, fontweight='bold', ha='center', zorder=10)

    # Exactly 72 Nodes across 6 Mesh Clusters (12 nodes per cluster x 6 = 72 nodes: Node 1 to 72)
    clusters = [
        {'id': 'Mesh Cluster 1', 'ch': 1,  'nodes': list(range(1, 13)),   'center': (-6.0, 3.2)},
        {'id': 'Mesh Cluster 2', 'ch': 13, 'nodes': list(range(13, 25)),  'center': (0.0, 4.0)},
        {'id': 'Mesh Cluster 3', 'ch': 25, 'nodes': list(range(25, 37)),  'center': (6.0, 3.2)},
        {'id': 'Mesh Cluster 4', 'ch': 37, 'nodes': list(range(37, 49)),  'center': (-6.0, -4.0)},
        {'id': 'Mesh Cluster 5', 'ch': 49, 'nodes': list(range(49, 61)),  'center': (0.0, -4.8)},
        {'id': 'Mesh Cluster 6', 'ch': 61, 'nodes': list(range(61, 73)),  'center': (6.5, -4.0)}
    ]
    
    cluster_heads = [c['ch'] for c in clusters]
    
    # Position all 72 Nodes
    for c in clusters:
        ch_id = c['ch']
        cx, cy = c['center']
        nodes_list = c['nodes']
        
        pos[ch_id] = (cx, cy)
        members = [n for n in nodes_list if n != ch_id]
        n_m = len(members)
        for i, n_id in enumerate(members):
            ang = i * (2 * np.pi / n_m)
            r = 1.6 + (i % 2) * 0.4
            pos[n_id] = (cx + r * np.cos(ang), cy + r * np.sin(ang))

    # 2. Connect all 6 Mesh Cluster Heads directly to the RPL-UDP Sink Node via RPL DODAG DAG links
    for idx, ch_id in enumerate(cluster_heads):
        ch_x, ch_y = pos[ch_id]
        ax.plot([ch_x, sink_x], [ch_y, sink_y], '--', color='#d97706', alpha=0.85, linewidth=1.8, zorder=3,
                label='RPL DODAG DAG Link (CH to Sink)' if idx == 0 else '')

    # 3. Intra-Cluster Mesh Edges
    edges_intra = []
    for c in clusters:
        nodes_list = c['nodes']
        for i in range(len(nodes_list)):
            for j in range(i+1, len(nodes_list)):
                n1, n2 = nodes_list[i], nodes_list[j]
                d = np.sqrt((pos[n1][0]-pos[n2][0])**2 + (pos[n1][1]-pos[n2][1])**2)
                if d < 2.8:
                    edges_intra.append((n1, n2))

    # 4. Full Mesh Connections among Cluster Heads (1, 13, 25, 37, 49, 61)
    edges_ch_mesh = []
    for i in range(len(cluster_heads)):
        for j in range(i+1, len(cluster_heads)):
            edges_ch_mesh.append((cluster_heads[i], cluster_heads[j]))

    # Draw Intra-Cluster Mesh Edges (Light Blue Lines)
    for u, v in edges_intra:
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#3b82f6', alpha=0.45, linewidth=0.9, zorder=1)

    # Draw Mesh Backbone Connections among Cluster Heads (Red Lines)
    for idx, (u, v) in enumerate(edges_ch_mesh):
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#ef4444', alpha=0.85, linewidth=2.0, zorder=4,
                label='Mesh Backbone Link (CH-to-CH)' if idx == 0 else '')

    # Draw Nodes as Blue/Gold Circles with White Numbers
    for n_id, (x, y) in pos.items():
        if n_id in cluster_heads:
            # Mesh Cluster Head Node
            ax.scatter(x, y, c='#f59e0b', s=260, zorder=6, edgecolors='#b45309', linewidth=1.5, label='Cluster Head (CH)' if n_id == cluster_heads[0] else '')
            ax.text(x, y, str(n_id), color='black', fontweight='bold', fontsize=7.5, ha='center', va='center', zorder=7)
        else:
            # Member Node
            ax.scatter(x, y, c='#3b82f6', s=160, zorder=4, edgecolors='#1d4ed8', linewidth=1.0)
            ax.text(x, y, str(n_id), color='white', fontweight='bold', fontsize=6.0, ha='center', va='center', zorder=5)

    ax.legend(loc='upper right', fontsize=8.5, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    plt.title('Fig. 5. Mesh network with RPL-UDP & 72 Nodes Topology', fontsize=12.5, fontweight='bold', pad=15, color='#1e293b')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'etasr_fig5_mesh_network.png'), bbox_inches='tight')
    plt.close()
    print("[+] SUCCESS: Generated Fig. 5. Mesh network with RPL-UDP and 72 nodes!")

if __name__ == '__main__':
    generate_fig5_accurate_node_numbers()
