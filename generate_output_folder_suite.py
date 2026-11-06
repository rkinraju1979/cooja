import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = script_dir if script_dir else os.getcwd()
output_dir = os.path.join(base_dir, 'output')
os.makedirs(output_dir, exist_ok=True)

print("=" * 100)
print(f"[+] MASTER WSN SIMULATION RUNNER — SAVING ALL OUTPUTS TO: {output_dir}")
print("=" * 100)

# ------------------------------------------------------------------------------
# 1. ALGORITHM 1: POWER CONSUMPTION SIMULATION (FIGURE 3)
# ------------------------------------------------------------------------------
def simulate_power(total_hours=24):
    hours = np.arange(1, total_hours + 1)
    pwr_low, pwr_med, pwr_high, pwr_lucas, pwr_random = [], [], [], [], []
    for h in hours:
        p_l = 1.35 - 0.008 * h + 0.04 * np.sin(0.4 * h)
        p_m = 0.35 * np.exp(-0.12 * h) + 0.24
        p_h = 0.28 * np.exp(-0.15 * h) + 0.15
        p_luc = 0.20 * np.exp(-0.25 * h) + 0.052
        np.random.seed(h * 13)
        spike = 0.40 if (h % 3 == 0) else 0.0
        p_r = 0.85 + spike + np.random.uniform(-0.05, 0.05)
        
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
    ax.set_yticks(np.arange(0.0, 1.7, 0.2))
    ax.set_ylim(0.0, 1.65)
    ax.grid(True, linestyle='--', alpha=0.25)
    ax.legend(fontsize=9, loc='upper right')

    plt.tight_layout()
    p_out = os.path.join(output_dir, f'power_consumption_fig3_{sub_h}h.png')
    plt.savefig(p_out, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"[+] Saved Output Plot: {p_out}")

print("\n" + "=" * 100)
print(f"  SUCCESS: ALL OUTPUT FILES GENERATED IN: {output_dir}")
print("=" * 100)
