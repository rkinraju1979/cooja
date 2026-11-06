import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = script_dir if script_dir else os.getcwd()

print("[+] Generating Figure 1 Cluster Deployment Density Comparison Maps...")

plt.style.use('dark_background')

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
((ax_low, ax_med), (ax_high, ax_lucas)) = axes

# --- 1. Low Density Clustering (a): 20 clusters x 5 nodes ---
ax_low.set_title('(a) Low Density Clustering (20 x 5 Nodes)', fontsize=11, fontweight='bold', color='#3498db', pad=10)
np.random.seed(101)
cluster_centers_low = []
for r in range(4):
    for c in range(5):
        cluster_centers_low.append((c * 100 + np.random.uniform(-10, 10), r * 100 + np.random.uniform(-10, 10)))

sink_low_x, sink_low_y = 200.0, 420.0
ax_low.scatter([sink_low_x], [sink_low_y], c='#e74c3c', s=220, marker='*', zorder=7, edgecolors='white', linewidths=1.5, label='RPL Root Sink (Node 1)')

for h_idx, (cx, cy) in enumerate(cluster_centers_low):
    # Cluster Head (CH)
    ax_low.scatter([cx], [cy], c='#f1c40f', s=65, marker='*', zorder=6, edgecolors='white', linewidths=0.8)
    # CH-to-Sink Backbone Link
    ax_low.plot([cx, sink_low_x], [cy, sink_low_y], color='#f1c40f', linestyle='--', linewidth=0.9, alpha=0.5, label='CH-to-Sink Backbone' if h_idx==0 else '')
    # Intra-cluster CM-to-CH links
    for i in range(4):
        angle = i * (2 * np.pi / 4.0) + np.random.uniform(-0.2, 0.2)
        lx = cx + 22.0 * np.cos(angle)
        ly = cy + 22.0 * np.sin(angle)
        ax_low.scatter([lx], [ly], c='#3498db', s=25, alpha=0.9)
        ax_low.plot([cx, lx], [cy, ly], color='#3498db', alpha=0.35, linewidth=0.8)

ax_low.legend(loc='upper right', fontsize=8, frameon=True, facecolor='#151b26', edgecolor='#263347')
ax_low.set_aspect('equal')
ax_low.axis('off')

# --- 2. Medium Density Clustering (b): 5 clusters x 20 nodes ---
ax_med.set_title('(b) Medium Density Clustering (5 x 20 Nodes)', fontsize=11, fontweight='bold', color='#f1c40f', pad=10)
colors_med = ['#9b59b6', '#2ecc71', '#3498db', '#e74c3c', '#f1c40f']
med_hubs = [(150, 150), (450, 150), (300, 350), (150, 550), (450, 550)]

sink_med_x, sink_med_y = 300.0, 670.0
ax_med.scatter([sink_med_x], [sink_med_y], c='#e74c3c', s=240, marker='*', zorder=7, edgecolors='white', linewidths=1.5, label='RPL Root Sink (Node 1)')

for h_idx, (cx, cy) in enumerate(med_hubs):
    c_col = colors_med[h_idx]
    # Cluster Head (CH)
    ax_med.scatter([cx], [cy], c='#f1c40f', s=140, marker='*', zorder=6, edgecolors='white', linewidths=1.2)
    # CH-to-Sink Backbone Link
    ax_med.plot([cx, sink_med_x], [cy, sink_med_y], color='#f1c40f', linestyle='--', linewidth=1.8, alpha=0.85, label='CH-to-Sink Backbone' if h_idx==0 else '')
    # Intra-cluster CM-to-CH links
    for i in range(19):
        angle = i * (2 * np.pi / 19.0)
        lx = cx + 60.0 * np.cos(angle)
        ly = cy + 60.0 * np.sin(angle)
        ax_med.scatter([lx], [ly], c=c_col, s=35, alpha=0.8, edgecolors='white', linewidths=0.4)
        ax_med.plot([cx, lx], [cy, ly], color=c_col, alpha=0.35, linewidth=1.0)

ax_med.legend(loc='upper right', fontsize=8, frameon=True, facecolor='#151b26', edgecolor='#263347')
ax_med.set_aspect('equal')
ax_med.axis('off')

# --- 3. High Density Clustering (c): 2 clusters x 50 nodes ---
ax_high.set_title('(c) High Density Clustering (2 x 50 Nodes)', fontsize=11, fontweight='bold', color='#e74c3c', pad=10)
high_hubs = [(200, 300), (600, 300)]
colors_high = ['#e74c3c', '#9b59b6']

sink_high_x, sink_high_y = 400.0, 520.0
ax_high.scatter([sink_high_x], [sink_high_y], c='#e74c3c', s=260, marker='*', zorder=7, edgecolors='white', linewidths=1.5, label='RPL Root Sink (Node 1)')

for h_idx, (cx, cy) in enumerate(high_hubs):
    c_col = colors_high[h_idx]
    # Cluster Head (CH)
    ax_high.scatter([cx], [cy], c='#f1c40f', s=180, marker='*', zorder=6, edgecolors='white', linewidths=1.5)
    # CH-to-Sink Backbone Link
    ax_high.plot([cx, sink_high_x], [cy, sink_high_y], color='#f1c40f', linestyle='--', linewidth=2.0, alpha=0.9, label='CH-to-Sink Backbone' if h_idx==0 else '')
    # Intra-cluster CM-to-CH links
    for i in range(49):
        angle = i * (2 * np.pi / 49.0)
        r = 110.0 + (i % 2) * 20.0
        lx = cx + r * np.cos(angle)
        ly = cy + r * np.sin(angle)
        ax_high.scatter([lx], [ly], c=c_col, s=30, alpha=0.75, edgecolors='white', linewidths=0.3)
        ax_high.plot([cx, lx], [cy, ly], color=c_col, alpha=0.25, linewidth=0.8)

ax_high.legend(loc='upper right', fontsize=8, frameon=True, facecolor='#151b26', edgecolor='#263347')
ax_high.set_aspect('equal')
ax_high.axis('off')

# --- 4. Lucas Adaptive Clustering (d): 100 Clients (9 Lucas Clusters) + 1 Dedicated Sink = 101 Motes Total ---
ax_lucas.set_title('(d) Lucas Adaptive Clustering [TOP PERFORMER: LASS 89.9% Energy Savings]', fontsize=11, fontweight='bold', color='#2ecc71', pad=10)
lucas_sizes = [2, 1, 3, 4, 7, 11, 18, 29, 25]
lucas_centers = [
    (100, 100), (300, 100), (520, 100),
    (100, 320), (300, 320), (520, 320),
    (100, 540), (310, 540), (530, 540)
]
lucas_colors = ['#2ecc71', '#1abc9c', '#3498db', '#9b59b6', '#e74c3c', '#f1c40f', '#e67e22', '#fd79a8', '#a29bfe']

# Dedicated RPL Root Sink (Node 1) at Top-Center (310, 670)
sink_x, sink_y = 310.0, 670.0
ax_lucas.scatter([sink_x], [sink_y], c='#e74c3c', s=260, marker='*', zorder=8, edgecolors='white', linewidths=1.8, label='RPL Root Sink (Node 1)')
ax_lucas.text(sink_x, sink_y + 25, "RPL Root Sink (Node 1)", color='#ff7675', fontsize=9, fontweight='bold', ha='center')

for idx, n_nodes in enumerate(lucas_sizes):
    cx, cy = lucas_centers[idx]
    c_col = lucas_colors[idx]
    
    # Cluster Head (CH) Node - Gold Star Marker
    ax_lucas.scatter([cx], [cy], c='#f1c40f', s=140, marker='*', zorder=6, edgecolors='white', linewidths=1.0)
    
    # Direct CH-to-Sink Backbone Link (Highlighting RPL DODAG link between Sink and Cluster Head 26)
    is_ch26 = (idx == 7 or n_nodes == 29)
    link_label = 'RPL DODAG Link (Sink to CH 26)' if is_ch26 else ('CH-to-Sink Backbone' if idx==0 else '')
    link_width = 2.2 if is_ch26 else 1.5
    link_alpha = 0.95 if is_ch26 else 0.75
    link_color = '#e74c3c' if is_ch26 else '#f1c40f'
    ax_lucas.plot([cx, sink_x], [cy, sink_y], color=link_color, linestyle='--', linewidth=link_width, zorder=5 if is_ch26 else 4, alpha=link_alpha, label=link_label)

    r_radius = 22.0 + n_nodes * 1.1
    if n_nodes > 1:
        for i in range(n_nodes - 1):
            angle = i * (2 * np.pi / (n_nodes - 1))
            lx = cx + r_radius * np.cos(angle)
            ly = cy + r_radius * np.sin(angle)
            # Cluster Member (CM) Node
            ax_lucas.scatter([lx], [ly], c=c_col, s=28, alpha=0.85, edgecolors='white', linewidths=0.4)
            # CM-to-CH Intra-Cluster Transmission Link
            ax_lucas.plot([cx, lx], [cy, ly], color=c_col, alpha=0.35, linewidth=0.8)
    
    # Label L_n cluster size & CH ID
    offset_y = (r_radius + 15) if n_nodes > 1 else 18
    ax_lucas.text(cx, cy - offset_y, f"CH_{idx} (L_{idx}={n_nodes})" + (" [CH 26]" if is_ch26 else ""), color='white', fontsize=7.5, fontweight='bold', ha='center')

ax_lucas.legend(loc='upper right', fontsize=8, frameon=True, facecolor='#151b26', edgecolor='#263347')
ax_lucas.set_aspect('equal')
ax_lucas.axis('off')

output_dir = os.path.join(base_dir, 'output')
os.makedirs(output_dir, exist_ok=True)

plt.tight_layout()
fig_cluster_path = os.path.join(base_dir, "clustering_density_fig1.png")
fig_cluster_out_path = os.path.join(output_dir, "clustering_density_fig1.png")
plt.savefig(fig_cluster_path, dpi=200, bbox_inches='tight')
plt.savefig(fig_cluster_out_path, dpi=200, bbox_inches='tight')
plt.close(fig)

print(f"[+] Saved Figure 1 Cluster Deployment Density Map to {fig_cluster_out_path}")
