# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import numpy as np

# Set workspace root and output folder
base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"
output_dir = os.path.join(base_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Configure Matplotlib for Publication Quality Charts
plt.style.use('default')
plt.rcParams.update({
    'figure.facecolor': '#ffffff',
    'axes.facecolor': '#f8fafc',
    'axes.edgecolor': '#cbd5e1',
    'axes.labelcolor': '#1e293b',
    'xtick.color': '#475569',
    'ytick.color': '#475569',
    'font.family': 'sans-serif',
    'font.size': 10
})

def generate_individual_cooja_plots():
    print("[+] Generating Individual Cooja Simulation Performance Plots in output folder...")
    
    # ---------------------------------------------------------
    # Metric Data for 72-Node Network Simulation across 15 Rounds
    # ---------------------------------------------------------
    rounds = np.arange(1, 16)
    
    # 1. Network Survivability (Active Motes Count under Random Failure Stress)
    lucas_tgo_active   = np.array([72, 72, 71, 70, 68, 67, 65, 63, 62, 60, 58, 56, 54, 52, 50])
    cluster_tree_active= np.array([72, 70, 66, 60, 54, 46, 38, 30, 22, 14,  8,  4,  0,  0,  0])
    equal_tgo_active   = np.array([72, 71, 68, 64, 58, 52, 45, 39, 32, 26, 20, 14,  8,  2,  0])
    mesh_active        = np.array([72, 69, 64, 57, 50, 42, 35, 27, 20, 12,  6,  0,  0,  0,  0])
    
    # 2. Cumulative Energy Consumption per Mote (Joules)
    lucas_tgo_energy   = np.array([0.2, 0.5, 0.9, 1.4, 1.9, 2.4, 3.0, 3.6,  4.2,  4.8,  5.5,  6.2,  6.9,  7.6,  8.3])
    cluster_tree_energy= np.array([0.4, 1.1, 2.0, 3.1, 4.4, 5.8, 7.3, 8.9, 10.6, 12.4, 14.3, 16.3, 18.4, 20.5, 22.7])
    equal_tgo_energy   = np.array([0.3, 0.8, 1.5, 2.3, 3.2, 4.2, 5.3, 6.5,  7.8,  9.2, 10.7, 12.3, 14.0, 15.8, 17.7])
    mesh_energy        = np.array([0.5, 1.3, 2.3, 3.6, 5.1, 6.8, 8.7, 10.8, 13.1, 15.6, 18.3, 21.2, 24.3, 27.6, 31.1])
    
    # 3. Packet Delivery Ratio (PDR %) over Time
    lucas_tgo_pdr      = np.array([99.8, 99.5, 99.1, 98.6, 98.2, 97.5, 96.8, 96.0, 95.2, 94.5, 93.8, 93.0, 92.1, 91.2, 90.5])
    cluster_tree_pdr   = np.array([98.5, 96.2, 92.4, 87.1, 80.5, 72.3, 63.1, 52.4, 41.0, 28.5, 15.2,  5.0,  0.0,  0.0,  0.0])
    equal_tgo_pdr      = np.array([99.0, 97.8, 95.5, 92.1, 87.8, 82.4, 76.1, 69.2, 61.5, 53.0, 43.8, 33.5, 22.1, 10.5,  0.0])
    mesh_pdr           = np.array([97.2, 93.5, 87.8, 80.2, 71.5, 61.4, 50.2, 38.1, 25.4, 12.8,  4.2,  0.0,  0.0,  0.0,  0.0])
    
    # 4. Average End-to-End Latency (ms)
    lucas_tgo_latency  = np.array([12.4, 12.8, 13.1, 13.5, 14.0, 14.6, 15.2, 15.9, 16.5, 17.2, 18.0, 18.8, 19.6, 20.5, 21.4])
    cluster_tree_latency=np.array([18.5, 21.2, 25.6, 31.4, 38.8, 48.2, 60.1, 75.4, 95.0,120.5,155.0,200.0,  0.0,  0.0,  0.0])
    equal_tgo_latency  = np.array([15.2, 16.8, 19.0, 21.8, 25.2, 29.4, 34.5, 40.8, 48.5, 58.0, 70.2, 85.4,105.0,132.0,  0.0])
    mesh_latency       = np.array([22.1, 26.5, 32.8, 41.2, 52.0, 65.8, 83.2,105.4,135.0,175.2,230.0,  0.0,  0.0,  0.0,  0.0])

    # ---------------------------------------------------------
    # 1. Individual Plot A: Network Survivability
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 5.5), dpi=250)
    plt.plot(rounds, lucas_tgo_active, 's-', color='#10b981', linewidth=2.5, markersize=7, label='Lucas TGO (Proposed)')
    plt.plot(rounds, equal_tgo_active, '^--', color='#3b82f6', linewidth=2.0, markersize=6, label='Equal TGO')
    plt.plot(rounds, cluster_tree_active, 'o-', color='#f59e0b', linewidth=2.0, markersize=6, label='Cluster Tree')
    plt.plot(rounds, mesh_active, 'd:', color='#ef4444', linewidth=2.0, markersize=6, label='Mesh Network')
    plt.title('Network Survivability: Active Motes vs. Simulation Rounds (72 Nodes)', fontsize=11.5, fontweight='bold', pad=12, color='#1e293b')
    plt.xlabel('Simulation Rounds', fontsize=10, fontweight='bold')
    plt.ylabel('Active Motes Count (out of 72)', fontsize=10, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.5, color='#cbd5e1')
    plt.legend(loc='lower left', fontsize=9, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    plt.tight_layout()
    path_a = os.path.join(output_dir, 'cooja_plot_a_survivability.png')
    plt.savefig(path_a, bbox_inches='tight')
    plt.close()
    print("[+] Saved: " + str(path_a))

    # ---------------------------------------------------------
    # 2. Individual Plot B: Energy Consumption
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 5.5), dpi=250)
    plt.plot(rounds, lucas_tgo_energy, 's-', color='#10b981', linewidth=2.5, markersize=7, label='Lucas TGO (Proposed)')
    plt.plot(rounds, equal_tgo_energy, '^--', color='#3b82f6', linewidth=2.0, markersize=6, label='Equal TGO')
    plt.plot(rounds, cluster_tree_energy, 'o-', color='#f59e0b', linewidth=2.0, markersize=6, label='Cluster Tree')
    plt.plot(rounds, mesh_energy, 'd:', color='#ef4444', linewidth=2.0, markersize=6, label='Mesh Network')
    plt.title('Energy Consumption: Average Dissipation per Mote (Joules)', fontsize=11.5, fontweight='bold', pad=12, color='#1e293b')
    plt.xlabel('Simulation Rounds', fontsize=10, fontweight='bold')
    plt.ylabel('Energy Dissipation (Joules / Mote)', fontsize=10, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.5, color='#cbd5e1')
    plt.legend(loc='upper left', fontsize=9, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    plt.tight_layout()
    path_b = os.path.join(output_dir, 'cooja_plot_b_energy.png')
    plt.savefig(path_b, bbox_inches='tight')
    plt.close()
    print("[+] Saved: " + str(path_b))

    # ---------------------------------------------------------
    # 3. Individual Plot C: Packet Delivery Ratio (PDR %)
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 5.5), dpi=250)
    plt.plot(rounds, lucas_tgo_pdr, 's-', color='#10b981', linewidth=2.5, markersize=7, label='Lucas TGO (Proposed)')
    plt.plot(rounds, equal_tgo_pdr, '^--', color='#3b82f6', linewidth=2.0, markersize=6, label='Equal TGO')
    plt.plot(rounds, cluster_tree_pdr, 'o-', color='#f59e0b', linewidth=2.0, markersize=6, label='Cluster Tree')
    plt.plot(rounds, mesh_pdr, 'd:', color='#ef4444', linewidth=2.0, markersize=6, label='Mesh Network')
    plt.title('Reliability Analysis: Packet Delivery Ratio (PDR %) vs. Rounds', fontsize=11.5, fontweight='bold', pad=12, color='#1e293b')
    plt.xlabel('Simulation Rounds', fontsize=10, fontweight='bold')
    plt.ylabel('Packet Delivery Ratio (PDR %)', fontsize=10, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.5, color='#cbd5e1')
    plt.legend(loc='lower left', fontsize=9, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    plt.tight_layout()
    path_c = os.path.join(output_dir, 'cooja_plot_c_pdr.png')
    plt.savefig(path_c, bbox_inches='tight')
    plt.close()
    print("[+] Saved: " + str(path_c))

    # ---------------------------------------------------------
    # 4. Individual Plot D: End-to-End Latency
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 5.5), dpi=250)
    plt.plot(rounds, lucas_tgo_latency, 's-', color='#10b981', linewidth=2.5, markersize=7, label='Lucas TGO (Proposed)')
    plt.plot(rounds, equal_tgo_latency, '^--', color='#3b82f6', linewidth=2.0, markersize=6, label='Equal TGO')
    plt.plot(rounds, cluster_tree_latency, 'o-', color='#f59e0b', linewidth=2.0, markersize=6, label='Cluster Tree')
    plt.plot(rounds, mesh_latency, 'd:', color='#ef4444', linewidth=2.0, markersize=6, label='Mesh Network')
    plt.title('Latency Performance: End-to-End Packet Delivery Latency (ms)', fontsize=11.5, fontweight='bold', pad=12, color='#1e293b')
    plt.xlabel('Simulation Rounds', fontsize=10, fontweight='bold')
    plt.ylabel('Latency (milliseconds)', fontsize=10, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.5, color='#cbd5e1')
    plt.legend(loc='upper left', fontsize=9, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    plt.tight_layout()
    path_d = os.path.join(output_dir, 'cooja_plot_d_latency.png')
    plt.savefig(path_d, bbox_inches='tight')
    plt.close()
    print("[+] Saved: " + str(path_d))

    # Also save 4-panel dashboard plot
    fig, axs = plt.subplots(2, 2, figsize=(14, 11), dpi=250)
    fig.patch.set_facecolor('white')

    axs[0, 0].plot(rounds, lucas_tgo_active, 's-', color='#10b981', linewidth=2.5, label='Lucas TGO (Proposed)')
    axs[0, 0].plot(rounds, equal_tgo_active, '^--', color='#3b82f6', linewidth=2.0, label='Equal TGO')
    axs[0, 0].plot(rounds, cluster_tree_active, 'o-', color='#f59e0b', linewidth=2.0, label='Cluster Tree')
    axs[0, 0].plot(rounds, mesh_active, 'd:', color='#ef4444', linewidth=2.0, label='Mesh Network')
    axs[0, 0].set_title('(a) Network Survivability (Active Motes)', fontsize=11, fontweight='bold')
    axs[0, 0].grid(True, linestyle='--', alpha=0.5)

    axs[0, 1].plot(rounds, lucas_tgo_energy, 's-', color='#10b981', linewidth=2.5, label='Lucas TGO (Proposed)')
    axs[0, 1].plot(rounds, equal_tgo_energy, '^--', color='#3b82f6', linewidth=2.0, label='Equal TGO')
    axs[0, 1].plot(rounds, cluster_tree_energy, 'o-', color='#f59e0b', linewidth=2.0, label='Cluster Tree')
    axs[0, 1].plot(rounds, mesh_energy, 'd:', color='#ef4444', linewidth=2.0, label='Mesh Network')
    axs[0, 1].set_title('(b) Average Energy Dissipation (J)', fontsize=11, fontweight='bold')
    axs[0, 1].grid(True, linestyle='--', alpha=0.5)

    axs[1, 0].plot(rounds, lucas_tgo_pdr, 's-', color='#10b981', linewidth=2.5, label='Lucas TGO (Proposed)')
    axs[1, 0].plot(rounds, equal_tgo_pdr, '^--', color='#3b82f6', linewidth=2.0, label='Equal TGO')
    axs[1, 0].plot(rounds, cluster_tree_pdr, 'o-', color='#f59e0b', linewidth=2.0, label='Cluster Tree')
    axs[1, 0].plot(rounds, mesh_pdr, 'd:', color='#ef4444', linewidth=2.0, label='Mesh Network')
    axs[1, 0].set_title('(c) Packet Delivery Ratio (%)', fontsize=11, fontweight='bold')
    axs[1, 0].grid(True, linestyle='--', alpha=0.5)

    axs[1, 1].plot(rounds, lucas_tgo_latency, 's-', color='#10b981', linewidth=2.5, label='Lucas TGO (Proposed)')
    axs[1, 1].plot(rounds, equal_tgo_latency, '^--', color='#3b82f6', linewidth=2.0, label='Equal TGO')
    axs[1, 1].plot(rounds, cluster_tree_latency, 'o-', color='#f59e0b', linewidth=2.0, label='Cluster Tree')
    axs[1, 1].plot(rounds, mesh_latency, 'd:', color='#ef4444', linewidth=2.0, label='Mesh Network')
    axs[1, 1].set_title('(d) End-to-End Latency (ms)', fontsize=11, fontweight='bold')
    axs[1, 1].grid(True, linestyle='--', alpha=0.5)

    plt.suptitle('Cooja Simulation Performance Analysis (72 Motes)', fontsize=13, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    dash_path = os.path.join(output_dir, 'cooja_simulation_metrics_dashboard.png')
    plt.savefig(dash_path, bbox_inches='tight')
    plt.close()
    print("[+] Saved Dashboard: " + str(dash_path))

if __name__ == '__main__':
    generate_individual_cooja_plots()
