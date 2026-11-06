import os
import matplotlib.pyplot as plt
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"

plt.style.use('default')

def generate_no_overlap_fig4_cluster_tree():
    fig, ax = plt.subplots(figsize=(10, 9.5), dpi=250)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axis('off')
    
    pos = {}
    pos[1] = (0, 0) # Central Root Node 1
    
    # 8 Equal Clusters with ZERO overlap between clusters
    n_clusters = 8
    motes_per_cluster = 8
    
    current_node = 2
    cluster_heads = []
    
    r_ch = 6.5       # Large radial distance to ensure zero overlap between clusters
    r_member = 1.5   # Tightly bounded member radius
    
    edges_root_to_ch = []
    edges_ch_to_member = []
    
    for c_idx in range(n_clusters):
        ang = c_idx * (2 * np.pi / n_clusters)
        ch_id = current_node
        cluster_heads.append(ch_id)
        
        ch_x = r_ch * np.cos(ang)
        ch_y = r_ch * np.sin(ang)
        pos[ch_id] = (ch_x, ch_y)
        edges_root_to_ch.append((1, ch_id))
        current_node += 1
        
        # Place equal member motes in outward sector away from center
        for m in range(motes_per_cluster):
            # Angular spread tightly constrained to +/- 22 degrees
            m_ang = ang + (m - (motes_per_cluster - 1) / 2.0) * (np.pi / 16.0)
            m_r = r_member + (m % 2) * 0.35
            mx = ch_x + m_r * np.cos(m_ang)
            my = ch_y + m_r * np.sin(m_ang)
            
            m_id = current_node
            pos[m_id] = (mx, my)
            edges_ch_to_member.append((ch_id, m_id))
            current_node += 1

    # Draw Root-to-CH Backbone Edges (Dark Navy Lines)
    for u, v in edges_root_to_ch:
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#1e293b', linewidth=1.8, zorder=2)

    # Draw CH-to-Member Spokes (Blue Lines)
    for u, v in edges_ch_to_member:
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#3b82f6', linewidth=1.1, alpha=0.85, zorder=1)

    # Draw Nodes
    for n_id, (x, y) in pos.items():
        if n_id == 1:
            # Root Sink Node
            ax.scatter(x, y, c='#ef4444', s=340, zorder=6, edgecolors='#991b1b', linewidth=1.6)
            ax.text(x, y, '1', color='white', fontweight='bold', fontsize=10, ha='center', va='center', zorder=7)
        elif n_id in cluster_heads:
            # Cluster Head Motes
            ax.scatter(x, y, c='#f59e0b', s=250, zorder=5, edgecolors='#b45309', linewidth=1.3)
            ax.text(x, y, str(n_id), color='black', fontweight='bold', fontsize=7.5, ha='center', va='center', zorder=6)
        else:
            # Equal Member Motes (Non-overlapping)
            ax.scatter(x, y, c='#3b82f6', s=160, zorder=4, edgecolors='#1d4ed8', linewidth=1.0)
            ax.text(x, y, str(n_id), color='white', fontweight='bold', fontsize=6.5, ha='center', va='center', zorder=5)

    plt.title('Fig. 4.  Cluster tree.', fontsize=12, fontweight='bold', pad=15, color='#1e293b')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'etasr_fig4_cluster_tree.png'), bbox_inches='tight')
    plt.close()
    print("[+] SUCCESS: Generated Fig. 4. Cluster tree with ZERO overlap between clusters!")

if __name__ == '__main__':
    generate_no_overlap_fig4_cluster_tree()
