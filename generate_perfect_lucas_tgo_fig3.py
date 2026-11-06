import os
import matplotlib.pyplot as plt
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"

plt.style.use('default')

def generate_lucas_tgo_fig3():
    fig, ax = plt.subplots(figsize=(11, 10), dpi=250)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axis('off')
    
    # 1. RPL-UDP Dedicated Sink Node (DODAG Root)
    sink_x, sink_y = 0.0, 7.8
    ax.scatter(sink_x, sink_y, c='#ef4444', s=380, marker='*', zorder=10, edgecolors='white', linewidths=2.0, label='RPL-UDP Sink Node (DODAG Root)')
    ax.text(sink_x, sink_y + 0.5, "RPL-UDP Sink Node (DODAG Root)", color='#dc2626', fontsize=10.5, fontweight='bold', ha='center', zorder=10)

    # Define Lucas sequence cluster sizes: 3, 4, 7, 11, 18, 29
    lucas_clusters = [
        {'name': 'Cluster 1 (L_1=3)',  'size': 3,  'center': (-6.0, 3.2),  'color': '#2ecc71'},
        {'name': 'Cluster 2 (L_2=4)',  'size': 4,  'center': (0.0, 4.0),   'color': '#3498db'},
        {'name': 'Cluster 3 (L_3=7)',  'size': 7,  'center': (6.0, 3.2),   'color': '#9b59b6'},
        {'name': 'Cluster 4 (L_4=11)', 'size': 11, 'center': (-6.0, -4.0), 'color': '#e67e22'},
        {'name': 'Cluster 5 (L_5=18)', 'size': 18, 'center': (0.0, -4.8),  'color': '#16a085'},
        {'name': 'Cluster 6 (L_6=29)', 'size': 29, 'center': (6.5, -4.0),  'color': '#e74c3c'}
    ]
    
    pos = {}
    edges_trimet = []
    cluster_heads = []
    
    current_node = 1
    
    for c_idx, cl in enumerate(lucas_clusters):
        cx, cy = cl['center']
        size = cl['size']
        ch_id = current_node
        cluster_heads.append(ch_id)
        
        if size == 3:
            # 1 Trimet Triangle (3 nodes)
            n1, n2, n3 = current_node, current_node+1, current_node+2
            r = 1.0
            pos[n1] = (cx + r*np.cos(0), cy + r*np.sin(0))
            pos[n2] = (cx + r*np.cos(2*np.pi/3), cy + r*np.sin(2*np.pi/3))
            pos[n3] = (cx + r*np.cos(4*np.pi/3), cy + r*np.sin(4*np.pi/3))
            edges_trimet.extend([(n1, n2), (n2, n3), (n3, n1)])
            current_node += 3
            
        elif size == 4:
            # 1 Trimet Triangle + 1 Central CH Node
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
            # 2 Trimet Triangles sharing CH (7 nodes)
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
            # 3 Trimet Triangles (11 nodes)
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
            # 5 Trimet Triangles (18 nodes)
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
            # 9 Trimet Triangles (29 nodes)
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

        # Annotate Cluster Box & Name
        ax.text(cx, cy + (2.5 if size <= 7 else 3.6), cl['name'], fontsize=9.5, fontweight='bold', 
                color=cl['color'], ha='center', bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor=cl['color'], alpha=0.9))

    # Draw Intra-Cluster Trimet Triangle Edges (solid blue lines)
    for u, v in edges_trimet:
        if u in pos and v in pos:
            ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], '-', color='#3b82f6', alpha=0.75, linewidth=1.2, zorder=2)

    # 2. CONNECT ALL CLUSTER HEADS DIRECTLY TO THE RPL-UDP SINK NODE VIA RPL DODAG DAG LINKS
    for idx, ch_id in enumerate(cluster_heads):
        ch_x, ch_y = pos[ch_id]
        ax.plot([ch_x, sink_x], [ch_y, sink_y], '--', color='#d97706', alpha=0.85, linewidth=1.8, zorder=3, 
                label='RPL DODAG DAG Link (CH to Sink)' if idx == 0 else '')

    # 3. ESTABLISH TRIMET GRAPH OPTIMIZATION (TGO) TRIADIC CONNECTIONS AMONG ALL CLUSTER HEADS AND SINK NODE
    # Inter-CH Trimet Triangles (triadic mesh between CHs)
    inter_ch_tgo_edges = [
        (1, 4), (4, 8), (8, 44), (44, 26), (26, 15), (15, 1), # Ring of CHs
        (1, 26), (4, 26), (8, 26), # Spoke triads to central CH 26
        (15, 44) # Base triad
    ]
    for idx, (ch_a, ch_b) in enumerate(inter_ch_tgo_edges):
        pa, pb = pos[ch_a], pos[ch_b]
        ax.plot([pa[0], pb[0]], [pa[1], pb[1]], '-', color='#10b981', alpha=0.9, linewidth=2.0, zorder=4, 
                label='TGO Triad Connection (CH-to-CH Inter-Cluster)' if idx == 0 else '')

    # Draw Nodes as Blue Circles with White Numbers, CHs as Gold Stars
    for n_id, (x, y) in pos.items():
        if n_id in cluster_heads:
            # Cluster Head Mote (Gold Star / Dark Yellow Marker)
            ax.scatter(x, y, c='#f59e0b', s=270, zorder=6, edgecolors='#b45309', linewidth=1.5, label='Cluster Head (CH)' if n_id == cluster_heads[0] else '')
            ax.text(x, y, str(n_id), color='black', fontweight='bold', fontsize=8.0, ha='center', va='center', zorder=7)
        else:
            # Trimet Mote
            ax.scatter(x, y, c='#3b82f6', s=160, zorder=4, edgecolors='#1d4ed8', linewidth=1.0)
            ax.text(x, y, str(n_id), color='white', fontweight='bold', fontsize=6.5, ha='center', va='center', zorder=5)

    ax.legend(loc='upper right', fontsize=8.5, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    plt.title('Fig. 3. Representation of Lucas-based clustering with Trimet Graph Optimization (TGO) & RPL-UDP Sink Node', fontsize=11.5, fontweight='bold', pad=15, color='#1e293b')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'etasr_fig3_lucas_clustering.png'), bbox_inches='tight')
    plt.close()
    print("[+] SUCCESS: Generated Fig. 3 with Trimet Graph Optimization (TGO) among all Cluster Heads and RPL-UDP Sink Node!")

if __name__ == '__main__':
    generate_lucas_tgo_fig3()
