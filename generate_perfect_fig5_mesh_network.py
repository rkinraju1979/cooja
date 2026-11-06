import os
import matplotlib.pyplot as plt
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"

plt.style.use('default')

def generate_fig5_mesh_network_with_ch_mesh():
    fig, ax = plt.subplots(figsize=(10, 9.5), dpi=250)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axis('off')
    
    pos = {}
    
    # 5 Main Mesh Clusters with designated Cluster Heads
    clusters = [
        {'id': 'C1', 'ch': 1,  'nodes': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 'center': (-3.5, 3.5)},
        {'id': 'C2', 'ch': 20, 'nodes': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], 'center': (3.5, 3.5)},
        {'id': 'C3', 'ch': 40, 'nodes': [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 'center': (0.0, 0.0)},
        {'id': 'C4', 'ch': 60, 'nodes': [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], 'center': (-3.5, -3.5)},
        {'id': 'C5', 'ch': 80, 'nodes': [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], 'center': (3.5, -3.5)}
    ]
    
    cluster_heads = [c['ch'] for c in clusters]
    
    # Position Nodes
    for c in clusters:
        ch_id = c['ch']
        cx, cy = c['center']
        pos[ch_id] = (cx, cy)
        
        nodes_list = [n for n in c['nodes'] if n != ch_id]
        n_n = len(nodes_list)
        for i, n_id in enumerate(nodes_list):
            ang = i * (2 * np.pi / n_n)
            r = 1.3 + (i % 2) * 0.3
            pos[n_id] = (cx + r * np.cos(ang), cy + r * np.sin(ang))

    # 1. Intra-Cluster Mesh Edges
    edges_intra = []
    for c in clusters:
        nodes_list = c['nodes']
        for i in range(len(nodes_list)):
            for j in range(i+1, len(nodes_list)):
                n1, n2 = nodes_list[i], nodes_list[j]
                d = np.sqrt((pos[n1][0]-pos[n2][0])**2 + (pos[n1][1]-pos[n2][1])**2)
                if d < 2.4:
                    edges_intra.append((n1, n2))

    # 2. MESH CONNECTIONS AMONG ALL CLUSTER HEADS (Full Mesh Backbone among CHs)
    edges_ch_mesh = []
    for i in range(len(cluster_heads)):
        for j in range(i+1, len(cluster_heads)):
            edges_ch_mesh.append((cluster_heads[i], cluster_heads[j]))

    # Draw Intra-Cluster Mesh Edges (Light Blue Lines)
    for u, v in edges_intra:
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#3b82f6', alpha=0.45, linewidth=0.9, zorder=1)

    # Draw MESH CONNECTIONS AMONG CLUSTER HEADS (Highlighted Red Lines forming full mesh)
    for u, v in edges_ch_mesh:
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#ef4444', alpha=0.85, linewidth=2.2, zorder=3)

    # Draw Nodes
    for n_id, (x, y) in pos.items():
        if n_id in cluster_heads:
            # Cluster Head Motes in Mesh Network
            ax.scatter(x, y, c='#f59e0b', s=260, zorder=5, edgecolors='#b45309', linewidth=1.5)
            ax.text(x, y, str(n_id), color='black', fontweight='bold', fontsize=7.5, ha='center', va='center', zorder=6)
        else:
            # Member Motes
            ax.scatter(x, y, c='#3b82f6', s=160, zorder=4, edgecolors='#1d4ed8', linewidth=1.0)
            ax.text(x, y, str(n_id), color='white', fontweight='bold', fontsize=6.5, ha='center', va='center', zorder=5)

    plt.title('Fig. 5.  Mesh network.', fontsize=12, fontweight='bold', pad=15, color='#1e293b')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'etasr_fig5_mesh_network.png'), bbox_inches='tight')
    plt.close()
    print("[+] SUCCESS: Generated Fig. 5. Mesh network with mesh connection among cluster heads!")

if __name__ == '__main__':
    generate_fig5_mesh_network_with_ch_mesh()
