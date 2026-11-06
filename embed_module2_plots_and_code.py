import os
import base64
import html

workspace = os.path.dirname(os.path.abspath(__file__))
dashboard_path = os.path.join(workspace, "dashboard.html")
script_path = os.path.join(workspace, "power_consumption_lass_plotter.py")

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    print(f"[!] Warning: missing {path}")
    return ""

# Read the Python script code
with open(script_path, "r", encoding="utf-8") as f:
    python_code = f.read()
python_code_escaped = html.escape(python_code)

# Encode all plots
img_power_5schemes = get_b64(os.path.join(workspace, "output", "power_consumption_5schemes.png"))
img_eff_5schemes = get_b64(os.path.join(workspace, "output", "energy_efficiency_5schemes.png"))
img_life_5schemes = get_b64(os.path.join(workspace, "output", "network_lifetime_5schemes.png"))
img_comp_5schemes = get_b64(os.path.join(workspace, "output", "comprehensive_5schemes_metrics.png"))

img_fig1 = get_b64(os.path.join(workspace, "clustering_density_fig1.png"))
img_fig3_6h = get_b64(os.path.join(workspace, "power_consumption_fig3_6h.png"))
img_fig3_12h = get_b64(os.path.join(workspace, "power_consumption_fig3_12h.png"))
img_fig3_18h = get_b64(os.path.join(workspace, "power_consumption_fig3_18h.png"))
img_fig3_24h = get_b64(os.path.join(workspace, "power_consumption_fig3_24h.png"))

module2_html = f"""<div id="module-power-lucas" class="portal-module-view">
        
        <div class="portal-back-bar">
            <button class="back-portal-btn" onclick="openModule('cover-portal-view')">
                <span>🏠</span>
                <span>Back to Research Portal Cover Page</span>
            </button>
            <div style="font-weight: 800; font-size: 15px; color: var(--accent-green);">
                ⚡ Module 2: Lucas-Based Adaptive Sampling Optimization (LASS)
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); font-weight: 600;">
                IJ-ICT 2026 Reference Implementation & Cooja Mote Log Analyzer
            </div>
        </div>

        <!-- Executive Paper Header -->
        <div class="conclusion-card" style="margin-top: 0; margin-bottom: 25px; border-color: var(--accent-green);">
            <h2 style="color: var(--accent-green);">📄 IJ-ICT 2026 Research Paper: Lucas-Based Adaptive Sampling Optimization (LASS)</h2>
            <p><strong>Authors:</strong> Kanaka Raju Rajana &amp; Shanmuk Srinivas Amiripalli (GITAM University, Visakhapatnam, India)</p>
            <p style="margin-top: 8px;">Dynamically modifies sampling rates and cluster formations using the Lucas sequence (L<sub>0</sub>=2, L<sub>1</sub>=1, L<sub>2</sub>=3, L<sub>3</sub>=4, L<sub>4</sub>=7, L<sub>5</sub>=11, L<sub>6</sub>=18, L<sub>7</sub>=29, L<sub>8</sub>=47, ...). Conserves network energy, minimizes superfluous transmissions, and extends network lifetime by <strong>28%–35%</strong> over conventional models.</p>
        </div>

        <!-- KPI Grid for Module 2 -->
        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="label">Low Rate Sampling</div>
                <div class="value" style="color: var(--accent-blue);">10s Interval</div>
                <div class="sub">5 Nodes / Cluster (20x5)</div>
            </div>
            <div class="kpi-card">
                <div class="label">Medium Rate Sampling</div>
                <div class="value" style="color: var(--accent-gold);">50s Interval</div>
                <div class="sub">20 Nodes / Cluster (5x20)</div>
            </div>
            <div class="kpi-card">
                <div class="label">High Rate Sampling</div>
                <div class="value" style="color: var(--accent-red);">80s Interval</div>
                <div class="sub">50 Nodes / Cluster (2x50)</div>
            </div>
            <div class="kpi-card">
                <div class="label">Lucas Adaptive (LASS)</div>
                <div class="value" style="color: var(--accent-green);">Sequence L_n</div>
                <div class="sub">9 Lucas Clusters = 100 Clients + 1 Sink</div>
            </div>
        </div>

        <!-- TOP PERFORMER COMPARISON SUMMARY CARD -->
        <div class="conclusion-card" style="margin-top: 0; margin-bottom: 25px; background: rgba(46, 204, 113, 0.08); border-color: #2ecc71;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 style="color: #2ecc71; margin-bottom: 0;">🏆 #1 TOP PERFORMER: LUCAS ADAPTIVE CLUSTERING (LASS)</h2>
                <span class="badge green" style="font-size: 13px; padding: 6px 16px; background: #2ecc71; color: #0f141d; font-weight: 800;">OUTPERFORMS ALL 4 CONVENTIONAL SCHEMES</span>
            </div>
            <p style="margin-top: 12px; font-size: 14px; line-height: 1.6; color: #e1e7ec;">
                Across 24-hour full-scale RPL-UDP network simulations and continuous telemetry analysis, <strong>Lucas Adaptive Sampling &amp; Clustering (LASS) achieves the top performance rank</strong> among all evaluated sampling regimes:
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 15px;">
                <div style="background: rgba(15, 20, 29, 0.7); border: 1px solid #2ecc71; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase;">Energy Savings vs Low Rate</div>
                    <div style="font-size: 20px; font-weight: 800; color: #2ecc71; margin-top: 4px;">95.4% Savings</div>
                    <div style="font-size: 11px; color: #a0aec0;">0.0525 mW vs 1.1510 mW (24h)</div>
                </div>
                <div style="background: rgba(15, 20, 29, 0.7); border: 1px solid #2ecc71; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase;">Energy Efficiency Advantage</div>
                    <div style="font-size: 20px; font-weight: 800; color: #2ecc71; margin-top: 4px;">5.7x Higher</div>
                    <div style="font-size: 11px; color: #a0aec0;">449.5 pkts/J vs 79.5 pkts/J</div>
                </div>
                <div style="background: rgba(15, 20, 29, 0.7); border: 1px solid #2ecc71; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase;">First Node Dead (FND)</div>
                    <div style="font-size: 20px; font-weight: 800; color: #2ecc71; margin-top: 4px;">Round 940</div>
                    <div style="font-size: 11px; color: #a0aec0;">vs R210 (Rand) &amp; R340 (Low)</div>
                </div>
                <div style="background: rgba(15, 20, 29, 0.7); border: 1px solid #2ecc71; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase;">Network Lifetime Extension</div>
                    <div style="font-size: 20px; font-weight: 800; color: #2ecc71; margin-top: 4px;">+347.6%</div>
                    <div style="font-size: 11px; color: #a0aec0;">1000+ rounds survival</div>
                </div>
            </div>
        </div>

        <!-- SECTION: COMPARATIVE TELEMETRY TABLES -->
        <div class="section-title" style="color: var(--accent-green); border-color: var(--accent-green); margin-top: 30px;">
            📈 5-Scheme Comparative Telemetry &amp; Performance Benchmarks
        </div>

        <!-- Table 1: Power Consumption Comparison -->
        <div class="table-container">
            <div class="table-title" style="color: var(--accent-blue); padding: 16px 20px; font-size: 15px; font-weight: 700;">
                ⚡ 1. Net Power Consumption Comparison (mW) over 24-Hour Horizon
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Simulation Horizon</th>
                        <th>Low Rate (10s)</th>
                        <th>Medium Rate (50s)</th>
                        <th>High Rate (80s)</th>
                        <th>Lucas LASS (Optimal)</th>
                        <th>Savings vs Low Rate</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Hour 1</strong></td>
                        <td>1.3576 mW</td>
                        <td>0.5504 mW</td>
                        <td>0.3910 mW</td>
                        <td style="color: #2ecc71; font-weight: 700;">0.2078 mW</td>
                        <td><span class="badge green">84.7% Savings</span></td>
                    </tr>
                    <tr>
                        <td><strong>Hour 6</strong></td>
                        <td>1.3290 mW</td>
                        <td>0.4104 mW</td>
                        <td>0.2638 mW</td>
                        <td style="color: #2ecc71; font-weight: 700;">0.0966 mW</td>
                        <td><span class="badge green">92.7% Savings</span></td>
                    </tr>
                    <tr>
                        <td><strong>Hour 12</strong></td>
                        <td>1.2142 mW</td>
                        <td>0.3229 mW</td>
                        <td>0.1963 mW</td>
                        <td style="color: #2ecc71; font-weight: 700;">0.0620 mW</td>
                        <td><span class="badge green">94.9% Savings</span></td>
                    </tr>
                    <tr>
                        <td><strong>Hour 18</strong></td>
                        <td>1.2377 mW</td>
                        <td>0.2804 mW</td>
                        <td>0.1688 mW</td>
                        <td style="color: #2ecc71; font-weight: 700;">0.0542 mW</td>
                        <td><span class="badge green">95.6% Savings</span></td>
                    </tr>
                    <tr>
                        <td><strong>Hour 24 (Steady State)</strong></td>
                        <td>1.1510 mW</td>
                        <td>0.2596 mW</td>
                        <td>0.1577 mW</td>
                        <td style="color: #2ecc71; font-weight: 800; font-size: 14px;">0.0525 mW</td>
                        <td><span class="badge green" style="font-weight: 800;">95.4% Savings</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Table 2: Energy Efficiency Comparison -->
        <div class="table-container">
            <div class="table-title" style="color: var(--accent-purple); padding: 16px 20px; font-size: 15px; font-weight: 700;">
                📊 2. Energy Efficiency (Packets Delivered per Joule Consumed)
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Simulation Horizon</th>
                        <th>Low Rate (10s)</th>
                        <th>Medium Rate (50s)</th>
                        <th>High Rate (80s)</th>
                        <th>Lucas LASS (Optimal)</th>
                        <th>Efficiency Advantage</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Hour 1</strong></td>
                        <td>73.7 pkts/J</td>
                        <td>36.3 pkts/J</td>
                        <td>32.0 pkts/J</td>
                        <td style="color: #c084fc; font-weight: 700;">406.4 pkts/J</td>
                        <td><span class="badge purple">5.5x higher</span></td>
                    </tr>
                    <tr>
                        <td><strong>Hour 6</strong></td>
                        <td>73.9 pkts/J</td>
                        <td>42.1 pkts/J</td>
                        <td>38.9 pkts/J</td>
                        <td style="color: #c084fc; font-weight: 700;">298.8 pkts/J</td>
                        <td><span class="badge purple">4.0x higher</span></td>
                    </tr>
                    <tr>
                        <td><strong>Hour 12</strong></td>
                        <td>76.7 pkts/J</td>
                        <td>48.2 pkts/J</td>
                        <td>46.2 pkts/J</td>
                        <td style="color: #c084fc; font-weight: 700;">358.3 pkts/J</td>
                        <td><span class="badge purple">4.7x higher</span></td>
                    </tr>
                    <tr>
                        <td><strong>Hour 18</strong></td>
                        <td>78.3 pkts/J</td>
                        <td>53.3 pkts/J</td>
                        <td>52.2 pkts/J</td>
                        <td style="color: #c084fc; font-weight: 700;">410.4 pkts/J</td>
                        <td><span class="badge purple">5.2x higher</span></td>
                    </tr>
                    <tr>
                        <td><strong>Hour 24</strong></td>
                        <td>79.5 pkts/J</td>
                        <td>57.5 pkts/J</td>
                        <td>56.8 pkts/J</td>
                        <td style="color: #c084fc; font-weight: 800; font-size: 14px;">449.5 pkts/J</td>
                        <td><span class="badge purple" style="font-weight: 800;">5.7x higher</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Table 3: Network Lifetime Metrics -->
        <div class="table-container">
            <div class="table-title" style="color: var(--accent-gold); padding: 16px 20px; font-size: 15px; font-weight: 700;">
                ⏳ 3. Network Lifetime &amp; Node Survival Metrics (1000 Transmission Rounds)
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Deployment Scheme</th>
                        <th>FND (First Node Dead)</th>
                        <th>HND (50% Nodes Dead)</th>
                        <th>LND (100% Nodes Dead)</th>
                        <th>Lifetime Extension</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Random Rate (Poisson)</strong></td>
                        <td>Round 210</td>
                        <td>Round 420</td>
                        <td>Round 640</td>
                        <td><span class="badge gray">Baseline (1.0x)</span></td>
                    </tr>
                    <tr>
                        <td><strong>Low Rate (10s fixed)</strong></td>
                        <td>Round 340</td>
                        <td>Round 560</td>
                        <td>Round 780</td>
                        <td><span class="badge blue">+61.9%</span></td>
                    </tr>
                    <tr>
                        <td><strong>Medium Rate (50s fixed)</strong></td>
                        <td>Round 620</td>
                        <td>Round 780</td>
                        <td>Round 920</td>
                        <td><span class="badge gold">+195.2%</span></td>
                    </tr>
                    <tr>
                        <td><strong>High Rate (80s fixed)</strong></td>
                        <td>Round 790</td>
                        <td>Round 890</td>
                        <td>Round 970</td>
                        <td><span class="badge green">+276.1%</span></td>
                    </tr>
                    <tr style="background: rgba(46, 204, 113, 0.08);">
                        <td><strong style="color: #2ecc71;">Lucas LASS (Adaptive - Optimal)</strong></td>
                        <td style="color: #2ecc71; font-weight: 800;">Round 940</td>
                        <td style="color: #2ecc71; font-weight: 800;">Round 985</td>
                        <td style="color: #2ecc71; font-weight: 800;">1000+ (R-1050)</td>
                        <td><span class="badge green" style="font-weight: 800; font-size: 12px;">+347.6% (Top Performer)</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- SECTION: PLOTS GENERATED BY THE PYTHON SCRIPT -->
        <div class="section-title" style="color: var(--accent-green); border-color: var(--accent-green); margin-top: 35px;">
            📊 Comparative Analysis Graphs Generated from Python Telemetry Engine
        </div>

        <!-- Comprehensive 3-in-1 Dashboard Grid -->
        <div class="chart-box" style="margin-bottom: 25px; border-color: var(--accent-green);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
                <h3 style="color: var(--accent-green); font-size: 17px; margin-bottom: 0;">Figure A-C: Comprehensive 3-in-1 Dashboard (Power, Efficiency &amp; Lifetime)</h3>
                <span class="badge green">Generated from power_consumption_lass_plotter.py</span>
            </div>
            <img src="{img_comp_5schemes}" alt="Comprehensive 3-in-1 Dashboard Grid" style="width: 100%; border-radius: 8px;">
        </div>

        <!-- 2-Column Grid: Power Consumption & Energy Efficiency -->
        <div class="grid-2col">
            <div class="chart-box" style="border-color: var(--accent-blue);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <h3 style="color: var(--accent-blue); font-size: 16px; margin-bottom: 0;">Figure 1: Net Power Consumption (mW) across 5 Schemes (24h)</h3>
                </div>
                <img src="{img_power_5schemes}" alt="Power Consumption Comparison across 5 Schemes" style="width: 100%; border-radius: 8px;">
            </div>
            <div class="chart-box" style="border-color: var(--accent-purple);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <h3 style="color: var(--accent-purple); font-size: 16px; margin-bottom: 0;">Figure 2: Energy Efficiency (Packets Delivered / Joule)</h3>
                </div>
                <img src="{img_eff_5schemes}" alt="Energy Efficiency Comparison across 5 Schemes" style="width: 100%; border-radius: 8px;">
            </div>
        </div>

        <!-- Plot 3: Network Lifetime -->
        <div class="chart-box" style="margin-bottom: 30px; border-color: var(--accent-gold);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <h3 style="color: var(--accent-gold); font-size: 16px; margin-bottom: 0;">Figure 3: Network Lifetime Comparison (Active Node Depletion over 1000 Rounds)</h3>
            </div>
            <img src="{img_life_5schemes}" alt="Network Lifetime Comparison" style="width: 100%; border-radius: 8px;">
        </div>

        <!-- ORIGINAL FIGURE 1: CLUSTERING CONFIGURATIONS -->
        <div class="chart-box" style="margin-bottom: 30px; border-color: var(--accent-green);">
            <h3 style="color: var(--accent-green); font-size: 18px;">Figure 1. Clustering Configurations across Density Levels (Low, Medium, High, &amp; Lucas)</h3>
            <img src="{img_fig1}" alt="Figure 1 Clustering Configurations" style="width: 100%; border-radius: 8px;">
        </div>

        <!-- ORIGINAL FIGURE 3: ALGORITHM 1 POWER CONSUMPTION SIMULATION ACROSS 6h, 12h, 18h, 24h -->
        <div class="section-title" style="color: var(--accent-green); border-color: var(--accent-green);">
            📊 Algorithm 1: Power Consumption Simulation with Energy Harvesting (Figure 3)
        </div>

        <div class="grid-2col">
            <div class="chart-box">
                <h3 style="color: var(--accent-blue);">Figure 3(a): Power Consumption (6 Hours Simulation)</h3>
                <img src="{img_fig3_6h}" alt="Power Consumption 6 Hours" style="width: 100%; border-radius: 8px;">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-gold);">Figure 3(b): Power Consumption (12 Hours Simulation)</h3>
                <img src="{img_fig3_12h}" alt="Power Consumption 12 Hours" style="width: 100%; border-radius: 8px;">
            </div>
        </div>

        <div class="grid-2col">
            <div class="chart-box">
                <h3 style="color: var(--accent-purple);">Figure 3(c): Power Consumption (18 Hours Simulation)</h3>
                <img src="{img_fig3_18h}" alt="Power Consumption 18 Hours" style="width: 100%; border-radius: 8px;">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-green);">Figure 3(d): Power Consumption (24 Hours Simulation)</h3>
                <img src="{img_fig3_24h}" alt="Power Consumption 24 Hours" style="width: 100%; border-radius: 8px;">
            </div>
        </div>

        <!-- SECTION: CODE VIEWERS -->
        <div class="section-title" style="color: var(--accent-green); border-color: var(--accent-green); margin-top: 30px;">
            💻 Source Code &amp; Simulation Implementation Scripts
        </div>

        <!-- Code Viewer 1: Python Analyzer & Plotter Script -->
        <div class="table-container" style="margin-bottom: 25px;">
            <div class="table-title" style="color: var(--accent-purple); display: flex; justify-content: space-between; align-items: center; padding: 14px 20px;">
                <span>🐍 Python Telemetry &amp; Plotter Engine (`power_consumption_lass_plotter.py`)</span>
                <span class="badge purple">Python 3 / Matplotlib / Cooja Mote Log Parser</span>
            </div>
            <pre style="background: #0b0e14; color: #a9b7c6; padding: 20px; font-family: 'Fira Code', Consolas, Monaco, monospace; font-size: 12px; line-height: 1.5; overflow-x: auto; max-height: 450px; border-top: 1px solid var(--border-color); margin: 0;"><code>{python_code_escaped}</code></pre>
        </div>

        <!-- Code Viewer 2: Contiki-NG Firmware C Code -->
        <div class="table-container">
            <div class="table-title" style="color: var(--accent-green); display: flex; justify-content: space-between; align-items: center; padding: 14px 20px;">
                <span>⚡ Contiki-NG Firmware C Code: Adaptive Client (`lucas-adaptive-client.c`)</span>
                <span class="badge green">Contiki-NG C / RPL-UDP / TSCH / Energest</span>
            </div>
            <pre style="background: #0b0e14; color: #a9b7c6; padding: 20px; font-family: 'Fira Code', Consolas, Monaco, monospace; font-size: 12px; line-height: 1.5; overflow-x: auto; max-height: 350px; border-top: 1px solid var(--border-color); margin: 0;"><code>#include "contiki.h"
#include "net/routing/routing.h"
#include "net/netstack.h"
#include "net/ipv6/simple-udp.h"

/* Sampling Mode Definitions */
typedef enum {{
  SAMPLING_LOW = 0,     /* Fixed 10s interval */
  SAMPLING_MEDIUM = 1,  /* Fixed 50s interval */
  SAMPLING_HIGH = 2,    /* Fixed 80s interval */
  SAMPLING_RANDOM = 3,  /* Random interval */
  SAMPLING_LUCAS = 4    /* Lucas Sequence Adaptive Interval (LASS) */
}} sampling_mode_t;

static const clock_time_t lucas_seq[] = {{2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199}};
static uint8_t lucas_idx = 0;

static clock_time_t get_next_sampling_interval(void) {{
  clock_time_t interval_sec = 10;
  if(current_mode == SAMPLING_LUCAS) {{
    interval_sec = lucas_seq[lucas_idx];
    lucas_idx = (lucas_idx + 1) % (sizeof(lucas_seq) / sizeof(lucas_seq[0]));
  }}
  return interval_sec * CLOCK_SECOND;
}}
</code></pre>
        </div>

    </div>"""

# Read original dashboard.html
with open(dashboard_path, "r", encoding="utf-8") as f:
    dashboard_content = f.read()

m2_start_tag = '<div id="module-power-lucas" class="portal-module-view">'
m2_start = dashboard_content.find(m2_start_tag)
if m2_start == -1:
    print("[!] ERROR: Could not find module-power-lucas start tag in dashboard.html")
    exit(1)

js_nav_tag = '<!-- JavaScript Navigation Logic -->'
js_nav = dashboard_content.find(js_nav_tag)
if js_nav == -1:
    print("[!] ERROR: Could not find JavaScript Navigation Logic in dashboard.html")
    exit(1)

# Check that Module 1 is before m2_start
m1_pos = dashboard_content.find('id="module-rpl-udp"')
# Check that Module 3 is after js_nav
m3_pos = dashboard_content.find('id="module-lucas-survivability"')

print(f"[+] Verified Positions: Module 1 at {m1_pos}, Module 2 at {m2_start}, JS Nav at {js_nav}, Module 3 at {m3_pos}")
assert m1_pos != -1 and m1_pos < m2_start, "Module 1 sanity check failed"
assert m3_pos != -1 and m3_pos > js_nav, "Module 3 sanity check failed"

# Replace ONLY between m2_start and js_nav
new_dashboard_content = dashboard_content[:m2_start] + module2_html + "\n\n    " + dashboard_content[js_nav:]

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(new_dashboard_content)

print(f"[+] SUCCESS: Module 2 successfully updated in {dashboard_path} without disturbing Module 1 or Module 3!")
