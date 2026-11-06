import os
import matplotlib.pyplot as plt
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"

plt.style.use('default')

def generate_fig6_tgo_mesh():
    fig, ax = plt.subplots(figsize=(10.5, 10), dpi=250)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axis('off')
    
    # Dedicated RPL-UDP Sink Node (DODAG Root)
    sink_x, sink_y = 0.0, 7.8
    ax.scatter(sink_x, sink_y, c='#ef4444', s=380, marker='*', zorder=10, edgecolors='white', linewidths=2.0, label='RPL-UDP Sink Node (DODAG Root)')
    ax.text(sink_x, sink_y + 0.5, "RPL-UDP Sink Node (DODAG Root)", color='#dc2626', fontsize=10.5, fontweight='bold', ha='center', zorder=10)

    # 6 TGO Clusters forming 72 nodes total (12 nodes per cluster x 6 = 72 nodes: Node 1 to 72)
    clusters = [
        {'id': 'TGO Cluster 1', 'ch': 1,  'nodes': list(range(1, 13)),   'center': (-6.0, 3.2)},
        {'id': 'TGO Cluster 2', 'ch': 13, 'nodes': list(range(13, 25)),  'center': (0.0, 4.0)},
        {'id': 'TGO Cluster 3', 'ch': 25, 'nodes': list(range(25, 37)),  'center': (6.0, 3.2)},
        {'id': 'TGO Cluster 4', 'ch': 37, 'nodes': list(range(37, 49)),  'center': (-6.0, -4.0)},
        {'id': 'TGO Cluster 5', 'ch': 49, 'nodes': list(range(49, 61)),  'center': (0.0, -4.8)},
        {'id': 'TGO Cluster 6', 'ch': 61, 'nodes': list(range(61, 73)),  'center': (6.5, -4.0)}
    ]
    
    cluster_heads = [c['ch'] for c in clusters]
    pos = {}
    edges_intra_tgo = []
    
    # Position all 72 Nodes & Build Intra-Cluster TGO Triads
    for c in clusters:
        ch_id = c['ch']
        cx, cy = c['center']
        nodes_list = c['nodes']
        
        pos[ch_id] = (cx, cy)
        members = [n for n in nodes_list if n != ch_id]
        n_m = len(members)
        
        # Position members in triads
        for i, n_id in enumerate(members):
            ang = i * (2 * np.pi / n_m)
            r = 1.5 + (i % 2) * 0.45
            pos[n_id] = (cx + r * np.cos(ang), cy + r * np.sin(ang))
            # Intra-cluster spoke/triad edges to CH
            edges_intra_tgo.append((ch_id, n_id))
            
        # Form triangular triads between adjacent members in cluster
        for i in range(n_m):
            n1 = members[i]
            n2 = members[(i + 1) % n_m]
            edges_intra_tgo.append((n1, n2))

    # 1. RPL DODAG Links connecting CHs to Sink Node (Dashed Amber Lines)
    for idx, ch_id in enumerate(cluster_heads):
        ch_x, ch_y = pos[ch_id]
        ax.plot([ch_x, sink_x], [ch_y, sink_y], '--', color='#d97706', alpha=0.85, linewidth=1.8, zorder=3,
                label='RPL DODAG DAG Link (CH to Sink)' if idx == 0 else '')

    # 2. Inter-CH TGO Triad Mesh Overlay (Solid Green Lines)
    inter_ch_tgo_edges = [
        (1, 13), (13, 25), (25, 61), (61, 49), (49, 37), (37, 1),
        (1, 49), (13, 49), (25, 49), (37, 61)
    ]
    for idx, (ch_a, ch_b) in enumerate(inter_ch_tgo_edges):
        pa, pb = pos[ch_a], pos[ch_b]
        ax.plot([pa[0], pb[0]], [pa[1], pb[1]], '-', color='#10b981', alpha=0.9, linewidth=2.0, zorder=4,
                label='TGO Triad Connection (CH-to-CH Inter-Cluster)' if idx == 0 else '')

    # 3. Intra-Cluster TGO Lines (Solid Blue Lines)
    for u, v in edges_intra_tgo:
        if u in pos and v in pos:
            ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#3b82f6', alpha=0.6, linewidth=1.1, zorder=2)

    # 4. Draw Nodes as Blue/Gold Circles with White Numbers (All 72 Nodes: 1 to 72)
    for n_id, (x, y) in pos.items():
        if n_id in cluster_heads:
            # TGO Cluster Head Node
            ax.scatter(x, y, c='#f59e0b', s=270, zorder=6, edgecolors='#b45309', linewidth=1.5, label='Cluster Head (CH)' if n_id == cluster_heads[0] else '')
            ax.text(x, y, str(n_id), color='black', fontweight='bold', fontsize=8.0, ha='center', va='center', zorder=7)
        else:
            # Member Node
            ax.scatter(x, y, c='#3b82f6', s=160, zorder=4, edgecolors='#1d4ed8', linewidth=1.0)
            ax.text(x, y, str(n_id), color='white', fontweight='bold', fontsize=6.0, ha='center', va='center', zorder=5)

    ax.legend(loc='upper right', fontsize=8.5, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    plt.title('Fig. 6.  TGO mesh network.', fontsize=12.5, fontweight='bold', pad=15, color='#1e293b')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'etasr_fig6_tgo_mesh.png'), bbox_inches='tight')
    plt.close()
    print("[+] SUCCESS: Generated Fig. 6. TGO mesh network with EXACT 72 nodes (Node 1 to Node 72)!")

if __name__ == '__main__':
    generate_fig6_tgo_mesh()
