import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

dashboard_path = r"c:\Users\Kanaka Raju\Desktop\joy29\dashboard.html"

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

print("[+] Finalizing Cover Page Hub with 3 Card-Type Modules...")

# Build clean Cover Portal HTML
clean_cover_portal_html = """
    <!-- ========================================================================= -->
    <!-- COVER PAGE HUB / PORTAL VIEW (DEFAULT LOAD VIEW)                         -->
    <!-- ========================================================================= -->
    <div id="cover-portal-view" class="portal-module-view active">
        <div class="cover-hero">
            <h1>Contiki-NG Cooja Master WSN Research Portal</h1>
            <p>Welcome to the Multi-Module Wireless Sensor Network Research Hub. Select any research module card below to launch protocol analytics, simulation diagnostics, adaptive sampling algorithms, or smart home topology survivability suites in Contiki-NG.</p>
            <div class="cover-badges">
                <div class="cover-badge">🚀 Active Modules: <span>3 Integrated Card Modules</span></div>
                <div class="cover-badge">📊 Network Scales: <span>20 to 10,000 Motes</span></div>
                <div class="cover-badge">🏆 Winner Layout: <span>Lucas Golden Ratio (φ = 1.618)</span></div>
            </div>
        </div>

        <div class="modules-section-title">
            <span>🧩</span> Research Modules & Simulation Frameworks (3 Card Modules)
        </div>

        <div class="modules-grid">
            <!-- Card Module 1: Contiki-NG Cooja Simulation using RPL-UDP -->
            <div class="module-card" onclick="openModule('module-rpl-udp')">
                <div>
                    <div class="module-card-header">
                        <div class="module-card-icon">📡</div>
                        <div class="module-card-tag">Active Module 1</div>
                    </div>
                    <div class="module-card-title">Contiki-NG Cooja Simulation using RPL-UDP</div>
                    <div class="module-card-desc">
                        Comprehensive 16-Scale (29 to 10,000 Motes) benchmark evaluating Lucas Golden Ratio, Hexagonal, Grid, Circular, and Random deployments across 128 individual high-res plots (RDC %, RPL Control Overhead, Latency, Power, Energy, PDR, & Throughput).
                    </div>
                </div>
                <button class="module-card-btn">
                    <span>Launch Contiki-NG RPL-UDP Suite</span>
                    <span>→</span>
                </button>
            </div>

            <!-- Card Module 2: Lucas-Based Adaptive Sampling Optimization (IJ-ICT 2026) -->
            <div class="module-card" onclick="openModule('module-power-lucas')">
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

            <!-- Card Module 3: Smart Home Survivability via Lucas TGO Clustering (ETASR 2025) -->
            <div class="module-card" onclick="openModule('module-lucas-survivability')">
                <div>
                    <div class="module-card-header">
                        <div class="module-card-icon">🛡️</div>
                        <div class="module-card-tag" style="color: var(--accent-gold); background: rgba(241, 196, 15, 0.12); border-color: rgba(241, 196, 15, 0.3);">Active Module 3</div>
                    </div>
                    <div class="module-card-title">Smart Home Survivability via Lucas TGO Clustering</div>
                    <div class="module-card-desc">
                        Implementation of attached document (ETASR 2025). Evaluates edge & node survivability under random node failures using Lucas numbers ($L_n = [3, 4, 7, 11, 18, 29]$) and Trimet Graph Optimization (TGO) across 20 to 100 motes in Contiki-NG.
                    </div>
                </div>
                <button class="module-card-btn" style="background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);">
                    <span>Launch Smart Home Survivability Suite</span>
                    <span>→</span>
                </button>
            </div>
        </div>

        <!-- Final Dashboard Conclusion Banner -->
        <div class="cover-hero" style="margin-top: 20px; margin-bottom: 30px; background: radial-gradient(circle at top center, rgba(46, 204, 113, 0.18) 0%, rgba(11, 14, 20, 0) 75%); border-color: var(--accent-green);">
            <h2 style="font-size: 26px; font-weight: 800; color: var(--accent-green); margin-bottom: 10px;">
                🎉 Dashboard Complete: 3 Research Card Modules Fully Integrated
            </h2>
            <p style="font-size: 14px; max-width: 900px; margin: 0 auto; color: var(--text-secondary);">
                This research dashboard is successfully concluded with 3 card-type modules: <strong>Module 1 (RPL-UDP 16-Scale Benchmark)</strong>, <strong>Module 2 (Lucas Adaptive Sampling LASS)</strong>, and <strong>Module 3 (Smart Home Survivability via Lucas TGO)</strong>.
            </p>
        </div>
    </div>
"""

# Replace cover-portal-view block
c_start = content.find('<div id="cover-portal-view"')
c_end = content.find('<div id="module-rpl-udp"')

if c_start != -1 and c_end != -1:
    content = content[:c_start] + clean_cover_portal_html + "\n    " + content[c_end:]
    print("[+] Replaced cover portal view with clean 3-card layout!")
else:
    print("[!] Error finding cover-portal-view or module-rpl-udp tags.")

# Check for openModule function in JS script
if "module-power-lucas" not in content:
    content = content.replace("openModule('module-lucas-adaptive')", "openModule('module-power-lucas')")

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[+] SUCCESS: dashboard.html finalized with 3 card-type modules!")
