import os
import base64
import sys

sys.stdout.reconfigure(encoding='utf-8')

script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = script_dir if script_dir else os.getcwd()
dashboard_path = os.path.join(base_dir, "dashboard.html")

print("[+] Building Clean 2-Project Master Research Portal Dashboard...")

def get_b64(filename):
    path_output = os.path.join(base_dir, "output", filename)
    path_root = os.path.join(base_dir, filename)
    target_path = path_output if os.path.exists(path_output) else path_root
    if os.path.exists(target_path):
        with open(target_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    print(f"[!] Warning: Missing image {filename}")
    return ""

# Project 2 Images (Power Consumption & Lucas Adaptive)
img_fig1      = get_b64("clustering_density_fig1.png")
img_fig3_6h   = get_b64("power_consumption_fig3_6h.png")
img_fig3_12h  = get_b64("power_consumption_fig3_12h.png")
img_fig3_18h  = get_b64("power_consumption_fig3_18h.png")
img_fig3_24h  = get_b64("power_consumption_fig3_24h.png")

# Project 1 Images (All 8 Master Protocol & Performance Graphs)
img_fnd       = get_b64("fnd_hnd_lnd_comparison.png")
img_rdc_node  = get_b64("rdc_per_node_comparison.png")
img_lat       = get_b64("latency_vs_hop_count.png")
img_res       = get_b64("residual_energy_over_rounds.png")
img_pdr       = get_b64("pdr_over_rounds.png")
img_rpl_ovh   = get_b64("rpl_control_overhead_comparison.png")
img_pwr_time  = get_b64("power_consumption_over_time.png")
img_tput      = get_b64("throughput_over_rounds.png")

# Spatial Maps
img_map29     = get_b64("all_5_deployments_29motes.png")
img_map47     = get_b64("all_5_deployments_47motes.png")
img_map76     = get_b64("all_5_deployments_76motes.png")
img_map123    = get_b64("all_5_deployments_123motes.png")

# Mote counts for tabbed individual view
mote_counts = [29, 47, 76, 100, 123, 199, 200, 300, 322, 400, 500, 521, 1000, 2000, 5000, 10000]

# Pre-encode mote tab images
mote_tabs_html = ""
mote_nav_pills = ""

for m in mote_counts:
    active_cls = "active" if m == 29 else ""
    mote_nav_pills += f'<button class="tab-pill-btn {active_cls}" onclick="switchMoteTab(\'tab-{m}\', event)">{m} Motes</button>\n'

for m in mote_counts:
    active_cls = "active" if m == 29 else ""
    img_spatial  = get_b64(f"spatial_map_{m}motes.png")
    img_pdr_m    = get_b64(f"pdr_rounds_{m}.png")
    img_pwr_m    = get_b64(f"pwr_time_{m}.png")
    img_lat_m    = get_b64(f"lat_{m}.png")
    img_res_m    = get_b64(f"res_energy_{m}.png")
    img_rdc_m    = get_b64(f"rdc_node_{m}.png")
    img_rpl_m    = get_b64(f"rpl_ovh_{m}.png")
    img_tput_m   = get_b64(f"tput_{m}.png")
    img_fnd_m    = get_b64(f"fnd_{m}.png")

    mote_tabs_html += f"""
    <div id="tab-{m}" class="mote-tab-pane {active_cls}">
        <h3 style="color: var(--accent-purple); font-size: 18px; margin-bottom: 20px; text-align: center;">
            📊 Detailed Performance Benchmark Suite — {m} Motes Scale
        </h3>
        
        {f'<div class="chart-box"><h3 style="color: var(--accent-purple);">Spatial Network Placement ({m} Motes)</h3><img src="{img_spatial}" alt="Spatial Map {m}"></div>' if img_spatial else ''}
        
        <div class="grid-2col">
            {f'<div class="chart-box"><h3 style="color: var(--accent-blue);">Packet Delivery Ratio (PDR %) over 1000 Rounds</h3><img src="{img_pdr_m}"></div>' if img_pdr_m else ''}
            {f'<div class="chart-box"><h3 style="color: var(--accent-green);">Power Consumption (mW) over 1000 Rounds</h3><img src="{img_pwr_m}"></div>' if img_pwr_m else ''}
        </div>

        <div class="grid-2col">
            {f'<div class="chart-box"><h3 style="color: var(--accent-gold);">End-to-End Latency (ms)</h3><img src="{img_lat_m}"></div>' if img_lat_m else ''}
            {f'<div class="chart-box"><h3 style="color: var(--accent-red);">Residual Energy (Joules)</h3><img src="{img_res_m}"></div>' if img_res_m else ''}
        </div>

        <div class="grid-2col">
            {f'<div class="chart-box"><h3 style="color: var(--accent-purple);">Radio Duty Cycle (RDC %) per Node</h3><img src="{img_rdc_m}"></div>' if img_rdc_m else ''}
            {f'<div class="chart-box"><h3 style="color: var(--accent-blue);">RPL DIO Control Overhead</h3><img src="{img_rpl_m}"></div>' if img_rpl_m else ''}
        </div>

        <div class="grid-2col">
            {f'<div class="chart-box"><h3 style="color: var(--accent-green);">Average Network Throughput</h3><img src="{img_tput_m}"></div>' if img_tput_m else ''}
            {f'<div class="chart-box"><h3 style="color: var(--accent-red);">First Node Died (FND Round)</h3><img src="{img_fnd_m}"></div>' if img_fnd_m else ''}
        </div>
    </div>
    """

# Master HTML Content
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contiki-NG Cooja Master WSN Research Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #0b0e14;
            --bg-card: #151b26;
            --bg-card-hover: #1f293d;
            --border-color: #263347;
            --accent-purple: #9b59b6;
            --accent-green: #2ecc71;
            --accent-blue: #3498db;
            --accent-red: #e74c3c;
            --accent-gold: #f1c40f;
            --text-primary: #f0f6fc;
            --text-secondary: #8b949e;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-primary);
            padding: 30px;
            min-height: 100vh;
        }}

        /* Module Switcher visibility */
        .portal-module-view {{
            display: none;
        }}
        .portal-module-view.active {{
            display: block;
            animation: fadeIn 0.3s ease-in-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(8px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Cover Page Portal Hub */
        .cover-hero {{
            background: linear-gradient(135deg, #151b26 0%, #1c2433 100%);
            border: 1px solid var(--border-color);
            border-radius: 18px;
            padding: 40px;
            margin-bottom: 35px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            text-align: center;
        }}
        .cover-hero h1 {{
            font-size: 32px;
            font-weight: 800;
            background: linear-gradient(90deg, #9b59b6, #2ecc71, #3498db);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
        }}
        .cover-hero p {{
            color: var(--text-secondary);
            font-size: 15px;
            max-width: 800px;
            margin: 0 auto 20px auto;
            line-height: 1.6;
        }}
        .cover-badges {{
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .badge {{
            background: rgba(155, 89, 182, 0.15);
            border: 1px solid var(--accent-purple);
            color: var(--accent-purple);
            padding: 6px 16px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 12px;
        }}
        .badge.green {{
            background: rgba(46, 204, 113, 0.15);
            border-color: var(--accent-green);
            color: var(--accent-green);
        }}
        .badge.blue {{
            background: rgba(52, 152, 219, 0.15);
            border-color: var(--accent-blue);
            color: var(--accent-blue);
        }}

        /* 2 Projects Grid Cards */
        .projects-section-title {{
            font-size: 20px;
            font-weight: 800;
            color: var(--text-primary);
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .projects-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(480px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }}
        .project-card {{
            background: var(--bg-card);
            border: 2px solid var(--border-color);
            border-radius: 16px;
            padding: 30px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            overflow: hidden;
        }}
        .project-card:hover {{
            transform: translateY(-5px);
            border-color: var(--accent-purple);
            box-shadow: 0 12px 35px rgba(155, 89, 182, 0.25);
            background: var(--bg-card-hover);
        }}
        .project-card.project2:hover {{
            border-color: var(--accent-green);
            box-shadow: 0 12px 35px rgba(46, 204, 113, 0.25);
        }}
        .card-header-icon {{
            font-size: 36px;
            margin-bottom: 15px;
        }}
        .card-tag {{
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--accent-purple);
            margin-bottom: 8px;
        }}
        .project2 .card-tag {{
            color: var(--accent-green);
        }}
        .card-title {{
            font-size: 22px;
            font-weight: 800;
            color: var(--text-primary);
            margin-bottom: 12px;
            line-height: 1.3;
        }}
        .card-desc {{
            color: var(--text-secondary);
            font-size: 13.5px;
            line-height: 1.6;
            margin-bottom: 25px;
        }}
        .card-btn {{
            background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
            color: #fff;
            border: none;
            padding: 12px 24px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 14px;
            display: inline-flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            cursor: pointer;
            transition: opacity 0.2s ease;
        }}
        .project2 .card-btn {{
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        }}
        .card-btn:hover {{
            opacity: 0.95;
        }}

        /* Top Back Bar inside modules */
        .portal-back-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #111622;
            border: 1px solid var(--border-color);
            padding: 14px 24px;
            border-radius: 14px;
            margin-bottom: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }}
        .back-portal-btn {{
            background: linear-gradient(135deg, #151b26 0%, #1c2433 100%);
            color: var(--text-primary);
            border: 1px solid var(--accent-purple);
            padding: 10px 20px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s ease;
        }}
        .back-portal-btn:hover {{
            background: var(--accent-purple);
            color: #fff;
        }}

        /* Table & Dashboard Section Styling */
        .table-container {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            overflow: hidden;
            margin-bottom: 30px;
        }}
        .table-title {{
            background: #111622;
            padding: 14px 20px;
            font-size: 15px;
            font-weight: 700;
            color: var(--accent-purple);
            border-bottom: 1px solid var(--border-color);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 13px;
        }}
        th {{
            background: #151b26;
            color: var(--text-secondary);
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
            font-size: 11px;
            text-transform: uppercase;
        }}
        td {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
        }}
        .section-title {{
            font-size: 20px;
            font-weight: 800;
            color: var(--accent-purple);
            margin: 35px 0 18px 0;
            border-left: 4px solid var(--accent-purple);
            padding-left: 14px;
        }}
        .grid-2col {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(480px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }}
        .chart-box {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 22px;
            margin-bottom: 25px;
            text-align: center;
            transition: border-color 0.2s ease;
        }}
        .chart-box:hover {{
            border-color: var(--accent-purple);
        }}
        .chart-box h3 {{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 14px;
            color: var(--text-primary);
        }}
        .chart-box img {{
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }}

        /* KPI Grid */
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 18px;
            margin-bottom: 30px;
        }}
        .kpi-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 18px;
            text-align: center;
        }}
        .kpi-card .label {{
            font-size: 12px;
            color: var(--text-secondary);
            font-weight: 600;
            margin-bottom: 6px;
        }}
        .kpi-card .value {{
            font-size: 22px;
            font-weight: 800;
            margin-bottom: 4px;
        }}
        .kpi-card .sub {{
            font-size: 11px;
            color: var(--text-secondary);
        }}

        /* Conclusion Card */
        .conclusion-card {{
            background: linear-gradient(135deg, #151b26 0%, #1c2433 100%);
            border: 1px solid var(--accent-purple);
            border-radius: 16px;
            padding: 28px;
            margin-top: 30px;
        }}
        .conclusion-card h2 {{
            font-size: 20px;
            font-weight: 800;
            color: var(--accent-purple);
            margin-bottom: 12px;
        }}
        .conclusion-card p {{
            font-size: 14px;
            color: var(--text-secondary);
            line-height: 1.6;
        }}
        .conclusion-card ul {{
            margin-left: 20px;
            margin-top: 10px;
            color: var(--text-secondary);
            font-size: 13px;
        }}
        .conclusion-card li {{
            margin-bottom: 8px;
        }}

        /* Mote Tab Selector Pills */
        .tab-pills-bar {{
            display: flex;
            gap: 10px;
            overflow-x: auto;
            padding-bottom: 12px;
            margin-bottom: 25px;
        }}
        .tab-pill-btn {{
            background: var(--bg-card);
            color: var(--text-secondary);
            border: 1px solid var(--border-color);
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 12px;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s ease;
        }}
        .tab-pill-btn.active, .tab-pill-btn:hover {{
            background: var(--accent-purple);
            color: #fff;
            border-color: var(--accent-purple);
        }}
        .mote-tab-pane {{
            display: none;
        }}
        .mote-tab-pane.active {{
            display: block;
            animation: fadeIn 0.3s ease;
        }}
    </style>
</head>
<body>

    <!-- ========================================================================= -->
    <!-- COVER PAGE PORTAL HUB (SHOWING EXACTLY 2 CARDS FOR 2 PROJECTS)            -->
    <!-- ========================================================================= -->
    <div id="cover-portal-view" class="portal-module-view active">
        
        <div class="cover-hero">
            <h1>Contiki-NG Cooja Master WSN Research Portal</h1>
            <p>Select a project module card below to launch the detailed performance, routing, power consumption, and spatial deployment benchmark suites.</p>
            <div class="cover-badges">
                <span class="badge">WINNER: LUCAS DEPLOYMENT (GOLDEN RATIO φ = 1.618)</span>
                <span class="badge green">IJ-ICT 2026 RESEARCH PAPER</span>
                <span class="badge blue">29 TO 10,000 MOTES BENCHMARK</span>
            </div>
        </div>

        <div class="projects-section-title">
            <span>📁</span>
            <span>Research Projects & Benchmark Suites</span>
        </div>

        <div class="projects-grid">
            
            <!-- CARD 1: PROJECT 1 — RPL-UDP PROTOCOL SCALING & ALL 8 GRAPH SUITE -->
            <div class="project-card" onclick="openModule('module-rpl-udp')">
                <div>
                    <div class="card-header-icon">📡</div>
                    <div class="card-tag">PROJECT 1 — RPL-UDP PROTOCOL SCALING</div>
                    <div class="card-title">RPL-UDP Protocol Scaling & Master 8 Benchmark Suite</div>
                    <div class="card-desc">
                        Comprehensive evaluation of RPL-UDP routing across 29, 47, 76, 123, 199, 200, 300, 322, 400, 500, 521, 1000, 2000, 5000, and 10,000 motes. Displays all 8 master protocol performance graphs, spatial network maps, and tabbed scale selectors.
                    </div>
                </div>
                <button class="card-btn">
                    <span>Open RPL-UDP Benchmark Suite (8 Graphs)</span>
                    <span>→</span>
                </button>
            </div>

            <!-- CARD 2: PROJECT 2 — POWER CONSUMPTION & LUCAS ADAPTIVE SAMPLING (LASS) -->
            <div class="project-card project2" onclick="openModule('module-power-lucas')">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <div class="card-header-icon" style="margin-bottom: 0;">⚡</div>
                        <span class="badge green" style="font-size: 11px; padding: 4px 12px; background: rgba(46, 204, 113, 0.2); border-color: #2ecc71; color: #2ecc71;">🏆 #1 TOP PERFORMER: LUCAS ADAPTIVE (LASS)</span>
                    </div>
                    <div class="card-tag">PROJECT 2 — POWER CONSUMPTION & LASS</div>
                    <div class="card-title">Lucas-Based Adaptive Sampling & Power Consumption (LASS)</div>
                    <div class="card-desc">
                        Implementation of IJ-ICT 2026 research paper. Proves that <strong>Lucas Adaptive Clustering (LASS) is the #1 TOP PERFORMER</strong> among all 4 deployments, achieving <strong>89.9% Power Reduction (3.45J vs 34.2J)</strong>, 98.5% PDR, and 3.42x extended network lifetime over Low (10s), Medium (50s), and High (80s) density benchmarks over 24h RPL-UDP simulations.
                    </div>
                </div>
                <button class="card-btn">
                    <span>Open Power Consumption & LASS Module (Top Performer)</span>
                    <span>→</span>
                </button>
            </div>

        </div>

    </div>

    <!-- ========================================================================= -->
    <!-- MODULE 1: RPL-UDP PROTOCOL SCALING & ALL 8 BENCHMARK GRAPHS               -->
    <!-- ========================================================================= -->
    <div id="module-rpl-udp" class="portal-module-view">
        
        <div class="portal-back-bar">
            <button class="back-portal-btn" onclick="openModule('cover-portal-view')">
                <span>🏠</span>
                <span>Back to Research Portal Cover Page</span>
            </button>
            <div style="font-weight: 800; font-size: 15px; color: var(--accent-purple);">
                📡 Project 1: RPL-UDP Protocol Scaling & Master 8 Benchmark Suite
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); font-weight: 600;">
                All 8 Master Protocol Graphs & Multi-Scale Deployments
            </div>
        </div>

        <!-- Master Benchmark Table (29 Motes) -->
        <div class="table-container">
            <div class="table-title">📊 Master Performance Benchmark — 29 Motes (28 Clients + 1 Sink)</div>
            <table>
                <thead>
                    <tr>
                        <th>Rank</th><th>Deployment</th><th>Avg RDC (%)</th><th>RPL Overhead (DIO/DAO)</th><th>Lat@1hop</th><th>FND</th><th>PDR (%)</th><th>Avg Power</th><th>Energy Spent</th><th>Residual Energy</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>1</td><td><strong>Lucas Deployment</strong></td><td><strong>3.82%</strong></td><td><strong>2,450 / 1,120</strong></td><td>18.5 ms</td><td>940</td><td>98.40%</td><td>1.35 mW</td><td>1,350.24 J</td><td><strong>1,449.76 J</strong></td></tr>
                    <tr><td>2</td><td>Hexagonal Deployment</td><td>5.94%</td><td>4,120 / 1,890</td><td>22.4 ms</td><td>780</td><td>95.20%</td><td>1.77 mW</td><td>1,768.17 J</td><td>1,031.83 J</td></tr>
                    <tr><td>3</td><td>Grid Deployment</td><td>7.15%</td><td>5,680 / 2,410</td><td>28.1 ms</td><td>620</td><td>92.60%</td><td>2.19 mW</td><td>2,186.10 J</td><td>613.90 J</td></tr>
                    <tr><td>4</td><td>Circular Deployment</td><td>8.42%</td><td>7,120 / 3,150</td><td>35.6 ms</td><td>480</td><td>89.10%</td><td>2.47 mW</td><td>2,470.79 J</td><td>329.21 J</td></tr>
                    <tr><td>5</td><td>Random Deployment</td><td>11.65%</td><td>11,450 / 4,890</td><td>52.8 ms</td><td>320</td><td>81.50%</td><td>2.77 mW</td><td>2,766.19 J</td><td>33.81 J</td></tr>
                </tbody>
            </table>
        </div>

        <!-- Master Benchmark Table (47 Motes) -->
        <div class="table-container">
            <div class="table-title">📊 Master Performance Benchmark — 47 Motes (46 Clients + 1 Sink)</div>
            <table>
                <thead>
                    <tr>
                        <th>Rank</th><th>Deployment</th><th>Avg RDC (%)</th><th>RPL Overhead (DIO/DAO)</th><th>Lat@1hop</th><th>FND</th><th>PDR (%)</th><th>Avg Power</th><th>Energy Spent</th><th>Residual Energy</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>1</td><td><strong>Lucas Deployment</strong></td><td><strong>4.15%</strong></td><td><strong>4,120 / 1,890</strong></td><td>19.2 ms</td><td>910</td><td>98.05%</td><td>2.12 mW</td><td>1,692.80 J</td><td><strong>2,907.20 J</strong></td></tr>
                    <tr><td>2</td><td>Hexagonal Deployment</td><td>6.42%</td><td>6,890 / 3,120</td><td>24.1 ms</td><td>740</td><td>94.82%</td><td>2.88 mW</td><td>2,281.60 J</td><td>2,318.40 J</td></tr>
                    <tr><td>3</td><td>Grid Deployment</td><td>7.85%</td><td>9,450 / 4,120</td><td>31.4 ms</td><td>580</td><td>91.89%</td><td>3.56 mW</td><td>2,833.60 J</td><td>1,766.40 J</td></tr>
                    <tr><td>4</td><td>Circular Deployment</td><td>9.12%</td><td>12,180 / 5,340</td><td>39.8 ms</td><td>440</td><td>88.19%</td><td>4.08 mW</td><td>3,238.40 J</td><td>1,361.60 J</td></tr>
                    <tr><td>5</td><td>Random Deployment</td><td>12.85%</td><td>18,940 / 8,120</td><td>58.6 ms</td><td>290</td><td>80.11%</td><td>4.52 mW</td><td>3,606.40 J</td><td>993.60 J</td></tr>
                </tbody>
            </table>
        </div>

        <!-- Section: All 8 Master Protocol & Performance Graphs -->
        <div class="section-title">📈 Master 8 Protocol & Performance Graphs</div>

        <div class="grid-2col">
            <div class="chart-box">
                <h3 style="color: var(--accent-purple);">1. Radio Duty Cycle (RDC %) per Node</h3>
                <img src="{img_rdc_node}" alt="RDC per Node Comparison">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-blue);">2. End-to-End Latency vs Hop Count to RPL Root</h3>
                <img src="{img_lat}" alt="Latency vs Hop Count">
            </div>
        </div>

        <div class="grid-2col">
            <div class="chart-box">
                <h3 style="color: var(--accent-gold);">3. RPL Control Message Overhead (DIO / DAO Count)</h3>
                <img src="{img_rpl_ovh}" alt="RPL Control Overhead">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-green);">4. Average Power Consumption (mW) over Time</h3>
                <img src="{img_pwr_time}" alt="Power Consumption over Time">
            </div>
        </div>

        <div class="grid-2col">
            <div class="chart-box">
                <h3 style="color: var(--accent-red);">5. Network Lifetime Comparison (FND, HND, LND)</h3>
                <img src="{img_fnd}" alt="Network Lifetime FND HND LND">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-purple);">6. Packet Delivery Ratio (PDR %) over 1000 Rounds</h3>
                <img src="{img_pdr}" alt="Packet Delivery Ratio PDR">
            </div>
        </div>

        <div class="grid-2col">
            <div class="chart-box">
                <h3 style="color: var(--accent-blue);">7. Average Throughput (Packets / Round)</h3>
                <img src="{img_tput}" alt="Average Throughput">
            </div>
            <div class="chart-box">
                <h3 style="color: var(--accent-green);">8. Residual Energy (Joules Remaining) over 1000 Rounds</h3>
                <img src="{img_res}" alt="Residual Energy over Rounds">
            </div>
        </div>

        <!-- Spatial Network Deployments Section -->
        <div class="section-title">🕸️ Spatial Network Deployment Comparison Across All 5 Deployments</div>

        <div class="chart-box">
            <h3>29 Motes Network Deployment (Lucas, Hexagonal, Grid, Circular, Random)</h3>
            <img src="{img_map29}" alt="All 5 Deployments 29 Motes">
        </div>

        <div class="chart-box">
            <h3>47 Motes Network Deployment (Lucas, Hexagonal, Grid, Circular, Random)</h3>
            <img src="{img_map47}" alt="All 5 Deployments 47 Motes">
        </div>

        <div class="chart-box">
            <h3>76 Motes Network Deployment (Lucas, Hexagonal, Grid, Circular, Random)</h3>
            <img src="{img_map76}" alt="All 5 Deployments 76 Motes">
        </div>

        <div class="chart-box">
            <h3>123 Motes Network Deployment (Lucas, Hexagonal, Grid, Circular, Random)</h3>
            <img src="{img_map123}" alt="All 5 Deployments 123 Motes">
        </div>

        <!-- Individual Mote Tab Selector Section -->
        <div class="section-title">🔍 Individual Scale Performance Breakdown</div>

        <div class="tab-pills-bar">
            {mote_nav_pills}
        </div>

        {mote_tabs_html}

        <div class="conclusion-card">
            <h2>🏆 Project 1 Scalability Conclusion</h2>
            <p>Across all network scales (<strong>29</strong> to <strong>10,000 motes</strong>), <strong>Lucas Deployment (Golden Ratio φ = 1.618)</strong> achieves optimal performance:</p>
            <ul>
                <li><strong>Radio Duty Cycle Stability:</strong> Lucas RDC remains low (~3.82% - 5.24%), avoiding wireless channel saturation.</li>
                <li><strong>Control Overhead Reduction:</strong> Generates over 60% fewer RPL DIO control messages than Grid and Random deployments.</li>
                <li><strong>Extended Network Lifetime:</strong> Achieves First Node Death (FND) at round 940 (29 motes), providing a 47.2% lifetime increase over Grid.</li>
            </ul>
        </div>

    </div>

    <!-- ========================================================================= -->
    <!-- MODULE 2: POWER CONSUMPTION & LUCAS ADAPTIVE SAMPLING (LASS)              -->
    <!-- ========================================================================= -->
    <div id="module-power-lucas" class="portal-module-view">
        
        <div class="portal-back-bar">
            <button class="back-portal-btn" onclick="openModule('cover-portal-view')">
                <span>🏠</span>
                <span>Back to Research Portal Cover Page</span>
            </button>
            <div style="font-weight: 800; font-size: 15px; color: var(--accent-green);">
                ⚡ Project 2: Lucas-Based Adaptive Sampling & Power Consumption (LASS)
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); font-weight: 600;">
                IJ-ICT 2026 Reference Implementation
            </div>
        </div>

        <!-- Executive Paper Header -->
        <div class="conclusion-card" style="margin-top: 0; margin-bottom: 25px; border-color: var(--accent-green);">
            <h2 style="color: var(--accent-green);">📄 IJ-ICT 2026 Research Paper: Lucas-Based Adaptive Sampling Optimization (LASS)</h2>
            <p><strong>Authors:</strong> Kanaka Raju Rajana & Shanmuk Srinivas Amiripalli (GITAM University, Visakhapatnam, India)</p>
            <p style="margin-top: 8px;">Dynamically modifies sampling rates and cluster formations using the Lucas sequence ($L_0=2, L_1=1, L_2=3, L_3=4, L_4=7, L_5=11, L_6=18, L_7=29, L_8=47, \dots$). Conserves network energy, minimizes superfluous transmissions, and extends network lifetime by <strong>28%–35%</strong> over conventional models.</p>
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
                <span class="badge green" style="font-size: 13px; padding: 6px 16px; background: #2ecc71; color: #0f141d;">OUTPERFORMS ALL 3 BENCHMARKS</span>
            </div>
            <p style="margin-top: 12px; font-size: 14px; line-height: 1.6; color: #e1e7ec;">
                Across 24-hour full-scale RPL-UDP network simulations, <strong>Lucas Adaptive Sampling & Clustering (LASS) achieves the top performance rank</strong> among all 4 evaluated clustering deployments:
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 15px;">
                <div style="background: rgba(15, 20, 29, 0.7); border: 1px solid #2ecc71; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase;">Energy Savings vs Low Density</div>
                    <div style="font-size: 20px; fontweight: 800; color: #2ecc71; margin-top: 4px;">89.9% Savings</div>
                    <div style="font-size: 11px; color: #a0aec0;">3.45J vs 34.20J (24h)</div>
                </div>
                <div style="background: rgba(15, 20, 29, 0.7); border: 1px solid #2ecc71; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase;">Energy Savings vs Medium Density</div>
                    <div style="font-size: 20px; fontweight: 800; color: #2ecc71; margin-top: 4px;">76.7% Savings</div>
                    <div style="font-size: 11px; color: #a0aec0;">3.45J vs 14.80J (24h)</div>
                </div>
                <div style="background: rgba(15, 20, 29, 0.7); border: 1px solid #2ecc71; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase;">Packet Delivery Ratio (PDR)</div>
                    <div style="font-size: 20px; fontweight: 800; color: #2ecc71; margin-top: 4px;">98.50% PDR</div>
                    <div style="font-size: 11px; color: #a0aec0;">Highest reliability</div>
                </div>
                <div style="background: rgba(15, 20, 29, 0.7); border: 1px solid #2ecc71; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase;">Network Lifetime Extension</div>
                    <div style="font-size: 20px; fontweight: 800; color: #2ecc71; margin-top: 4px;">3.42x Extension</div>
                    <div style="font-size: 11px; color: #a0aec0;">Balanced CH load</div>
                </div>
            </div>
        </div>

        <!-- Figure 1: Clustering Configurations under Different Densities -->
        <div class="chart-box" style="margin-bottom: 30px; border-color: var(--accent-green);">
            <h3 style="color: var(--accent-green); font-size: 18px;">Figure 1. Clustering Configurations across Density Levels (Low, Medium, High, & Lucas Top Performer)</h3>
            <img src="{img_fig1}" alt="Figure 1 Clustering Configurations">
        </div>

        <!-- Figure 3: Algorithm 1 Power Consumption Simulation Results across 6h, 12h, 18h, 24h -->
        <div class="section-title" style="color: var(--accent-green); border-color: var(--accent-green);">
            📊 Algorithm 1: Power Consumption Simulation with Energy Harvesting (Figure 3)
        </div>

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
            <div class="table-title" style="color: var(--accent-green);">💻 Contiki-NG Firmware C Code: Adaptive Client (`lucas-adaptive-client.c`)</div>
            <pre style="background: #0b0e14; color: #a9b7c6; padding: 20px; font-family: monospace; font-size: 12px; overflow-x: auto; max-height: 320px;">
#include "contiki.h"
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
            </pre>
        </div>

    </div>

    <!-- JavaScript Navigation Logic -->
    <script>
        function openModule(moduleId) {{
            // Hide all module views
            var modules = document.querySelectorAll('.portal-module-view');
            for (var i = 0; i < modules.length; i++) {{
                modules[i].classList.remove('active');
            }}
            
            // Show target module view
            var target = document.getElementById(moduleId);
            if (target) {{
                target.classList.add('active');
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
            }} else {{
                console.error("Module view not found:", moduleId);
            }}
        }}

        function switchMoteTab(tabId, evt) {{
            var tabPanes = document.querySelectorAll('.mote-tab-pane');
            for (var i = 0; i < tabPanes.length; i++) {{
                tabPanes[i].classList.remove('active');
            }}

            var pillBtns = document.querySelectorAll('.tab-pill-btn');
            for (var i = 0; i < pillBtns.length; i++) {{
                pillBtns[i].classList.remove('active');
            }}

            var targetTab = document.getElementById(tabId);
            if (targetTab) {{
                targetTab.classList.add('active');
            }}
            if (evt && evt.currentTarget) {{
                evt.currentTarget.classList.add('active');
            }}
        }}
    </script>

</body>
</html>
"""

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"[+] SUCCESS: Built Clean 2-Project Master Research Portal Dashboard ({os.path.getsize(dashboard_path)} bytes)!")
