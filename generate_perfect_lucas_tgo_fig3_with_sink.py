import os
import matplotlib.pyplot as plt
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"

plt.style.use('default')

def generate_lucas_tgo_fig3_with_sink():
    fig, ax = plt.subplots(figsize=(10, 9.5), dpi=250)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axis('off')
    
    # 1. Place Sink Node (Node 1 / RPL Root) at Top-Center (0, 7.0)
    pos = {1: (0.0, 7.0)}
    
    # Define 6 Lucas Sequence clusters: 3, 4, 7, 11, 18, 29
    lucas_clusters = [
        {'name': 'Cluster 1 (L_1=3)',  'size': 3,  'center': (-5.5, 3.8),  'color': '#2ecc71'},
        {'name': 'Cluster 2 (L_2=4)',  'size': 4,  'center': (0.0, 3.5),   'color': '#3498db'},
        {'name': 'Cluster 3 (L_3=7)',  'size': 7,  'center': (5.5, 3.8),   'color': '#9b59b6'},
        {'name': 'Cluster 4 (L_4=11)', 'size': 11, 'center': (-5.5, -3.2), 'color': '#e67e22'},
        {'name': 'Cluster 5 (L_5=18)', 'size': 18, 'center': (0.0, -4.2),  'color': '#16a085'},
        {'name': 'Cluster 6 (L_6=29)', 'size': 29, 'center': (6.0, -3.2),  'color': '#e74c3c'}
    ]
    
    edges_trimet = []
    edges_ch_trimet_sink = []
    cluster_heads = []
    
    current_node = 2
    
    for c_idx, cl in enumerate(lucas_clusters):
        cx, cy = cl['center']
        size = cl['size']
        ch_id = current_node
        cluster_heads.append(ch_id)
        
        if size == 3:
            # 3 nodes in a trimet triangle
            n1, n2, n3 = current_node, current_node+1, current_node+2
            r = 1.0
            pos[n1] = (cx + r*np.cos(0), cy + r*np.sin(0))
            pos[n2] = (cx + r*np.cos(2*np.pi/3), cy + r*np.sin(2*np.pi/3))
            pos[n3] = (cx + r*np.cos(4*np.pi/3), cy + r*np.sin(4*np.pi/3))
            edges_trimet.extend([(n1, n2), (n2, n3), (n3, n1)])
            current_node += 3
            
        elif size == 4:
            # 4 nodes (1 CH + 3 nodes in trimet triangle)
            ch = current_node
            pos[ch] = (cx, cy)
            r = 1.2
            n1, n2, n3 = current_node+1, current_node+2, current_node+3
            pos[n1] = (cx + r*np.cos(0), cy + r*np.sin(0))
            pos[n2] = (cx + r*np.cos(2*np.pi/3), cy + r*np.sin(2*np.pi/3))
            pos[n3] = (cx + r*np.cos(4*np.pi/3), cy + r*np.sin(4*np.pi/3))
            edges_trimet.extend([(n1, n2), (n2, n3), (n3, n1)])
            edges_trimet.extend([(ch, n1), (ch, n2), (ch, n3)])
            current_node += 4
            
        elif size == 7:
            ch = current_node
            pos[ch] = (cx, cy)
            n1, n2, n3 = current_node+1, current_node+2, current_node+3
            r = 1.3
            pos[n1] = (cx + r*np.cos(np.pi/6), cy + r*np.sin(np.pi/6))
            pos[n2] = (cx + r*np.cos(5*np.pi/6), cy + r*np.sin(5*np.pi/6))
            pos[n3] = (cx + r*np.cos(3*np.pi/2), cy + r*np.sin(3*np.pi/2))
            edges_trimet.extend([(n1, n2), (n2, ch), (ch, n1)])
            edges_trimet.extend([(n2, n3), (n3, ch), (ch, n2)])
            
            n4, n5, n6 = current_node+4, current_node+5, current_node+6
            r2 = 2.2
            pos[n4] = (cx + r2*np.cos(np.pi/4), cy + r2*np.sin(np.pi/4))
            pos[n5] = (cx + r2*np.cos(3*np.pi/4), cy + r2*np.sin(3*np.pi/4))
            pos[n6] = (cx + r2*np.cos(5*np.pi/4), cy + r2*np.sin(5*np.pi/4))
            edges_trimet.extend([(n4, n5), (n5, n1), (n1, n4)])
            edges_trimet.extend([(n5, n6), (n6, n2), (n2, n5)])
            current_node += 7

        elif size == 11:
            ch = current_node
            pos[ch] = (cx, cy)
            nodes_c = [current_node + i for i in range(11)]
            for t_idx in range(3):
                t_ang = t_idx * (2*np.pi / 3.0)
                n_a = nodes_c[1 + t_idx*3]
                n_b = nodes_c[2 + t_idx*3]
                n_c = nodes_c[3 + t_idx*3]
                
                pos[n_a] = (cx + 1.4*np.cos(t_ang - 0.3), cy + 1.4*np.sin(t_ang - 0.3))
                pos[n_b] = (cx + 1.4*np.cos(t_ang + 0.3), cy + 1.4*np.sin(t_ang + 0.3))
                pos[n_c] = (cx + 2.4*np.cos(t_ang), cy + 2.4*np.sin(t_ang))
                
                edges_trimet.extend([(ch, n_a), (n_a, n_b), (n_b, ch)])
                edges_trimet.extend([(n_a, n_c), (n_c, n_b), (n_b, n_a)])
                
            n_last = nodes_c[10]
            pos[n_last] = (cx, cy + 2.5)
            edges_trimet.extend([(n_last, nodes_c[3]), (nodes_c[3], nodes_c[6]), (nodes_c[6], n_last)])
            current_node += 11

        elif size == 18:
            ch = current_node
            pos[ch] = (cx, cy)
            nodes_c = [current_node + i for i in range(18)]
            for t_idx in range(5):
                t_ang = t_idx * (2*np.pi / 5.0)
                n_a = nodes_c[1 + t_idx*3]
                n_b = nodes_c[2 + t_idx*3]
                n_c = nodes_c[3 + t_idx*3]
                
                pos[n_a] = (cx + 1.5*np.cos(t_ang - 0.3), cy + 1.5*np.sin(t_ang - 0.3))
                pos[n_b] = (cx + 1.5*np.cos(t_ang + 0.3), cy + 1.5*np.sin(t_ang + 0.3))
                pos[n_c] = (cx + 2.6*np.cos(t_ang), cy + 2.6*np.sin(t_ang))
                
                edges_trimet.extend([(ch, n_a), (n_a, n_b), (n_b, ch)])
                edges_trimet.extend([(n_a, n_c), (n_c, n_b), (n_b, n_a)])
                
            pos[nodes_c[16]] = (cx + 3.2*np.cos(0.5), cy + 3.2*np.sin(0.5))
            pos[nodes_c[17]] = (cx + 3.2*np.cos(2.5), cy + 3.2*np.sin(2.5))
            edges_trimet.extend([(nodes_c[16], nodes_c[3]), (nodes_c[3], nodes_c[6]), (nodes_c[6], nodes_c[16])])
            edges_trimet.extend([(nodes_c[17], nodes_c[9]), (nodes_c[9], nodes_c[12]), (nodes_c[12], nodes_c[17])])
            current_node += 18

        elif size == 29:
            ch = current_node
            pos[ch] = (cx, cy)
            nodes_c = [current_node + i for i in range(29)]
            for t_idx in range(9):
                t_ang = t_idx * (2*np.pi / 9.0)
                n_a = nodes_c[1 + t_idx*3]
                n_b = nodes_c[2 + t_idx*3]
                n_c = nodes_c[3 + t_idx*3]
                
                pos[n_a] = (cx + 1.6*np.cos(t_ang - 0.2), cy + 1.6*np.sin(t_ang - 0.2))
                pos[n_b] = (cx + 1.6*np.cos(t_ang + 0.2), cy + 1.6*np.sin(t_ang + 0.2))
                pos[n_c] = (cx + 2.8*np.cos(t_ang), cy + 2.8*np.sin(t_ang))
                
                edges_trimet.extend([(ch, n_a), (n_a, n_b), (n_b, ch)])
                edges_trimet.extend([(n_a, n_c), (n_c, n_b), (n_b, n_a)])
                
            pos[nodes_c[28]] = (cx + 3.5, cy)
            edges_trimet.extend([(nodes_c[28], nodes_c[3]), (nodes_c[3], nodes_c[6]), (nodes_c[6], nodes_c[28])])
            current_node += 29

        ax.text(cx, cy + (2.5 if size <= 7 else 3.6), cl['name'], fontsize=9.5, fontweight='bold', 
                color=cl['color'], ha='center', bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor=cl['color'], alpha=0.9))

    # 2. TRIMET GRAPH CONNECTIONS AMONG ALL CLUSTER HEADS WITH THE SINK NODE
    # Triangular triads formed by (Sink, CH_i, CH_j) and inter-CH triads
    sink_id = 1
    ch1, ch2, ch3, ch4, ch5, ch6 = cluster_heads[0], cluster_heads[1], cluster_heads[2], cluster_heads[3], cluster_heads[4], cluster_heads[5]
    
    # Trimet triads connecting Sink Node with Cluster Heads
    ch_trimet_triads = [
        (sink_id, ch1, ch2),
        (sink_id, ch2, ch3),
        (sink_id, ch1, ch3),
        (ch1, ch4, ch2),
        (ch2, ch5, ch3),
        (ch3, ch6, ch5),
        (ch4, ch5, ch6),
        (sink_id, ch4, ch6)
    ]
    
    for u, v, w in ch_trimet_triads:
        edges_ch_trimet_sink.extend([(u, v), (v, w), (w, u)])

    # Draw Intra-cluster Trimet Triads (blue lines)
    for u, v in edges_trimet:
        if u in pos and v in pos:
            ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#3b82f6', alpha=0.75, linewidth=1.1, zorder=2)

    # Draw TRIMET GRAPH CONNECTIONS AMONG CLUSTER HEADS AND SINK NODE (highlighted green/purple lines)
    for u, v in set(edges_ch_trimet_sink):
        if u in pos and v in pos:
            ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#10b981', alpha=0.85, linewidth=2.0, zorder=3)

    # Draw Sink Node
    ax.scatter(pos[1][0], pos[1][1], c='#ef4444', s=340, marker='*', zorder=10, edgecolors='#991b1b', linewidth=1.8)
    ax.text(pos[1][0], pos[1][1] + 0.6, "Sink Node (RPL Root)", color='#dc2626', fontweight='bold', fontsize=10, ha='center', zorder=11)

    # Draw Nodes
    for n_id, (x, y) in pos.items():
        if n_id == 1: continue
        elif n_id in cluster_heads:
            # Cluster Head
            ax.scatter(x, y, c='#f59e0b', s=240, zorder=6, edgecolors='#b45309', linewidth=1.4)
            ax.text(x, y, str(n_id), color='black', fontweight='bold', fontsize=7.5, ha='center', va='center', zorder=7)
        else:
            # Trimet Mote
            ax.scatter(x, y, c='#3b82f6', s=150, zorder=4, edgecolors='#1d4ed8', linewidth=1.0)
            ax.text(x, y, str(n_id), color='white', fontweight='bold', fontsize=6.5, ha='center', va='center', zorder=5)

    plt.title('Fig. 3. Representation of Lucas-based clustering with TGO model', fontsize=12, fontweight='bold', pad=15, color='#1e293b')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'etasr_fig3_lucas_clustering.png'), bbox_inches='tight')
    plt.close()
    print("[+] SUCCESS: Generated Fig. 3 with Sink Node & Trimet Graph among all cluster heads!")

if __name__ == '__main__':
    generate_lucas_tgo_fig3_with_sink()
