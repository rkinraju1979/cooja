# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import numpy as np

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"
output_dir = os.path.join(base_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set style
plt.style.use('dark_background')
fig_bg = '#0b0e14'
ax_bg = '#111622'
text_color = '#e2e8f0'

plt.rcParams.update({
    'figure.facecolor': fig_bg,
    'axes.facecolor': ax_bg,
    'axes.edgecolor': '#2a3447',
    'axes.labelcolor': text_color,
    'xtick.color': '#94a3b8',
    'ytick.color': '#94a3b8',
    'text.color': text_color,
    'font.family': 'sans-serif',
    'font.size': 10
})

nodes = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100])

# Helper function to save to both base_dir and output_dir
def save_dual(filename):
    p1 = os.path.join(base_dir, filename)
    p2 = os.path.join(output_dir, filename)
    plt.savefig(p1, bbox_inches='tight')
    plt.savefig(p2, bbox_inches='tight')
    print("[+] Saved: " + str(p1) + " AND " + str(p2))

# 1. Dynamic Comparison 1 (ETASR Fig. 7) - Exact Paper Match
plt.figure(figsize=(9, 5), dpi=200)
c_tree1 = np.array([4.0, 5.0, 6.0, 5.5, 4.8, 5.2, 5.0, 6.0, 6.0])
l_tgo1  = np.array([5.0, 6.0, 7.0, 8.0, 8.8, 9.5, 10.0, 11.2, 6.0])
e_tgo1  = np.array([4.0, 5.0, 6.0, 6.0, 6.2, 6.8, 8.0, 7.0, 6.0])
mesh1   = np.array([4.0, 5.0, 6.0, 7.2, 7.8, 8.0, 7.2, 6.5, 6.0])

plt.plot(nodes, c_tree1, 'o-', color='#3498db', label='Cluster Tree', linewidth=2, markersize=6)
plt.plot(nodes, l_tgo1, 's-', color='#ff9f43', label='Lucas TGO Unequal Clustering', linewidth=2.5, markersize=7)
plt.plot(nodes, e_tgo1, '^--', color='#10ac84', label='Equal Clustering of TGO', linewidth=2, markersize=6)
plt.plot(nodes, mesh1, 'd:', color='#ee5253', label='Mesh Clustering', linewidth=2, markersize=6)

plt.title('Dynamic Comparison 1: Survivability vs Nodes (ETASR Fig. 7)', fontsize=13, fontweight='bold', pad=15, color='#9b59b6')
plt.xlabel('Nodes', fontsize=11, fontweight='bold')
plt.ylabel('Rounds', fontsize=11, fontweight='bold')
plt.ylim(3.5, 12.0)
plt.grid(True, linestyle='--', alpha=0.3, color='#2a3447')
plt.legend(frameon=True, facecolor='#151b26', edgecolor='#2a3447')
plt.tight_layout()
save_dual('etasr_fig7_comparison1.png')
plt.close()

# 2. Dynamic Comparison 2 (ETASR Fig. 8) - Exact Paper Match
plt.figure(figsize=(9, 5), dpi=200)
c_tree2 = np.array([5.0, 5.0, 5.0, 6.0, 5.0, 5.0, 6.0, 6.0, 7.0])
l_tgo2  = np.array([5.0, 6.0, 7.0, 8.0, 8.0, 8.0, 8.5, 9.0, 9.0])
e_tgo2  = np.array([5.0, 5.0, 5.0, 6.0, 5.0, 5.5, 6.0, 6.0, 6.0])
mesh2   = np.array([5.0, 5.0, 6.0, 5.0, 5.0, 5.5, 6.0, 6.0, 7.0])

plt.plot(nodes, c_tree2, 'o-', color='#3498db', label='Cluster Tree', linewidth=2)
plt.plot(nodes, l_tgo2, 's-', color='#ff9f43', label='Lucas TGO Unequal Clustering', linewidth=2.5)
plt.plot(nodes, e_tgo2, '^--', color='#10ac84', label='Equal Clustering of TGO', linewidth=2)
plt.plot(nodes, mesh2, 'd:', color='#ee5253', label='Mesh Clustering', linewidth=2)

plt.title('Dynamic Comparison 2: Network Survivability (ETASR Fig. 8)', fontsize=13, fontweight='bold', pad=15, color='#9b59b6')
plt.xlabel('Nodes', fontsize=11, fontweight='bold')
plt.ylabel('Rounds', fontsize=11, fontweight='bold')
plt.ylim(4.5, 9.5)
plt.grid(True, linestyle='--', alpha=0.3, color='#2a3447')
plt.legend(frameon=True, facecolor='#151b26', edgecolor='#2a3447')
plt.tight_layout()
save_dual('etasr_fig8_comparison2.png')
plt.close()

# 3. Dynamic Comparison 3 (ETASR Fig. 9) - Exact Paper Match
plt.figure(figsize=(9, 5), dpi=200)
c_tree3 = np.array([5.0, 5.0, 6.0, 6.0, 6.0, 6.0, 7.0, 5.5, 6.0])
l_tgo3  = np.array([5.0, 5.5, 6.2, 7.8, 7.0, 6.5, 7.5, 6.0, 9.0])
e_tgo3  = np.array([5.0, 5.0, 6.0, 5.2, 5.0, 6.8, 5.0, 5.2, 6.0])
mesh3   = np.array([5.0, 5.0, 7.5, 7.0, 6.0, 6.0, 6.5, 5.0, 5.0])

plt.plot(nodes, c_tree3, 'o-', color='#3498db', label='Cluster Tree', linewidth=2)
plt.plot(nodes, l_tgo3, 's-', color='#ff9f43', label='Lucas TGO Unequal Clustering', linewidth=2.5)
plt.plot(nodes, e_tgo3, '^--', color='#10ac84', label='Equal Clustering of TGO', linewidth=2)
plt.plot(nodes, mesh3, 'd:', color='#ee5253', label='Mesh Clustering', linewidth=2)

plt.title('Dynamic Comparison 3: Network Survivability (ETASR Fig. 9)', fontsize=13, fontweight='bold', pad=15, color='#9b59b6')
plt.xlabel('Nodes', fontsize=11, fontweight='bold')
plt.ylabel('Rounds', fontsize=11, fontweight='bold')
plt.ylim(4.5, 9.5)
plt.grid(True, linestyle='--', alpha=0.3, color='#2a3447')
plt.legend(frameon=True, facecolor='#151b26', edgecolor='#2a3447')
plt.tight_layout()
save_dual('etasr_fig9_comparison3.png')
plt.close()

# 4. Dynamic Comparison 4 (ETASR Fig. 10) - Exact Paper Match
plt.figure(figsize=(9, 5), dpi=200)
c_tree4 = np.array([5.0, 5.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0])
l_tgo4  = np.array([5.0, 5.5, 6.5, 8.0, 7.0, 6.0, 7.5, 9.0, 10.2])
e_tgo4  = np.array([5.0, 5.0, 6.0, 5.5, 5.0, 5.5, 7.0, 6.0, 5.5])
mesh4   = np.array([5.0, 5.0, 6.0, 7.5, 6.0, 6.0, 6.0, 5.0, 5.0])

plt.plot(nodes, c_tree4, 'o-', color='#3498db', label='Cluster Tree', linewidth=2)
plt.plot(nodes, l_tgo4, 's-', color='#ff9f43', label='Lucas TGO Unequal Clustering', linewidth=2.5)
plt.plot(nodes, e_tgo4, '^--', color='#10ac84', label='Equal Clustering of TGO', linewidth=2)
plt.plot(nodes, mesh4, 'd:', color='#ee5253', label='Mesh Clustering', linewidth=2)

plt.title('Dynamic Comparison 4: Network Survivability (ETASR Fig. 10)', fontsize=13, fontweight='bold', pad=15, color='#9b59b6')
plt.xlabel('Nodes', fontsize=11, fontweight='bold')
plt.ylabel('Rounds', fontsize=11, fontweight='bold')
plt.ylim(4.5, 11.0)
plt.grid(True, linestyle='--', alpha=0.3, color='#2a3447')
plt.legend(frameon=True, facecolor='#151b26', edgecolor='#2a3447')
plt.tight_layout()
save_dual('etasr_fig10_comparison4.png')
plt.close()

# 5. Consolidated Comparison Across 18 Experiments (ETASR Fig. 11) - Exact Paper Match
plt.figure(figsize=(10, 5), dpi=200)
experiments = np.arange(0, 19)
exp_c_tree = np.array([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])
exp_l_tgo  = np.array([9, 9, 9, 9, 9, 8, 9, 10, 9, 12, 10, 11, 9, 10, 8, 9, 9, 9, 10])
exp_e_tgo  = np.array([6, 6, 6, 6, 7, 7, 7, 7, 6, 6, 6, 6, 7, 7, 7, 7, 6, 6, 6])
exp_mesh   = np.array([7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6])

plt.plot(experiments, exp_c_tree, 'o-', color='#3498db', label='Cluster Tree', linewidth=2, markersize=5)
plt.plot(experiments, exp_l_tgo, 's-', color='#ff9f43', label='Lucas TGO Unequal Clustering', linewidth=2.5, markersize=6)
plt.plot(experiments, exp_e_tgo, '^--', color='#10ac84', label='Equal Clustering of TGO', linewidth=2, markersize=5)
plt.plot(experiments, exp_mesh, 'x:', color='#8395a7', label='Mesh Clustering', linewidth=2, markersize=5)

plt.title('SURVIVABILITY\nConsolidated Comparison of Different Smart Home Topologies (ETASR Fig. 11)', fontsize=13, fontweight='bold', pad=15, color='#2ecc71')
plt.xlabel('Experiments', fontsize=11, fontweight='bold')
plt.ylabel('Rounds', fontsize=11, fontweight='bold')
plt.xticks(np.arange(0, 19, 2))
plt.yticks(np.arange(0, 16, 2))
plt.ylim(0, 15)
plt.grid(True, linestyle='--', alpha=0.3, color='#2a3447')
plt.legend(frameon=True, facecolor='#151b26', edgecolor='#2a3447', loc='upper right')
plt.tight_layout()
save_dual('etasr_fig11_consolidated.png')
plt.close()

# 6. Topologies Overview Diagram (Fig 3-6)
fig, axs = plt.subplots(2, 2, figsize=(10, 9), dpi=200)

# (a) Cluster Tree (StarOfStars)
ax = axs[0, 0]
ax.set_facecolor(ax_bg)
ax.set_title('Cluster Tree Topology (StarOfStars)', color='#3498db', fontweight='bold')
ax.plot([0, 0], [0, 0], 'o', color='#9b59b6', markersize=12)
for angle in np.linspace(0, 2*np.pi, 6, endpoint=False):
    x, y = np.cos(angle)*3, np.sin(angle)*3
    ax.plot([0, x], [0, y], '-', color='#3498db', alpha=0.6)
    ax.plot(x, y, 'o', color='#3498db', markersize=8)
    for sub_a in np.linspace(0, 2*np.pi, 4, endpoint=False):
        sx, sy = x + np.cos(sub_a)*1, y + np.sin(sub_a)*1
        ax.plot([x, sx], [y, sy], '--', color='#3498db', alpha=0.3)
        ax.plot(sx, sy, '.', color='#94a3b8', markersize=4)
ax.set_axis_off()

# (b) Mesh Network
ax = axs[0, 1]
ax.set_facecolor(ax_bg)
ax.set_title('Mesh Network Topology', color='#ee5253', fontweight='bold')
np.random.seed(42)
m_x = np.random.uniform(-4, 4, 15)
m_y = np.random.uniform(-4, 4, 15)
for i in range(15):
    for j in range(i+1, 15):
        dist = np.sqrt((m_x[i]-m_x[j])**2 + (m_y[i]-m_y[j])**2)
        if dist < 3.5:
            ax.plot([m_x[i], m_x[j]], [m_y[i], m_y[j]], '-', color='#ee5253', alpha=0.3)
ax.plot(m_x, m_y, 'o', color='#ee5253', markersize=7)
ax.set_axis_off()

# (c) TGO Mesh Network (TrimetOfStars)
ax = axs[1, 0]
ax.set_facecolor(ax_bg)
ax.set_title('Equal TGO Mesh Topology (TrimetOfTrimet)', color='#10ac84', fontweight='bold')
tri_centers = [(-2.5, -2), (2.5, -2), (0, 2.5)]
for cx, cy in tri_centers:
    ax.plot(cx, cy, 's', color='#10ac84', markersize=10)
    for sub_a in np.linspace(0, 2*np.pi, 3, endpoint=False):
        tx, ty = cx + np.cos(sub_a)*1.5, cy + np.sin(sub_a)*1.5
        ax.plot([cx, tx], [cy, ty], '-', color='#10ac84', alpha=0.6)
        ax.plot(tx, ty, 'o', color='#10ac84', markersize=6)
for i in range(3):
    for j in range(i+1, 3):
        ax.plot([tri_centers[i][0], tri_centers[j][0]], [tri_centers[i][1], tri_centers[j][1]], 'w--', alpha=0.5)
ax.set_axis_off()

# (d) Lucas TGO Unequal Clustering (Proposed Winner)
ax = axs[1, 1]
ax.set_facecolor(ax_bg)
ax.set_title('Lucas TGO Unequal Clustering (Proposed Winner)', color='#ff9f43', fontweight='bold')
lucas_r = [1, 2, 3, 4]
lucas_angles = [0, np.pi/2, np.pi, 3*np.pi/2]
l_centers = []
for i in range(4):
    lx, ly = np.cos(lucas_angles[i])*lucas_r[i]*1.2, np.sin(lucas_angles[i])*lucas_r[i]*1.2
    l_centers.append((lx, ly))
    n_nodes = [3, 4, 7, 11][i]
    ax.plot(lx, ly, 'p', color='#ff9f43', markersize=12)
    for k in range(n_nodes):
        sa = (2*np.pi / n_nodes) * k
        nx, ny = lx + np.cos(sa)*(0.6 + 0.1*i), ly + np.sin(sa)*(0.6 + 0.1*i)
        ax.plot([lx, nx], [ly, ny], '-', color='#ff9f43', alpha=0.5)
        ax.plot(nx, ny, 'o', color='#f1c40f', markersize=5)

for i in range(len(l_centers)):
    for j in range(i+1, len(l_centers)):
        ax.plot([l_centers[i][0], l_centers[j][0]], [l_centers[i][1], l_centers[j][1]], '-', color='#ff9f43', alpha=0.7, linewidth=1.5)

ax.set_axis_off()
plt.suptitle('Figure 3–6. Topology Representations Evaluated in ETASR 2025 Study', fontsize=14, fontweight='bold', color='#9b59b6', y=0.98)
plt.tight_layout()
save_dual('etasr_fig3_6_topologies.png')
plt.close()

print("[+] RECHECK & REBUILD COMPLETE: Generated exact ETASR 2025 paper plots in output folder!")
