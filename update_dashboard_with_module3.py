import os
import base64
import re

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"
output_dir = os.path.join(base_dir, "output")
dashboard_path = os.path.join(base_dir, "dashboard.html")

print("[+] Embedding Module 3 & Cooja Simulation Metrics into dashboard.html...")

def get_b64(filename):
    # Try base_dir first, then output_dir
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        path = os.path.join(output_dir, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    print(f"[!] Warning: missing {filename}")
    return ""

img_fig3 = get_b64("etasr_fig3_lucas_clustering.png")
img_fig4 = get_b64("etasr_fig4_cluster_tree.png")
img_fig5 = get_b64("etasr_fig5_mesh_network.png")
img_fig6 = get_b64("etasr_fig6_tgo_mesh.png")

img_comp1       = get_b64("etasr_fig7_comparison1.png")
img_comp2       = get_b64("etasr_fig8_comparison2.png")
img_comp3       = get_b64("etasr_fig9_comparison3.png")
img_comp4       = get_b64("etasr_fig10_comparison4.png")
img_consolidated= get_b64("etasr_fig11_consolidated.png")

# 72-Node Cooja Simulation Metric Plots
img_cooja_a = get_b64("cooja_plot_a_survivability.png")
img_cooja_b = get_b64("cooja_plot_b_energy.png")
img_cooja_c = get_b64("cooja_plot_c_pdr.png")
img_cooja_d = get_b64("cooja_plot_d_latency.png")

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# Build HTML for Module 3
module3_html = f"""
    <!-- ========================================================================= -->
    <!-- MODULE 3: LUCAS-BASED CLUSTERING OPTIMIZATION FOR SMART HOME SURVIVABILITY -->
    <!-- ========================================================================= -->
    <div id="module-lucas-survivability" class="portal-module-view">
        <div class="portal-back-bar">
            <button class="back-portal-btn" onclick="openModule('cover-portal-view')">
                <span>🏠</span>
                <span>Back to Research Portal Cover Page</span>
            </button>
            <div style="font-weight: 800; font-size: 15px; color: var(--accent-purple);">
                🛡️ Module 3: Smart Home Survivability via Lucas TGO Clustering (ETASR 2025)
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); font-weight: 600;">
                72 to 100 Motes | Random Node Failure Analysis
            </div>
        </div>

        <!-- Executive Paper Header -->
        <div class="conclusion-card" style="margin-top: 0; margin-bottom: 25px;">
            <h2>📄 ETASR 2025 Research Paper: A Novel Lucas-based Clustering Optimization for Enhancing Survivability in Smart Home Design</h2>
            <p><strong>Authors:</strong> Kanaka Raju Rajana & Shanmuk Srinivas Amiripalli (Department of Computer Science and Engineering, GST, GITAM University, Visakhapatnam, India)</p>
            <p><strong>Publication:</strong> <em>Engineering, Technology & Applied Science Research (ETASR)</em>, Vol. 15, No. 1, 2025, pp. 19903–19909. <strong>DOI:</strong> <a href="https://doi.org/10.48084/etasr.9232" target="_blank" style="color: var(--accent-green); text-decoration: underline;">10.48084/etasr.9232</a></p>
            <p style="margin-top: 10px;">This study introduces a novel Lucas-based topology optimization framework to enhance network survivability in smart homes against random node failures. By integrating mathematical properties of Lucas numbers ($L_n = [3, 4, 7, 11, 18, 29, \dots]$) with Trimet Graph Optimization (TGO), the framework optimizes network topologies to maintain robust edge/node connectivity under adverse disruption conditions.</p>
        </div>

        <!-- KPI Grid for Module 3 -->
        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="label">Lucas TGO Survivability</div>
                <div class="value" style="color: var(--accent-green);">9 – 12 Rounds</div>
                <div class="sub">Consistently Best Performance</div>
            </div>
            <div class="kpi-card">
                <div class="label">Baseline Topologies</div>
                <div class="value" style="color: var(--accent-red);">6 – 8 Rounds</div>
                <div class="sub">Cluster Tree, Equal TGO, Mesh</div>
            </div>
            <div class="kpi-card">
                <div class="label">Lucas Cluster Invariants</div>
                <div class="value" style="color: var(--accent-purple);">L_n Sequence</div>
                <div class="sub">3, 4, 7, 11, 18, 29 Motes</div>
            </div>
            <div class="kpi-card">
                <div class="label">Evaluated Network Scale</div>
                <div class="value" style="color: var(--accent-blue);">72 – 100 Nodes</div>
                <div class="sub">RPL-UDP & Cooja Simulation</div>
            </div>
        </div>

        <!-- Section 1: Individual Topology Figures (Figures 3, 4, 5, 6) -->
        <div class="section-title">📐 Topology Representations (Figures 3, 4, 5, & 6)</div>
        
        <div class="grid-2col" style="margin-bottom: 25px;">
            <div class="chart-box">
                <h3 style="color: var(--accent-purple);">Figure 3. Representation of Lucas-based clustering model.</h3>
                <img src="{img_fig3}" alt="Figure 3 Representation of Lucas-based clustering model">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-blue);">Figure 4. Cluster tree.</h3>
                <img src="{img_fig4}" alt="Figure 4 Cluster tree">
            </div>
        </div>

        <div class="grid-2col" style="margin-bottom: 30px;">
            <div class="chart-box">
                <h3 style="color: var(--accent-red);">Figure 5. Mesh network.</h3>
                <img src="{img_fig5}" alt="Figure 5 Mesh network">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-green);">Figure 6. TGO mesh network.</h3>
                <img src="{img_fig6}" alt="Figure 6 TGO mesh network">
            </div>
        </div>

        <!-- Section 2: Real-Time 72-Node Cooja Simulation Output Metrics -->
        <div class="section-title">⏱️ Real-Time 72-Node Cooja Simulation Performance Metrics</div>
        <div class="grid-2col" style="margin-bottom: 25px;">
            <div class="chart-box">
                <h3 style="color: var(--accent-green);">(a) Network Survivability (Active Motes vs. Rounds)</h3>
                <img src="{img_cooja_a}" alt="Network Survivability">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-blue);">(b) Average Energy Dissipation (Joules / Mote)</h3>
                <img src="{img_cooja_b}" alt="Energy Dissipation">
            </div>
        </div>
        <div class="grid-2col" style="margin-bottom: 30px;">
            <div class="chart-box">
                <h3 style="color: var(--accent-gold);">(c) Packet Delivery Ratio (PDR %) vs. Rounds</h3>
                <img src="{img_cooja_c}" alt="Packet Delivery Ratio">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-purple);">(d) End-to-End Delivery Latency (ms)</h3>
                <img src="{img_cooja_d}" alt="End-to-End Latency">
            </div>
        </div>

        <!-- Section 3: Dynamic Survivability Comparisons Across Node Counts (Figures 7–10) -->
        <div class="section-title">📊 ETASR Paper Dynamic Survivability Comparisons Across Node Counts (Figures 7–10)</div>
        <div class="grid-2col">
            <div class="chart-box">
                <h3 style="color: var(--accent-blue);">Figure 7. Dynamic comparison-1 of different smart home topologies with Lucas-based clustering.</h3>
                <img src="{img_comp1}" alt="Dynamic Comparison 1">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-gold);">Figure 8. Dynamic comparison-2 of different smart home topologies with Lucas-based clustering.</h3>
                <img src="{img_comp2}" alt="Dynamic Comparison 2">
            </div>
        </div>
        <div class="grid-2col" style="margin-bottom: 30px;">
            <div class="chart-box">
                <h3 style="color: var(--accent-purple);">Figure 9. Dynamic comparison-3 of different smart home topologies with Lucas-based clustering.</h3>
                <img src="{img_comp3}" alt="Dynamic Comparison 3">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-green);">Figure 10. Dynamic comparison-4 of different smart home topologies with Lucas-based clustering.</h3>
                <img src="{img_comp4}" alt="Dynamic Comparison 4">
            </div>
        </div>

        <!-- Section 4: Consolidated Comparison Across 18 Experiments (Figure 11) -->
        <div class="chart-box" style="margin-bottom: 30px;">
            <h3 style="color: var(--accent-green); font-size: 18px;">Figure 11. Consolidated comparison of different smart home topologies with Lucas-based clustering.</h3>
            <img src="{img_consolidated}" alt="Figure 11 Consolidated Comparison">
        </div>

        <!-- Section 5: Contiki-NG Firmware & Cooja Simulation Working -->
        <div class="section-title">💻 Working of Attached Document in Contiki-NG & Cooja</div>

        <div class="grid-2col" style="margin-bottom: 25px;">
            <div class="table-container">
                <div class="table-title">📜 Contiki-NG C Source (`lucas-tgo-survivability.c`)</div>
                <pre style="background: #0b0e14; color: #a9b7c6; padding: 18px; font-family: monospace; font-size: 11.5px; border-radius: 10px; max-height: 280px; overflow-y: auto;">
#include "contiki.h"
#include "net/routing/routing.h"
#include "net/ipv6/simple-udp.h"
#include "sys/log.h"
#include "random.h"

#define LOG_MODULE "LucasTGO"
#define LOG_LEVEL LOG_LEVEL_INFO
#define UDP_PORT 5678

static const uint8_t lucas_clusters[] = {{3, 4, 7, 11, 18, 29}};
static uint8_t current_round = 0;
static uint8_t active_nodes = 72;

PROCESS(lucas_tgo_survivability_process, "Lucas TGO Survivability Process");
AUTOSTART_PROCESSES(&lucas_tgo_survivability_process);

static void handle_random_node_failure(void) {{
  if(random_rand() % 100 < 15) {{
    LOG_WARN("Node %u failed! Triggering Lucas TGO rerouting...\\n", linkaddr_node_addr.u8[0]);
    if(active_nodes > 0) active_nodes--;
  }}
}}
                </pre>
            </div>

            <div class="table-container">
                <div class="table-title">🔧 Cooja XML Simulation (`lucas72_rpl_udp.csc`)</div>
                <pre style="background: #0b0e14; color: #a9b7c6; padding: 18px; font-family: monospace; font-size: 11.5px; border-radius: 10px; max-height: 280px; overflow-y: auto;">
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;simconf&gt;
  &lt;simulation&gt;
    &lt;title&gt;Lucas TGO Smart Home Survivability (72 Motes)&lt;/title&gt;
    &lt;randomseed&gt;123456&lt;/randomseed&gt;
    &lt;radiomedium&gt;
      org.contikios.cooja.radiomediums.UDGM
      &lt;transmitting_range&gt;50.0&lt;/transmitting_range&gt;
      &lt;interference_range&gt;100.0&lt;/interference_range&gt;
      &lt;success_ratio_rx&gt;1.0&lt;/success_ratio_rx&gt;
    &lt;/radiomedium&gt;
    &lt;motetype&gt;
      &lt;identifier&gt;lucasmote&lt;/identifier&gt;
      &lt;source&gt;[CONFIG_DIR]/lucas-adaptive-client.c&lt;/source&gt;
    &lt;/motetype&gt;
  &lt;/simulation&gt;
&lt;/simconf&gt;
                </pre>
            </div>
        </div>

        <!-- Interactive Contiki-NG Simulation Terminal Workbench -->
        <div class="conclusion-card" style="margin-bottom: 40px; border-color: var(--accent-purple);">
            <h3 style="color: var(--accent-purple); margin-bottom: 12px; display: flex; align-items: center; gap: 10px;">
                <span>🖥️</span> Interactive Contiki-NG Cooja Execution Terminal
            </h3>
            <p style="margin-bottom: 15px; font-size: 13.5px;">Click the buttons below to simulate random node failure injection, RPL DODAG dynamic restructuring, and Lucas sequence cluster head backup election live in Contiki-NG:</p>
            
            <div style="display: flex; gap: 12px; margin-bottom: 18px; flex-wrap: wrap;">
                <button class="back-portal-btn" style="background: linear-gradient(135deg, #9b59b6, #8e44ad);" onclick="runContikiSim('start')">
                    🚀 Run Contiki-NG Simulation
                </button>
                <button class="back-portal-btn" style="background: linear-gradient(135deg, #e74c3c, #c0392b);" onclick="runContikiSim('fail')">
                    ⚡ Inject Random Node Failures (15%)
                </button>
                <button class="back-portal-btn" style="background: linear-gradient(135deg, #2ecc71, #27ae60);" onclick="runContikiSim('reroute')">
                    🔄 Execute Lucas TGO Rerouting
                </button>
                <button class="back-portal-btn" style="background: #151b26; border-color: #94a3b8;" onclick="runContikiSim('reset')">
                    🧹 Reset Simulation
                </button>
            </div>

            <div id="contiki-terminal-output" style="background: #080b10; border: 1px solid #2a3447; border-radius: 12px; padding: 18px; font-family: monospace; font-size: 12.5px; color: #34d399; min-height: 180px; max-height: 320px; overflow-y: auto;">
[00:00.000] Contiki-NG-4.9-RELEASE booted on Cooja Mote #1 (Sink / Root)
[00:00.012] [LucasTGO: INFO] Initializing Lucas-Based TGO Smart Home Survivability Protocol
[00:00.025] [LucasTGO: INFO] Node 1 designated as Lucas Cluster Head (TGO Model)
[00:00.050] [LucasTGO: INFO] Initializing 72 Smart Home Motes across Lucas clusters
[00:00.100] Contiki-NG RPL DODAG formed with rank 128. Ready for Survivability Benchmark.
            </div>
        </div>
    </div>
"""

# Replace existing module-lucas-survivability block
m3_start = content.find('<div id="module-lucas-survivability"')
if m3_start != -1:
    m3_end = content.find('</div>\n    <script>', m3_start)
    if m3_end != -1:
        content = content[:m3_start] + module3_html + content[m3_end:]
    else:
        m3_end_body = content.rfind('</body>')
        content = content[:m3_start] + module3_html + content[m3_end_body:]

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[+] SUCCESS: Dashboard updated with both ETASR paper comparison figures AND 72-Node Cooja real-time simulation output metrics!")
