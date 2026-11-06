import os
import base64

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"
dashboard_path = os.path.join(base_dir, "dashboard.html")

print("[+] Embedding Module 2 (Lucas-Based Adaptive Sampling Optimization) into dashboard.html...")

def get_b64(filename):
    path = os.path.join(base_dir, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    print(f"[!] Warning: missing {filename}")
    return ""

img_fig1 = get_b64("clustering_density_fig1.png")
img_fig3_6h = get_b64("power_consumption_fig3_6h.png")
img_fig3_12h = get_b64("power_consumption_fig3_12h.png")
img_fig3_18h = get_b64("power_consumption_fig3_18h.png")
img_fig3_24h = get_b64("power_consumption_fig3_24h.png")

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# Build HTML for Module 2
module2_html = f"""
    <!-- ========================================================================= -->
    <!-- MODULE 2: LUCAS-BASED ADAPTIVE SAMPLING OPTIMIZATION (IJ-ICT 2026)        -->
    <!-- ========================================================================= -->
    <div id="module-lucas-adaptive" class="portal-module-view">
        <div class="portal-back-bar">
            <button class="back-portal-btn" onclick="openModule('cover-portal-view')">
                <span>🏠</span>
                <span>Back to Research Portal Cover Page</span>
            </button>
            <div style="font-weight: 800; font-size: 15px; color: var(--accent-purple);">
                ⚡ Module 2: Lucas-Based Adaptive Sampling Optimization (LASS)
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); font-weight: 600;">
                Low, Medium, High, Random & Lucas Rates
            </div>
        </div>

        <!-- Executive Paper Header -->
        <div class="conclusion-card" style="margin-top: 0; margin-bottom: 25px;">
            <h2>📄 IJ-ICT 2026 Research Paper: Lucas-Based Adaptive Sampling Optimization (LASS)</h2>
            <p><strong>Authors:</strong> Kanaka Raju Rajana & Shanmuk Srinivas Amiripalli (GITAM University, Visakhapatnam, India)</p>
            <p style="margin-top: 8px;">Dynamically modifies sampling rates and cluster formations using the Lucas sequence ($L_0=2, L_1=1, L_2=3, L_3=4, L_4=7, L_5=11, L_6=18, L_7=29, L_8=47, \dots$). Conserves network energy, minimizes superfluous transmissions, and extends network lifetime by <strong>28%–35%</strong> over conventional models.</p>
        </div>

        <!-- KPI Grid for Module 2 -->
        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="label">Low Rate Sampling</div>
                <div class="value" style="color: var(--accent-blue);">10s Interval</div>
                <div class="sub">5 Nodes / Cluster</div>
            </div>
            <div class="kpi-card">
                <div class="label">Medium Rate Sampling</div>
                <div class="value" style="color: var(--accent-gold);">50s Interval</div>
                <div class="sub">20 Nodes / Cluster</div>
            </div>
            <div class="kpi-card">
                <div class="label">High Rate Sampling</div>
                <div class="value" style="color: var(--accent-red);">80s Interval</div>
                <div class="sub">50 Nodes / Cluster</div>
            </div>
            <div class="kpi-card">
                <div class="label">Lucas Adaptive (LASS)</div>
                <div class="value" style="color: var(--accent-green);">Sequence L_n</div>
                <div class="sub">Lucas Cluster Sizes</div>
            </div>
        </div>

        <!-- Figure 1: Clustering Configurations under Different Densities -->
        <div class="chart-box" style="margin-bottom: 30px;">
            <h3 style="color: var(--accent-purple); font-size: 18px;">Figure 1. Clustering Configurations across Density Levels (Low, Medium, High, & Lucas)</h3>
            <img src="{img_fig1}" alt="Figure 1 Clustering Configurations">
        </div>

        <!-- Figure 3: Algorithm 1 Power Consumption Simulation Results across 6h, 12h, 18h, 24h -->
        <div class="section-title">📊 Algorithm 1: Power Consumption Simulation with Energy Harvesting (Figure 3)</div>

        <div class="grid-2col">
            <div class="chart-box">
                <h3 style="color: var(--accent-blue);">Figure 3(a): Power Consumption (6 Hours Simulation)</h3>
                <img src="{img_fig3_6h}" alt="Power Consumption 6 Hours">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-gold);">Figure 3(b): Power Consumption (12 Hours Simulation)</h3>
                <img src="{img_fig3_12h}" alt="Power Consumption 12 Hours">
            </div>
        </div>

        <div class="grid-2col">
            <div class="chart-box">
                <h3 style="color: var(--accent-purple);">Figure 3(c): Power Consumption (18 Hours Simulation)</h3>
                <img src="{img_fig3_18h}" alt="Power Consumption 18 Hours">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-green);">Figure 3(d): Power Consumption (24 Hours Simulation)</h3>
                <img src="{img_fig3_24h}" alt="Power Consumption 24 Hours">
            </div>
        </div>

        <!-- Contiki-NG Firmware Code Viewers -->
        <div class="table-container">
            <div class="table-title">💻 Contiki-NG Firmware C Code: Adaptive Client (`lucas-adaptive-client.c`)</div>
            <pre style="background: #0b0e14; color: #a9b7c6; padding: 20px; font-family: monospace; font-size: 12px; overflow-x: auto; max-height: 300px;">
#include "contiki.h"
#include "net/routing/routing.h"
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
            </pre>
        </div>

    </div>
"""

# Inject Card Module 2 into the Cover Page Hub
card_module2_html = """
            <!-- Card Module 2: Lucas-Based Adaptive Sampling Optimization -->
            <div class="module-card" onclick="openModule('module-lucas-adaptive')">
                <div>
                    <div class="module-card-header">
                        <div class="module-card-icon">⚡</div>
                        <div class="module-card-tag" style="color: var(--accent-purple); background: rgba(155, 89, 182, 0.12); border-color: rgba(155, 89, 182, 0.3);">Active Module 2</div>
                    </div>
                    <div class="module-card-title">Lucas-Based Adaptive Sampling Optimization (LASS)</div>
                    <div class="module-card-desc">
                        Implementation of IJ-ICT 2026 research paper. Evaluates Low (10s), Medium (50s), High (80s), Random, and Lucas-based adaptive sampling strategies across 6h, 12h, 18h, and 24h simulations with energy harvesting.
                    </div>
                </div>
                <button class="module-card-btn" style="background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);">
                    <span>Launch Lucas Adaptive Sampling Suite</span>
                    <span>→</span>
                </button>
            </div>
"""

# Insert Card 2 into modules-grid
if "module-lucas-adaptive" not in content:
    content = content.replace('<div class="modules-grid">', '<div class="modules-grid">\n' + card_module2_html)
    # Insert Module 2 HTML before </body>
    content = content.replace("</body>", module2_html + "\n</body>")

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[+] SUCCESS: Added Module 2 (Lucas-Based Adaptive Sampling Optimization) to dashboard.html!")
