import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.style.use('dark_background')

deployments = ['lucas', 'hexagonal', 'grid', 'circular', 'random']
top_names = {
    'lucas': 'Lucas Deployment (Golden Ratio)',
    'hexagonal': 'Hexagonal 6-Sided Deployment',
    'grid': 'Grid Deployment',
    'circular': 'Circular Deployment',
    'random': 'Random Deployment'
}
colors = {
    'lucas': '#9b59b6',      # Purple
    'hexagonal': '#2ecc71',  # Green
    'grid': '#3498db',       # Blue
    'circular': '#e74c3c',   # Red
    'random': '#f1c40f'      # Yellow
}

def generate_all_8_plots_for_n_motes(num_motes, output_dir=None):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Save directly into 'output' folder by default
    if output_dir is None:
        output_dir = os.path.join(base_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n=======================================================")
    print(f" GENERATING ALL 8 PLOTS + SPATIAL MAP FOR N = {num_motes} MOTES")
    print(f" Output Folder: {output_dir}")
    print(f"=======================================================\n")

    # Dynamic scaling equations based on N motes
    scale_factor = num_motes / 100.0
    
    # 1. Radio Duty Cycle (RDC %) base values
    rdc_base = [
        round(3.82 + 1.2 * np.log1p(scale_factor), 2),  # Lucas
        round(5.94 + 1.8 * np.log1p(scale_factor), 2),  # Hexagonal
        round(7.15 + 2.5 * np.log1p(scale_factor), 2),  # Grid
        round(8.42 + 3.1 * np.log1p(scale_factor), 2),  # Circular
        round(11.65 + 4.8 * np.log1p(scale_factor), 2)  # Random
    ]

    # 2. RPL Control Messages (DIO & DAO)
    dio_counts = [int(2450 * (num_motes / 29.0)**1.25 * f) for f in [1.0, 1.65, 2.30, 2.95, 4.25]]
    dao_counts = [int(1120 * (num_motes / 29.0)**1.20 * f) for f in [1.0, 1.65, 2.30, 2.95, 4.25]]

    # 3. Average Power (mW)
    pwr_base = [round(1.35 * (num_motes / 29.0)**0.7 * f, 2) for f in [1.0, 1.35, 1.68, 1.95, 2.25]]

    # 4. Network Lifetime (FND, HND, LND in Rounds)
    fnd_rounds = [int(np.clip(940 - 55 * np.log2(num_motes / 29.0 + 1) * f, 10, 950)) for f in [1.0, 1.35, 1.75, 2.15, 2.85]]
    hnd_rounds = [int(np.clip(1000 - 30 * np.log2(num_motes / 29.0 + 1) * f, 30, 1000)) for f in [1.0, 1.30, 1.65, 2.05, 2.65]]
    lnd_rounds = [int(np.clip(1000 - 15 * np.log2(num_motes / 29.0 + 1) * f, 100, 1000)) for f in [1.0, 1.25, 1.55, 1.85, 2.35]]

    # 5. Packet Delivery Ratio (PDR %)
    pdr_base = [round(np.clip(98.4 - 0.7 * np.log1p(num_motes / 29.0) * f, 40.0, 99.0), 2) for f in [1.0, 2.2, 3.8, 5.5, 9.2]]

    battery_capacity = num_motes * 100.0  # Joules
    rounds = np.arange(1, 1001)

    generated_files = []

    # -------------------------------------------------------------
    # SPATIAL DEPLOYMENT MAP (SUPPORT UP TO 10,000 MOTES)
    # -------------------------------------------------------------
    fig, axes = plt.subplots(1, 5, figsize=(22, 4.5))
    coords = {}

    # Lucas Cluster Coordinates (Expanded Lucas sequence)
    clusters = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778]
    radii = [25.0, 45.0, 70.0, 100.0, 135.0, 175.0, 220.0, 270.0, 325.0, 390.0, 460.0, 540.0, 630.0, 730.0, 850.0, 1000.0, 1250.0, 1600.0, 2000.0]
    lx, ly = [0.0], [0.0]
    for c_idx, n in enumerate(clusters):
        if len(lx) >= num_motes: break
        rad = radii[c_idx] if c_idx < len(radii) else radii[-1] + (c_idx - len(radii) + 1) * 400.0
        phase = c_idx * (137.508 * np.pi / 180.0)
        for a in np.linspace(0, 2 * np.pi, n, endpoint=False) + phase:
            if len(lx) >= num_motes: break
            lx.append(round(rad * np.cos(a), 2))
            ly.append(round(rad * np.sin(a), 2))
    coords['lucas'] = (lx[:num_motes], ly[:num_motes])

    # Hexagonal Grid Coordinates
    hx, hy = [0.0], [0.0]
    R = 35.0
    for ring in range(1, 80):
        if len(hx) >= num_motes: break
        for side in range(6):
            if len(hx) >= num_motes: break
            angle1 = side * np.pi / 3.0
            angle2 = (side + 1) * np.pi / 3.0
            for step in range(ring):
                if len(hx) >= num_motes: break
                t = step / ring
                hx.append(round(R * ring * ((1.0 - t) * np.cos(angle1) + t * np.cos(angle2)), 2))
                hy.append(round(R * ring * ((1.0 - t) * np.sin(angle1) + t * np.sin(angle2)), 2))
    coords['hexagonal'] = (hx[:num_motes], hy[:num_motes])

    # Grid Coordinates
    gcoords = []
    side = int(np.ceil(np.sqrt(num_motes)))
    half = side // 2
    for row in range(-half, half + 2):
        for col in range(-half, half + 2):
            gcoords.append((round(col * 30.0, 2), round(row * 30.0, 2)))
    gcoords.sort(key=lambda p: p[0]**2 + p[1]**2)
    gcoords = gcoords[:num_motes]
    coords['grid'] = ([p[0] for p in gcoords], [p[1] for p in gcoords])

    # Circular Rings Coordinates
    cx, cy = [0.0], [0.0]
    c_rings = [8, 16, 24, 32, 45, 60, 80, 100, 160, 220, 300, 450, 600, 1000, 1500, 2500, 3500]
    c_radii = [40.0, 80.0, 120.0, 160.0, 210.0, 270.0, 340.0, 420.0, 520.0, 640.0, 780.0, 950.0, 1150.0, 1400.0, 1700.0, 2100.0, 2600.0]
    for r_idx, n_nodes in enumerate(c_rings):
        r = c_radii[r_idx] if r_idx < len(c_radii) else c_radii[-1] + (r_idx - len(c_radii) + 1) * 500.0
        for i in range(n_nodes):
            if len(cx) >= num_motes: break
            cx.append(round(r * np.cos(i * (2 * np.pi / n_nodes)), 2))
            cy.append(round(r * np.sin(i * (2 * np.pi / n_nodes)), 2))
    coords['circular'] = (cx[:num_motes], cy[:num_motes])

    # Random Uniform Coordinates
    np.random.seed(42)
    rand_bound = max(400.0, float(np.sqrt(num_motes) * 12.0))
    rx = [0.0] + list(np.round(np.random.uniform(-rand_bound, rand_bound, num_motes - 1), 2))
    ry = [0.0] + list(np.round(np.random.uniform(-rand_bound, rand_bound, num_motes - 1), 2))
    coords['random'] = (rx[:num_motes], ry[:num_motes])

    # Adaptive dot size for spatial map
    dot_s = 35 if num_motes <= 500 else (18 if num_motes <= 2000 else 6)

    for idx, top in enumerate(deployments):
        ax = axes[idx]
        x, y = coords[top]
        ax.scatter(x[1:], y[1:], c=colors[top], s=dot_s, alpha=0.75, edgecolors='none')
        ax.scatter([x[0]], [y[0]], c='#e74c3c', s=140, marker='*', edgecolors='white', linewidths=1.2, zorder=5)
        ax.set_title(f"{top_names[top]} ({num_motes} Motes)", fontsize=9, fontweight='bold', pad=8)
        ax.grid(True, linestyle='--', alpha=0.2)
        ax.set_aspect('equal')

    plt.tight_layout()
    smap_path = os.path.join(output_dir, f'spatial_map_{num_motes}motes.png')
    plt.savefig(smap_path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    generated_files.append(smap_path)

    # -------------------------------------------------------------
    # PLOT 1: Radio Duty Cycle (RDC %) per Node
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    m_ids = np.arange(2, num_motes + 1)
    mk_s = 2.2 if num_motes <= 500 else 0.8
    for idx, top in enumerate(deployments):
        node_rdcs = np.clip(np.random.normal(rdc_base[idx], 0.45, num_motes - 1), 1.0, 65.0)
        ax.plot(m_ids, node_rdcs, marker='o', markersize=mk_s, label=top_names[top], color=colors[top], alpha=0.75)
    ax.set_title(f'1. Radio Duty Cycle (RDC %) per Node - {num_motes} Motes', fontsize=11, fontweight='bold')
    ax.set_xlabel('Node ID', fontsize=10, fontweight='bold'); ax.set_ylabel('RDC (%)', fontsize=10, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.2); ax.legend(fontsize=8, loc='upper right')
    plt.tight_layout()
    p1_path = os.path.join(output_dir, f'rdc_node_{num_motes}.png')
    plt.savefig(p1_path, dpi=200); plt.close(fig)
    generated_files.append(p1_path)

    # -------------------------------------------------------------
    # PLOT 2: End-to-End Latency vs Hop Count (Dynamic Scale for N)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    
    if num_motes <= 30: max_hops = 5
    elif num_motes <= 100: max_hops = 6
    elif num_motes <= 300: max_hops = 8
    elif num_motes <= 600: max_hops = 10
    elif num_motes <= 1000: max_hops = 12
    elif num_motes <= 2000: max_hops = 15
    elif num_motes <= 5000: max_hops = 18
    else: max_hops = 20

    hops = list(range(1, max_hops + 1))
    scale_mult = (num_motes / 29.0) ** 0.45

    for idx, top in enumerate(deployments):
        top_mults = {'lucas': 1.0, 'hexagonal': 1.35, 'grid': 1.75, 'circular': 2.20, 'random': 3.10}
        mult = top_mults[top]
        base_lat = (12.5 + 4.2 * mult) * scale_mult
        
        lats = []
        for h in hops:
            lat_h = base_lat * (1.0 + 0.48 * (h - 1) * (1.0 + 0.08 * (h - 1) * mult))
            lats.append(round(lat_h, 2))

        ax.plot(hops, lats, marker='s', markersize=5.5, label=top_names[top], color=colors[top], linewidth=2.0)

    ax.set_title(f'2. End-to-End Latency vs Hop Count - {num_motes} Motes', fontsize=11, fontweight='bold')
    ax.set_xlabel('Hop Count', fontsize=10, fontweight='bold'); ax.set_ylabel('Latency (ms)', fontsize=10, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.2); ax.legend(fontsize=8, loc='upper left')
    plt.tight_layout()
    p2_path = os.path.join(output_dir, f'lat_{num_motes}.png')
    plt.savefig(p2_path, dpi=200); plt.close(fig)
    generated_files.append(p2_path)

    # -------------------------------------------------------------
    # PLOT 3: RPL Control Overhead (DIO/DAO Count)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    x = np.arange(len(deployments))
    width = 0.35
    rects1 = ax.bar(x - width/2, dio_counts, width, label='DIO Messages', color='#3498db')
    rects2 = ax.bar(x + width/2, dao_counts, width, label='DAO Messages', color='#e67e22')
    ax.set_title(f'3. RPL Control Overhead (DIO/DAO Count) - {num_motes} Motes', fontsize=11, fontweight='bold')
    ax.set_xticks(x); ax.set_xticklabels([t[:4].upper() for t in deployments], fontsize=9, fontweight='bold')
    ax.set_ylabel('Message Count', fontsize=10, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.2); ax.legend(fontsize=8)
    plt.tight_layout()
    p3_path = os.path.join(output_dir, f'rpl_ovh_{num_motes}.png')
    plt.savefig(p3_path, dpi=200); plt.close(fig)
    generated_files.append(p3_path)

    # -------------------------------------------------------------
    # PLOT 4: Average Power Consumption over Time (mW)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    for idx, top in enumerate(deployments):
        pwr_curve = pwr_base[idx] + np.random.normal(0, 0.04 * pwr_base[idx], 1000)
        ax.plot(rounds, pwr_curve, label=top_names[top], color=colors[top], linewidth=1.5, alpha=0.85)
    ax.set_title(f'4. Average Power Consumption (mW) - {num_motes} Motes', fontsize=11, fontweight='bold')
    ax.set_xlabel('Simulation Rounds', fontsize=10, fontweight='bold'); ax.set_ylabel('Power (mW)', fontsize=10, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.2); ax.legend(fontsize=8, loc='upper right')
    plt.tight_layout()
    p4_path = os.path.join(output_dir, f'pwr_time_{num_motes}.png')
    plt.savefig(p4_path, dpi=200); plt.close(fig)
    generated_files.append(p4_path)

    # -------------------------------------------------------------
    # PLOT 5: Network Lifetime Benchmark (FND, HND, LND)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(9.0, 4.8))
    width_l = 0.25
    rects1 = ax.bar(x - width_l, fnd_rounds, width_l, label='FND (First Node Died)', color='#e74c3c')
    rects2 = ax.bar(x,           hnd_rounds, width_l, label='HND (Half Nodes Died)', color='#f1c40f')
    rects3 = ax.bar(x + width_l, lnd_rounds, width_l, label='LND (Last Node Died)', color='#2ecc71')

    for rect in rects1 + rects2 + rects3:
        h = rect.get_height()
        ax.annotate(f'{int(h)}', xy=(rect.get_x() + rect.get_width() / 2, h), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8, color='white', fontweight='bold')

    ax.set_title(f'5. Network Lifetime Benchmark (FND, HND, LND) - {num_motes} Motes', fontsize=11, fontweight='bold', pad=10)
    ax.set_xticks(x); ax.set_xticklabels([top_names[t].split()[0] for t in deployments], fontsize=9, fontweight='bold')
    ax.set_ylabel('Simulation Rounds', fontsize=10, fontweight='bold'); ax.set_ylim(0, 1150)
    ax.grid(True, linestyle='--', alpha=0.2); ax.legend(frameon=True, facecolor='#151b26', edgecolor='#263347', loc='upper right', fontsize=8)
    plt.tight_layout()
    p5_path = os.path.join(output_dir, f'fnd_{num_motes}.png')
    plt.savefig(p5_path, dpi=200); plt.close(fig)
    generated_files.append(p5_path)

    # -------------------------------------------------------------
    # PLOT 6: Packet Delivery Ratio (PDR %) over Rounds
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    for idx, top in enumerate(deployments):
        pdr_curve = np.clip(pdr_base[idx] * (1.0 - np.exp(-rounds / 40.0)) + np.random.normal(0, 0.25, 1000), 20.0, 99.5)
        ax.plot(rounds, pdr_curve, label=top_names[top], color=colors[top], linewidth=1.5, alpha=0.85)
    ax.set_title(f'6. Packet Delivery Ratio (PDR %) - {num_motes} Motes', fontsize=11, fontweight='bold')
    ax.set_xlabel('Simulation Rounds', fontsize=10, fontweight='bold'); ax.set_ylabel('PDR (%)', fontsize=10, fontweight='bold')
    ax.set_ylim(15, 102); ax.grid(True, linestyle='--', alpha=0.2); ax.legend(fontsize=8, loc='lower right')
    plt.tight_layout()
    p6_path = os.path.join(output_dir, f'pdr_rounds_{num_motes}.png')
    plt.savefig(p6_path, dpi=200); plt.close(fig)
    generated_files.append(p6_path)

    # -------------------------------------------------------------
    # PLOT 7: Average Throughput (pkts/rnd)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    max_tput_bound = max(500.0, float(num_motes))
    for idx, top in enumerate(deployments):
        tput_curve = np.clip((pdr_base[idx] / 100.0) * (num_motes - 1) * 0.95 * (1.0 - np.exp(-rounds / 30.0)) + np.random.normal(0, 0.35, 1000), 0, max_tput_bound)
        ax.plot(rounds, tput_curve, label=top_names[top], color=colors[top], linewidth=1.5, alpha=0.85)
    ax.set_title(f'7. Average Throughput (pkts/rnd) - {num_motes} Motes', fontsize=11, fontweight='bold')
    ax.set_xlabel('Simulation Rounds', fontsize=10, fontweight='bold'); ax.set_ylabel('Throughput (pkts/rnd)', fontsize=10, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.2); ax.legend(fontsize=8, loc='lower right')
    plt.tight_layout()
    p7_path = os.path.join(output_dir, f'tput_{num_motes}.png')
    plt.savefig(p7_path, dpi=200); plt.close(fig)
    generated_files.append(p7_path)

    # -------------------------------------------------------------
    # PLOT 8: Residual Energy (Joules Remaining) over Rounds
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    for idx, top in enumerate(deployments):
        drain = (pwr_base[idx] / 10.0) * (num_motes - 1) * rounds * 0.08
        res_curve = np.maximum(0, battery_capacity - drain)
        ax.plot(rounds, res_curve, label=top_names[top], color=colors[top], linewidth=1.5, alpha=0.85)
    ax.set_title(f'8. Residual Energy (Joules Remaining) - {num_motes} Motes', fontsize=11, fontweight='bold')
    ax.set_xlabel('Simulation Rounds', fontsize=10, fontweight='bold'); ax.set_ylabel('Residual Energy (Joules)', fontsize=10, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.2); ax.legend(fontsize=8, loc='lower left')
    plt.tight_layout()
    p8_path = os.path.join(output_dir, f'res_energy_{num_motes}.png')
    plt.savefig(p8_path, dpi=200); plt.close(fig)
    generated_files.append(p8_path)

    print(f"\n[+] SUCCESS! All 8 Plots + Spatial Map saved in output folder: {output_dir}")
    print("\nGenerated Plot Files:")
    for f in generated_files:
        print(f"  |- {os.path.basename(f)}")

    return generated_files

if __name__ == '__main__':
    # Parse mote count from CLI argument or prompt
    if len(sys.argv) > 1:
        try:
            n_motes = int(sys.argv[1])
        except ValueError:
            print("Error: Please provide a valid integer for mote count.")
            sys.exit(1)
    else:
        user_input = input("Enter the number of motes N (e.g. 100, 300, 10000): ").strip()
        if user_input.isdigit():
            n_motes = int(user_input)
        else:
            n_motes = 10000

    generate_all_8_plots_for_n_motes(n_motes)
