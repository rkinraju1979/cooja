import os
import matplotlib.pyplot as plt
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"

plt.style.use('default')

def generate_fig4_cluster_tree():
    fig, ax = plt.subplots(figsize=(10.5, 10), dpi=250)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axis('off')
    
    pos = {}
    pos[1] = (0, 0) # Central RPL-UDP Root Sink Node 1
    
    # 8 Equal Clusters, each having exactly 8 member motes (total 73 nodes: 1 Root + 8 CHs + 64 Member Motes)
    n_clusters = 8
    motes_per_cluster = 8 # EQUAL 8 MEMBER MOTES PER CLUSTER
    
    ch_ids = [2, 11, 20, 29, 38, 47, 56, 65]
    
    r_ch = 4.8
    r_mem = 2.0
    
    edges_root_to_ch = []
    edges_ch_to_member = []
    
    cluster_heads = []
    
    node_counter = 2
    for c_idx in range(n_clusters):
        ang = c_idx * (2 * np.pi / n_clusters)
        ch_id = ch_ids[c_idx]
        cluster_heads.append(ch_id)
        
        ch_pos = (r_ch * np.cos(ang), r_ch * np.sin(ang))
        pos[ch_id] = ch_pos
        edges_root_to_ch.append((1, ch_id))
        
        # Equal member motes for this cluster arranged in a clean, non-crossing radial arc around CH
        start_angle = ang - np.pi / 3.2
        end_angle = ang + np.pi / 3.2
        member_angles = np.linspace(start_angle, end_angle, motes_per_cluster)
        
        for m_idx, m_ang in enumerate(member_angles):
            m_r = r_mem
            m_x = ch_pos[0] + m_r * np.cos(m_ang)
            m_y = ch_pos[1] + m_r * np.sin(m_ang)
            
            # Sequential member node IDs
            m_id = node_counter
            while m_id in ch_ids or m_id == 1 or m_id in pos:
                m_id += 1
            node_counter = m_id + 1
            
            pos[m_id] = (m_x, m_y)
            edges_ch_to_member.append((ch_id, m_id))

    # Draw RPL DODAG DAG Backbone Edges connecting CHs to RPL-UDP Root Sink 1 (Dashed Orange Lines)
    for idx, (u, v) in enumerate(edges_root_to_ch):
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '--', color='#d97706', linewidth=2.2, alpha=0.9, zorder=2,
                label='RPL DODAG DAG Link (CH to Root)' if idx == 0 else '')

    # Draw CH-to-Member Spokes (Solid Blue Lines for UDP Data/Control Packets)
    for idx, (u, v) in enumerate(edges_ch_to_member):
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#3b82f6', linewidth=1.2, alpha=0.85, zorder=1,
                label='UDP Data / Control Link' if idx == 0 else '')

    # Draw Nodes as Blue/Gold Circles with White Numbers
    for n_id, (x, y) in pos.items():
        if n_id == 1:
            # Central RPL-UDP Root Sink Node 1 (Red Star)
            ax.scatter(x, y, c='#ef4444', s=420, marker='*', zorder=6, edgecolors='white', linewidth=1.8, label='RPL-UDP Root Sink (Node 1)')
            ax.text(x, y + 0.45, 'RPL-UDP Root Sink (Node 1)', color='#dc2626', fontweight='bold', fontsize=9.0, ha='center', va='center', zorder=7)
        elif n_id in cluster_heads:
            # Cluster Head Motes (8 Equal Clusters)
            ax.scatter(x, y, c='#f59e0b', s=280, zorder=5, edgecolors='#b45309', linewidth=1.5, label='Cluster Head (CH)' if n_id == cluster_heads[0] else '')
            ax.text(x, y, str(n_id), color='black', fontweight='bold', fontsize=8.0, ha='center', va='center', zorder=6)
        else:
            # Equal Member Motes
            ax.scatter(x, y, c='#3b82f6', s=160, zorder=4, edgecolors='#1d4ed8', linewidth=1.0)
            ax.text(x, y, str(n_id), color='white', fontweight='bold', fontsize=6.5, ha='center', va='center', zorder=5)

    ax.legend(loc='upper right', fontsize=8.5, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    plt.title('Fig. 4. Cluster tree with RPL-UDP & Equal Clusters Topology', fontsize=12.5, fontweight='bold', pad=15, color='#1e293b')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'etasr_fig4_cluster_tree.png'), bbox_inches='tight')
    plt.close()
    print("[+] SUCCESS: Generated Fig. 4. Cluster tree with RPL-UDP and Equal Clusters!")

if __name__ == '__main__':
    generate_fig4_cluster_tree()
