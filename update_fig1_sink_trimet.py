import os
import matplotlib.pyplot as plt
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"

plt.style.use('dark_background')

def generate_figure1_clustering_with_sink_trimet():
    print("[+] Rebuilding Figure 1 with explicit Sink Mote and Trimet Graph Connections among all clusters...")
    fig, axes = plt.subplots(2, 2, figsize=(14, 12), dpi=200)
    ((ax_low, ax_med), (ax_high, ax_lucas)) = axes

    # (a) Low Density: 20 clusters x 5 nodes + Sink Mote
    ax_low.set_title('(a) Low Density Clustering (20 x 5 Nodes)', fontsize=11, fontweight='bold', color='#3498db', pad=10)
    np.random.seed(101)
    cluster_centers_low = [(c * 100 + np.random.uniform(-10, 10), r * 100 + np.random.uniform(-10, 10)) for r in range(4) for c in range(5)]
    sink_low_x, sink_low_y = 200.0, 440.0
    
    # Sink Mote
    ax_low.scatter([sink_low_x], [sink_low_y], c='#e74c3c', s=260, marker='*', zorder=8, edgecolors='white', linewidths=1.5, label='Sink Mote (RPL Root)')
    ax_low.text(sink_low_x, sink_low_y + 22, "Sink Mote", color='#ff7675', fontsize=9, fontweight='bold', ha='center')

    for h_idx, (cx, cy) in enumerate(cluster_centers_low):
        ax_low.scatter([cx], [cy], c='#f1c40f', s=65, marker='*', zorder=6, edgecolors='white', linewidths=0.8)
        ax_low.plot([cx, sink_low_x], [cy, sink_low_y], color='#f1c40f', linestyle='--', linewidth=0.9, alpha=0.5)
        for i in range(4):
            ang = i * (2 * np.pi / 4.0) + np.random.uniform(-0.2, 0.2)
            lx, ly = cx + 22.0 * np.cos(ang), cy + 22.0 * np.sin(ang)
            ax_low.scatter([lx], [ly], c='#3498db', s=25, alpha=0.9)
            ax_low.plot([cx, lx], [cy, ly], color='#3498db', alpha=0.35, linewidth=0.8)
    ax_low.legend(loc='upper right', fontsize=8, frameon=True, facecolor='#151b26', edgecolor='#263347')
    ax_low.set_aspect('equal')
    ax_low.axis('off')

    # (b) Medium Density: 5 clusters x 20 nodes + Sink Mote
    ax_med.set_title('(b) Medium Density Clustering (5 x 20 Nodes)', fontsize=11, fontweight='bold', color='#f1c40f', pad=10)
    colors_med = ['#9b59b6', '#2ecc71', '#3498db', '#e74c3c', '#f1c40f']
    med_hubs = [(150, 150), (450, 150), (300, 350), (150, 550), (450, 550)]
    sink_med_x, sink_med_y = 300.0, 680.0
    
    # Sink Mote
    ax_med.scatter([sink_med_x], [sink_med_y], c='#e74c3c', s=280, marker='*', zorder=8, edgecolors='white', linewidths=1.5, label='Sink Mote (RPL Root)')
    ax_med.text(sink_med_x, sink_med_y + 25, "Sink Mote", color='#ff7675', fontsize=9, fontweight='bold', ha='center')

    for h_idx, (cx, cy) in enumerate(med_hubs):
        c_col = colors_med[h_idx]
        ax_med.scatter([cx], [cy], c='#f1c40f', s=140, marker='*', zorder=6, edgecolors='white', linewidths=1.2)
        ax_med.plot([cx, sink_med_x], [cy, sink_med_y], color='#f1c40f', linestyle='--', linewidth=1.8, alpha=0.85)
        for i in range(19):
            ang = i * (2 * np.pi / 19.0)
            lx, ly = cx + 60.0 * np.cos(ang), cy + 60.0 * np.sin(ang)
            ax_med.scatter([lx], [ly], c=c_col, s=35, alpha=0.8, edgecolors='white', linewidths=0.4)
            ax_med.plot([cx, lx], [cy, ly], color=c_col, alpha=0.35, linewidth=1.0)
    ax_med.legend(loc='upper right', fontsize=8, frameon=True, facecolor='#151b26', edgecolor='#263347')
    ax_med.set_aspect('equal')
    ax_med.axis('off')

    # (c) High Density: 2 clusters x 50 nodes + Sink Mote
    ax_high.set_title('(c) High Density Clustering (2 x 50 Nodes)', fontsize=11, fontweight='bold', color='#e74c3c', pad=10)
    high_hubs = [(200, 300), (600, 300)]
    colors_high = ['#e74c3c', '#9b59b6']
    sink_high_x, sink_high_y = 400.0, 540.0
    
    # Sink Mote
    ax_high.scatter([sink_high_x], [sink_high_y], c='#e74c3c', s=290, marker='*', zorder=8, edgecolors='white', linewidths=1.5, label='Sink Mote (RPL Root)')
    ax_high.text(sink_high_x, sink_high_y + 25, "Sink Mote", color='#ff7675', fontsize=9, fontweight='bold', ha='center')

    for h_idx, (cx, cy) in enumerate(high_hubs):
        c_col = colors_high[h_idx]
        ax_high.scatter([cx], [cy], c='#f1c40f', s=180, marker='*', zorder=6, edgecolors='white', linewidths=1.5)
        ax_high.plot([cx, sink_high_x], [cy, sink_high_y], color='#f1c40f', linestyle='--', linewidth=2.0, alpha=0.9)
        for i in range(49):
            ang = i * (2 * np.pi / 49.0)
            r = 110.0 + (i % 2) * 20.0
            lx, ly = cx + r * np.cos(ang), cy + r * np.sin(ang)
            ax_high.scatter([lx], [ly], c=c_col, s=30, alpha=0.75, edgecolors='white', linewidths=0.3)
            ax_high.plot([cx, lx], [cy, ly], color=c_col, alpha=0.25, linewidth=0.8)
    ax_high.legend(loc='upper right', fontsize=8, frameon=True, facecolor='#151b26', edgecolor='#263347')
    ax_high.set_aspect('equal')
    ax_high.axis('off')

    # (d) Lucas Adaptive Clustering with Trimet Graph Connections among ALL Clusters
    ax_lucas.set_title('(d) Lucas Adaptive Clustering with Trimet Graph Connections & Sink Mote', fontsize=11, fontweight='bold', color='#2ecc71', pad=10)
    lucas_sizes = [2, 1, 3, 4, 7, 11, 18, 29, 25]
    lucas_centers = [
        (100, 100), (300, 100), (520, 100),
        (100, 320), (300, 320), (520, 320),
        (100, 540), (310, 540), (530, 540)
    ]
    lucas_colors = ['#2ecc71', '#1abc9c', '#3498db', '#9b59b6', '#e74c3c', '#f1c40f', '#e67e22', '#fd79a8', '#a29bfe']
    
    # Explicit Sink Mote (Node 1 - RPL DODAG Root) at Top-Center (310, 680)
    sink_x, sink_y = 310.0, 680.0
    ax_lucas.scatter([sink_x], [sink_y], c='#ef4444', s=320, marker='*', zorder=10, edgecolors='white', linewidths=2.0, label='Sink Mote (RPL Root)')
    ax_lucas.text(sink_x, sink_y + 28, "Sink Mote (RPL Root)", color='#ff7675', fontsize=9.5, fontweight='bold', ha='center')

    # Draw Cluster Heads
    for idx, n_nodes in enumerate(lucas_sizes):
        cx, cy = lucas_centers[idx]
        c_col = lucas_colors[idx]
        
        # Cluster Head (CH) Node
        ax_lucas.scatter([cx], [cy], c='#f59e0b', s=140, marker='*', zorder=7, edgecolors='white', linewidths=1.0)
        
        # Direct CH-to-Sink RPL DODAG Links (Highlighting RPL DODAG Link between Sink and Cluster Head 26)
        is_ch26 = (idx == 7 or n_nodes == 29)
        link_label = 'RPL DODAG Link (Sink to CH 26)' if is_ch26 else ('CH-to-Sink Link' if idx==0 else '')
        link_width = 2.2 if is_ch26 else 1.2
        link_alpha = 0.95 if is_ch26 else 0.6
        link_color = '#e74c3c' if is_ch26 else '#f1c40f'
        ax_lucas.plot([cx, sink_x], [cy, sink_y], color=link_color, linestyle='--', linewidth=link_width, zorder=5 if is_ch26 else 3, alpha=link_alpha, label=link_label)

        r_radius = 22.0 + n_nodes * 1.1
        if n_nodes > 1:
            for i in range(n_nodes - 1):
                ang = i * (2 * np.pi / (n_nodes - 1))
                lx, ly = cx + r_radius * np.cos(ang), cy + r_radius * np.sin(ang)
                ax_lucas.scatter([lx], [ly], c=c_col, s=28, alpha=0.85, edgecolors='white', linewidths=0.4)
                # Intra-cluster trimet edges
                ax_lucas.plot([cx, lx], [cy, ly], color=c_col, alpha=0.35, linewidth=0.8)
        
        ax_lucas.text(cx, cy - (r_radius + 15), f"CH_{idx} (L_{idx}={n_nodes})" + (" [CH 26]" if is_ch26 else ""), color='white', fontsize=7.5, fontweight='bold', ha='center')

    # Draw Trimet Graph Optimization (TGO) Triangular Triad Connections AMONG ALL CLUSTERS
    trimet_cluster_triads = [
        (0, 1, 3), (1, 2, 5), (3, 4, 6), (4, 5, 7), (6, 7, 8), (0, 4, 8), (1, 4, 7), (2, 5, 8)
    ]
    for c1, c2, c3 in trimet_cluster_triads:
        p1, p2, p3 = lucas_centers[c1], lucas_centers[c2], lucas_centers[c3]
        ax_lucas.plot([p1[0], p2[0]], [p1[1], p2[1]], '-', color='#2ecc71', alpha=0.7, linewidth=1.5, zorder=4, label='Trimet Graph Connection' if c1==0 and c2==1 else '')
        ax_lucas.plot([p2[0], p3[0]], [p2[1], p3[1]], '-', color='#2ecc71', alpha=0.7, linewidth=1.5, zorder=4)
        ax_lucas.plot([p3[0], p1[0]], [p3[1], p1[1]], '-', color='#2ecc71', alpha=0.7, linewidth=1.5, zorder=4)

    ax_lucas.legend(loc='upper right', fontsize=8, frameon=True, facecolor='#151b26', edgecolor='#263347')
    ax_lucas.set_aspect('equal')
    ax_lucas.axis('off')

    plt.tight_layout()
    fig1_path = os.path.join(base_dir, "ijict_fig1_clustering.png")
    fig1_path2 = os.path.join(base_dir, "clustering_density_fig1.png")
    output_dir = os.path.join(base_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    fig1_path3 = os.path.join(output_dir, "clustering_density_fig1.png")
    
    plt.savefig(fig1_path, dpi=200, bbox_inches='tight')
    plt.savefig(fig1_path2, dpi=200, bbox_inches='tight')
    plt.savefig(fig1_path3, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"[+] Saved Figure 1 with RPL DODAG Link between Sink and Cluster Head 26")
    print(f"[+] Saved Figure 1 with Sink Mote & Trimet Graph Connections: {fig1_path}")

if __name__ == '__main__':
    generate_figure1_clustering_with_sink_trimet()
