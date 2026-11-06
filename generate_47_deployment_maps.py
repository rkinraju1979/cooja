import os
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

base_dir = 'c:/Users/Kanaka Raju/Desktop/joy29'

plt.style.use('dark_background')

deployments = ['lucas47', 'hexagonal47', 'grid47', 'circular47', 'random47']
top_titles = {
    'lucas47': 'Lucas Series (2, 1, 3, 4, 7, 11, 18)',
    'hexagonal47': 'Hexagonal 47-Mote Deployment',
    'grid47': 'Grid 47-Mote Deployment (7x7)',
    'circular47': 'Circular 47-Mote Deployment',
    'random47': 'Random 47-Mote Deployment'
}

colors = {
    'lucas47': '#9b59b6',
    'hexagonal47': '#2ecc71',
    'grid47': '#3498db',
    'circular47': '#e74c3c',
    'random47': '#f1c40f'
}

coords = {}

# 1. Lucas Deployment following exact Lucas Series L_n = (2, 1, 3, 4, 7, 11, 18)
# Cumulative sum: 2 + 1 + 3 + 4 + 7 + 11 + 18 = 46 client motes + 1 sink = 47 total motes
lucas_series = [1, 3, 4, 7, 11, 18]  # Ring 0 has Sink Node 1 + Gateway Node 2
ring_radii   = [30.0, 55.0, 85.0, 120.0, 160.0, 205.0]

lucas_x, lucas_y = [0.0, 15.0], [0.0, 0.0]  # Sink (0,0) and Node 2 (15,0)

for ring_idx, n_nodes in enumerate(lucas_series):
    r = ring_radii[ring_idx]
    phase_offset = (ring_idx * 137.508) * (np.pi / 180.0)
    angles = np.linspace(0, 2 * np.pi, n_nodes, endpoint=False) + phase_offset
    for a in angles:
        lucas_x.append(r * np.cos(a))
        lucas_y.append(r * np.sin(a))

coords['lucas47'] = (lucas_x[:47], lucas_y[:47])

# 2. Hexagonal 47-Mote
hex_x, hex_y = [0.0], [0.0]
ring = 1
while len(hex_x) < 47:
    for i in range(6 * ring):
        if len(hex_x) >= 47: break
        angle = i * (2 * np.pi / (6 * ring))
        r = ring * 35.0
        hex_x.append(r * np.cos(angle))
        hex_y.append(r * np.sin(angle))
    ring += 1
coords['hexagonal47'] = (hex_x[:47], hex_y[:47])

# 3. Grid 47-Mote (7x7)
grid_coords = []
for row in range(-3, 4):
    for col in range(-3, 4):
        grid_coords.append((col * 30.0, row * 30.0))
grid_coords.sort(key=lambda p: p[0]**2 + p[1]**2)
grid_coords = grid_coords[:47]
coords['grid47'] = ([p[0] for p in grid_coords], [p[1] for p in grid_coords])

# 4. Circular 47-Mote
circ_x, circ_y = [0.0], [0.0]
ring_sizes = [8, 16, 22]
ring_radii_circ = [40.0, 80.0, 120.0]
for r_idx, n_nodes in enumerate(ring_sizes):
    r = ring_radii_circ[r_idx]
    for i in range(n_nodes):
        if len(circ_x) >= 47: break
        angle = i * (2 * np.pi / n_nodes)
        circ_x.append(r * np.cos(angle))
        circ_y.append(r * np.sin(angle))
coords['circular47'] = (circ_x[:47], circ_y[:47])

# 5. Random 47-Mote
np.random.seed(42)
rand_x = [0.0] + list(np.random.uniform(-140, 140, 46))
rand_y = [0.0] + list(np.random.uniform(-140, 140, 46))
coords['random47'] = (rand_x[:47], rand_y[:47])

# Render combined 5-Deployment Map for 47 Motes
fig, axes = plt.subplots(1, 5, figsize=(22, 4.5))

for idx, top in enumerate(deployments):
    ax = axes[idx]
    x, y = coords[top]
    
    # Plot client motes (Nodes 2 to 47)
    ax.scatter(x[1:], y[1:], c=colors[top], s=60, alpha=0.85, edgecolors='white', linewidths=0.8, label='Client Motes (2-47)')
    # Plot RPL Root Sink (Node 1)
    ax.scatter([x[0]], [y[0]], c='#e74c3c', s=160, marker='*', edgecolors='white', linewidths=1.5, label='RPL Root Sink (1)', zorder=5)
    
    # Draw connection lines for Lucas deployment rings
    if top == 'lucas47':
        for r_val in ring_radii:
            circle = plt.Circle((0, 0), r_val, color='#9b59b6', fill=False, linestyle='--', alpha=0.25, linewidth=0.8)
            ax.add_patch(circle)
            
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            dist = np.hypot(x[i]-x[j], y[i]-y[j])
            if dist < 65.0:
                ax.plot([x[i], x[j]], [y[i], y[j]], color=colors[top], alpha=0.15, linewidth=0.8)
                
    ax.set_title(top_titles[top], fontsize=10, fontweight='bold', pad=10)
    ax.set_xlabel('X (meters)', fontsize=9)
    if idx == 0:
        ax.set_ylabel('Y (meters)', fontsize=9)
    ax.grid(True, linestyle='--', alpha=0.2)
    ax.set_aspect('equal')

fig.suptitle('Spatial Network Deployment Comparison (Lucas Series L_n = 2, 1, 3, 4, 7, 11, 18 - 47 Motes Total)', fontsize=13, fontweight='bold', y=1.03)
plt.tight_layout()
map_path = os.path.join(base_dir, 'deployment_all_5_comparison.png')
plt.savefig(map_path, dpi=250, bbox_inches='tight')
plt.close(fig)
print(f"[+] Saved Lucas Series (2,1,3,4,7,11,18) 47-Mote Spatial Deployment Map: {map_path}")
