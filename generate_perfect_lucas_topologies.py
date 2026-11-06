import os
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

base_dir = 'c:/Users/Kanaka Raju/Desktop/joy29'

plt.style.use('dark_background')

# Generate exact Lucas Series Cluster Deployments for 29 Motes & 47 Motes
# Lucas Clusters L_n: (2, 1, 3, 4, 7, 11) for 29 Motes, (2, 1, 3, 4, 7, 11, 18) for 47 Motes

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5))

# ------------------------------------------------------------------------------
# 1. 29 MOTES LUCAS CLUSTER DEPLOYMENT
# Clusters: L_0=2, L_1=1, L_2=3, L_3=4, L_4=7, L_5=11 -> Sum = 28 Clients + 1 Sink = 29 Motes
# ------------------------------------------------------------------------------
lucas_clusters_29 = [2, 1, 3, 4, 7, 11]
cluster_radii_29 = [25.0, 45.0, 70.0, 100.0, 135.0, 175.0]

x29, y29 = [0.0], [0.0] # Node 1 (Sink)
for c_idx, n_motes in enumerate(lucas_clusters_29):
    r = cluster_radii_29[c_idx]
    phase = c_idx * (137.508 * np.pi / 180.0)
    angles = np.linspace(0, 2 * np.pi, n_motes, endpoint=False) + phase
    for a in angles:
        x29.append(r * np.cos(a))
        y29.append(r * np.sin(a))

ax1.scatter(x29[1:], y29[1:], c='#9b59b6', s=70, alpha=0.85, edgecolors='white', linewidths=0.8, label='Client Motes (2-29)')
ax1.scatter([x29[0]], [y29[0]], c='#e74c3c', s=180, marker='*', edgecolors='white', linewidths=1.5, label='RPL Root Sink (Node 1)', zorder=5)

for r_val in cluster_radii_29:
    circle = plt.Circle((0, 0), r_val, color='#9b59b6', fill=False, linestyle='--', alpha=0.3, linewidth=0.9)
    ax1.add_patch(circle)

# RPL Multi-Hop Routing Connections to Sink
for i in range(1, 29):
    ax1.plot([x29[i], x29[0]], [y29[i], y29[0]], color='#9b59b6', alpha=0.1, linewidth=0.6)

ax1.set_title('29-Mote Lucas Cluster Deployment\n(Clusters: 2 + 1 + 3 + 4 + 7 + 11 = 28 Clients + 1 Sink)', fontsize=11, fontweight='bold', pad=12)
ax1.set_xlabel('X Position (meters)', fontsize=9)
ax1.set_ylabel('Y Position (meters)', fontsize=9)
ax1.legend(frameon=True, facecolor='#151b26', edgecolor='#263347', loc='upper right')
ax1.grid(True, linestyle='--', alpha=0.2)
ax1.set_aspect('equal')

# ------------------------------------------------------------------------------
# 2. 47 MOTES LUCAS CLUSTER DEPLOYMENT
# Clusters: L_0=2, L_1=1, L_2=3, L_3=4, L_4=7, L_5=11, L_6=18 -> Sum = 46 Clients + 1 Sink = 47 Motes
# ------------------------------------------------------------------------------
lucas_clusters_47 = [2, 1, 3, 4, 7, 11, 18]
cluster_radii_47 = [25.0, 45.0, 70.0, 100.0, 135.0, 175.0, 220.0]

x47, y47 = [0.0], [0.0] # Node 1 (Sink)
for c_idx, n_motes in enumerate(lucas_clusters_47):
    r = cluster_radii_47[c_idx]
    phase = c_idx * (137.508 * np.pi / 180.0)
    angles = np.linspace(0, 2 * np.pi, n_motes, endpoint=False) + phase
    for a in angles:
        x47.append(r * np.cos(a))
        y47.append(r * np.sin(a))

ax2.scatter(x47[1:], y47[1:], c='#9b59b6', s=70, alpha=0.85, edgecolors='white', linewidths=0.8, label='Client Motes (2-47)')
ax2.scatter([x47[0]], [y47[0]], c='#e74c3c', s=180, marker='*', edgecolors='white', linewidths=1.5, label='RPL Root Sink (Node 1)', zorder=5)

for r_val in cluster_radii_47:
    circle = plt.Circle((0, 0), r_val, color='#9b59b6', fill=False, linestyle='--', alpha=0.3, linewidth=0.9)
    ax2.add_patch(circle)

# RPL Multi-Hop Routing Connections to Sink
for i in range(1, 47):
    ax2.plot([x47[i], x47[0]], [y47[i], y47[0]], color='#9b59b6', alpha=0.1, linewidth=0.6)

ax2.set_title('47-Mote Lucas Cluster Deployment\n(Clusters: 2 + 1 + 3 + 4 + 7 + 11 + 18 = 46 Clients + 1 Sink)', fontsize=11, fontweight='bold', pad=12)
ax2.set_xlabel('X Position (meters)', fontsize=9)
ax2.set_ylabel('Y Position (meters)', fontsize=9)
ax2.legend(frameon=True, facecolor='#151b26', edgecolor='#263347', loc='upper right')
ax2.grid(True, linestyle='--', alpha=0.2)
ax2.set_aspect('equal')

plt.suptitle('Exact Lucas Series Cluster Deployment (RPL-UDP Interconnected to Sink Node 1)', fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()

map_path = os.path.join(base_dir, 'lucas_29_vs_47_perfect_map.png')
plt.savefig(map_path, dpi=250, bbox_inches='tight')
plt.close(fig)
print(f"[+] Saved Perfect Lucas Cluster Map (29 Motes vs 47 Motes): {map_path}")
