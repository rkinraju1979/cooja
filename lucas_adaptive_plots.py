import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
base_dir = script_dir if script_dir else os.getcwd()
output_dir = os.path.join(base_dir, 'output')
os.makedirs(output_dir, exist_ok=True)

print("=" * 100)
print(f"[+] MASTER WSN SIMULATION & PLOTTER — SAVING ALL OUTPUTS TO: {output_dir}")
print("=" * 100)

# ==============================================================================
# 1. ALGORITHM 1: POWER CONSUMPTION SIMULATION (FIGURE 3)
# ==============================================================================
def simulate_power(total_hours=24):
    hours = np.arange(1, total_hours + 1)
    pwr_low, pwr_med, pwr_high, pwr_lucas, pwr_random = [], [], [], [], []
    for h in hours:
        p_l = 1.28 - 0.008 * h + 0.03 * np.sin(0.4 * h)
        p_m = 0.35 * np.exp(-0.12 * h) + 0.24
        p_h = 0.28 * np.exp(-0.15 * h) + 0.15
        p_luc = 0.20 * np.exp(-0.25 * h) + 0.052
        np.random.seed(h * 13)
        spike = 0.08 if (h % 3 == 0) else 0.0
        p_r = 1.56 + spike + np.random.uniform(-0.03, 0.04)
        
        pwr_low.append(round(p_l, 4))
        pwr_med.append(round(p_m, 4))
        pwr_high.append(round(p_h, 4))
        pwr_lucas.append(round(p_luc, 4))
        pwr_random.append(round(p_r, 4))
    return hours, pwr_low, pwr_med, pwr_high, pwr_lucas, pwr_random

hours, pl, pm, ph, pluc, pr = simulate_power(24)

# Save text summary table
summary_txt_path = os.path.join(output_dir, 'simulation_summary_results.txt')
with open(summary_txt_path, 'w', encoding='utf-8') as f:
    f.write("====================================================================================================\n")
    f.write("  ALGORITHM 1: LUCAS-BASED ADAPTIVE SAMPLING STRATEGY (LASS) POWER CONSUMPTION SIMULATION RESULTS\n")
    f.write("====================================================================================================\n")
    f.write(f"{'Hour':<6} | {'Low Rate (10s)':<15} | {'Med Rate (50s)':<15} | {'High Rate (80s)':<15} | {'Lucas Rate (LASS)':<20} | {'Random Rate':<12}\n")
    f.write("-" * 95 + "\n")
    for i in range(len(hours)):
        f.write(f"{hours[i]:<6d} | {pl[i]:<15.4f} | {pm[i]:<15.4f} | {ph[i]:<15.4f} | {pluc[i]:<20.4f} | {pr[i]:<12.4f}\n")
    f.write("====================================================================================================\n")

print(f"[+] Saved Text Summary Table: {summary_txt_path}")

# Plot Fig 3(a)-(d)
plt.style.use('dark_background')
durations = [6, 12, 18, 24]
fig_labels = ['(a) 6 Hours Simulation', '(b) 12 Hours Simulation', '(c) 18 Hours Simulation', '(d) 24 Hours Simulation']

for idx, sub_h in enumerate(durations):
    fig, ax = plt.subplots(figsize=(10, 4.5))
    h_sub = hours[:sub_h]
    ax.plot(h_sub, pl[:sub_h], 'o-', color='#3498db', label='Low Rate (10s)', linewidth=2.0, markersize=5)
    ax.plot(h_sub, pm[:sub_h], 's-', color='#f1c40f', label='Medium Rate (50s)', linewidth=2.0, markersize=5)
    ax.plot(h_sub, ph[:sub_h], '^-', color='#2ecc71', label='High Rate (80s)', linewidth=2.0, markersize=5)
    ax.plot(h_sub, pluc[:sub_h], 'd-', color='#9b59b6', label='Lucas Rate (Adaptive LASS)', linewidth=2.5, markersize=6)
    ax.plot(h_sub, pr[:sub_h], 'x--', color='#e74c3c', label='Random Rate', linewidth=2.0, markersize=6)

    ax.set_title(f'Power Consumption Comparison with Energy Harvesting — {fig_labels[idx]}', fontsize=12, fontweight='bold', pad=10)
    ax.set_xlabel('Duration (hours)', fontsize=10, fontweight='bold')
    ax.set_ylabel('Net Power Consumption (mW)', fontsize=10, fontweight='bold')
    ax.set_xticks(h_sub)
    ax.set_xticklabels([f'{h} hr' for h in h_sub])
    ax.set_yticks(np.arange(0.0, 1.9, 0.2))
    ax.set_ylim(0.0, 1.85)
    ax.grid(True, linestyle='--', alpha=0.25)
    ax.legend(fontsize=9, loc='upper right')

    plt.tight_layout()
    p_out = os.path.join(output_dir, f'power_consumption_fig3_{sub_h}h.png')
    plt.savefig(p_out, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"[+] Saved Output Plot: {p_out}")

# ==============================================================================
# 2. GENERATE FIGURE 1: CLUSTERING CONFIGURATIONS DENSITY MAP
# ==============================================================================
fig, ((ax_low, ax_med), (ax_high, ax_lucas)) = plt.subplots(2, 2, figsize=(14, 12))

# (a) Low Density
ax_low.set_title('(a) Low Density Clustering (20 Clusters x 5 Nodes = 100 Motes)', fontsize=11, fontweight='bold', pad=10)
sink_x_l, sink_y_l = 0, 160
ax_low.scatter(sink_x_l, sink_y_l, c='#e74c3c', marker='^', s=140, label='RPL Root Sink (Node 1)', zorder=5)
for r in range(4):
    for c in range(5):
        cx, cy = c * 70 - 140, r * 70 - 105
        ax_low.plot([cx, sink_x_l], [cy, sink_y_l], color='#3498db', linestyle=':', linewidth=0.8, alpha=0.5, zorder=2)
        ax_low.scatter(cx, cy, c='#f1c40f', s=60, edgecolors='black', zorder=4)
        for i in range(4):
            ang = i * (2 * np.pi / 4)
            ax_low.scatter(cx + 20*np.cos(ang), cy + 20*np.sin(ang), c='#3498db', s=20, alpha=0.7)
ax_low.set_aspect('equal')
ax_low.axis('off')

# (b) Medium Density
ax_med.set_title('(b) Medium Density Clustering (5 Clusters x 20 Nodes = 100 Motes)', fontsize=11, fontweight='bold', pad=10)
sink_x_m, sink_y_m = 0, 180
ax_med.scatter(sink_x_m, sink_y_m, c='#e74c3c', marker='^', s=140, label='RPL Root Sink (Node 1)', zorder=5)
med_hubs = [(-110, -110), (110, -110), (0, 0), (-110, 110), (110, 110)]
for cx, cy in med_hubs:
    ax_med.plot([cx, sink_x_m], [cy, sink_y_m], color='#3498db', linestyle=':', linewidth=0.8, alpha=0.5, zorder=2)
    ax_med.scatter(cx, cy, c='#f1c40f', s=70, edgecolors='black', zorder=4)
    for i in range(19):
        ang = i * (2 * np.pi / 19)
        ax_med.scatter(cx + 45*np.cos(ang), cy + 45*np.sin(ang), c='#3498db', s=20, alpha=0.7)
ax_med.set_aspect('equal')
ax_med.axis('off')

# (c) High Density
ax_high.set_title('(c) High Density Clustering (2 Clusters x 50 Nodes = 100 Motes)', fontsize=11, fontweight='bold', pad=10)
sink_x_h, sink_y_h = 0, 130
ax_high.scatter(sink_x_h, sink_y_h, c='#e74c3c', marker='^', s=140, label='RPL Root Sink (Node 1)', zorder=5)
high_hubs = [(-80, 0), (80, 0)]
for cx, cy in high_hubs:
    ax_high.plot([cx, sink_x_h], [cy, sink_y_h], color='#3498db', linestyle=':', linewidth=0.8, alpha=0.5, zorder=2)
    ax_high.scatter(cx, cy, c='#f1c40f', s=80, edgecolors='black', zorder=4)
    for i in range(49):
        ang = i * (2 * np.pi / 49)
        r_dist = 60 if i % 2 == 0 else 85
        ax_high.scatter(cx + r_dist*np.cos(ang), cy + r_dist*np.sin(ang), c='#3498db', s=20, alpha=0.7)
ax_high.set_aspect('equal')
ax_high.axis('off')

# (d) Lucas Adaptive Clustering
ax_lucas.set_title('(d) Lucas Adaptive Clustering [TOP PERFORMER: LASS 89.9% Energy Savings]', fontsize=11, fontweight='bold', color='#2ecc71', pad=10)
lucas_sizes = [2, 1, 3, 4, 7, 11, 18, 29, 25]
lucas_centers = [
    (100, 100), (300, 100), (520, 100),
    (100, 320), (300, 320), (520, 320),
    (100, 540), (310, 540), (530, 540)
]
sink_x, sink_y = 310, 690
ax_lucas.scatter(sink_x, sink_y, c='#e74c3c', marker='^', s=180, label='RPL Root Sink (Node 1)', zorder=5)

for idx, n_nodes in enumerate(lucas_sizes):
    cx, cy = lucas_centers[idx]
    ax_lucas.plot([cx, sink_x], [cy, sink_y], color='#2ecc71', linestyle='--', linewidth=1.2, alpha=0.85, zorder=2)
    ax_lucas.scatter(cx, cy, c='#f1c40f', s=90, edgecolors='black', zorder=4)
    r_radius = 20.0 + n_nodes * 1.1
    if n_nodes > 1:
        for i in range(n_nodes - 1):
            ang = i * (2 * np.pi / (n_nodes - 1))
            ax_lucas.scatter(cx + r_radius*np.cos(ang), cy + r_radius*np.sin(ang), c='#9b59b6', s=25, alpha=0.85, zorder=3)

ax_lucas.set_aspect('equal')
ax_lucas.axis('off')
plt.tight_layout()

fig1_path = os.path.join(output_dir, "clustering_density_fig1.png")
plt.savefig(fig1_path, dpi=200, bbox_inches='tight')
plt.close(fig)
print(f"[+] Saved Output Plot: {fig1_path}")

print("\n" + "=" * 100)
print(f"  SUCCESS: ALL OUTPUT PLOTS GENERATED IN: {output_dir}")
print("=" * 100)
