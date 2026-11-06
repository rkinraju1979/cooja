import os

base_dir = r"c:\Users\Kanaka Raju\Desktop\joy29"
dashboard_path = os.path.join(base_dir, "dashboard.html")

print("[+] Updating dashboard.html with Cover Page & Modular Card Architecture...")

with open(dashboard_path, "r", encoding="utf-8") as f:
    content = f.read()

# CSS for Modular Cover Page & Card Layout
portal_css = """
        /* Modular Cover Page & Hub View Styling */
        .portal-module-view { display: none; }
        .portal-module-view.active { display: block; animation: fadeIn 0.3s ease; }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .cover-hero {
            text-align: center;
            padding: 50px 25px 35px;
            background: radial-gradient(circle at top center, rgba(155, 89, 182, 0.22) 0%, rgba(11, 14, 20, 0) 75%);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            margin-bottom: 35px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }
        .cover-hero h1 {
            font-size: 38px;
            font-weight: 800;
            background: linear-gradient(135deg, #9b59b6 0%, #2ecc71 45%, #3498db 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 14px;
            letter-spacing: -0.5px;
        }
        .cover-hero p {
            font-size: 15px;
            color: var(--text-secondary);
            max-width: 850px;
            margin: 0 auto 25px;
            line-height: 1.6;
        }
        .cover-badges {
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
        }
        .cover-badge {
            background: #151b26;
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 8px 16px;
            border-radius: 30px;
            font-size: 13px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .cover-badge span { color: var(--accent-purple); font-weight: 700; }

        .modules-section-title {
            font-size: 22px;
            font-weight: 800;
            color: var(--accent-purple);
            margin-bottom: 22px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .modules-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 28px;
            margin-bottom: 50px;
        }
        .module-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 18px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }
        .module-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--accent-purple), var(--accent-green), var(--accent-blue));
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .module-card:hover {
            transform: translateY(-6px);
            border-color: var(--accent-purple);
            box-shadow: 0 16px 40px rgba(155, 89, 182, 0.25);
        }
        .module-card:hover::before { opacity: 1; }

        .module-card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 16px;
        }
        .module-card-icon {
            font-size: 42px;
            background: rgba(155, 89, 182, 0.12);
            padding: 12px;
            border-radius: 14px;
            border: 1px solid rgba(155, 89, 182, 0.3);
        }
        .module-card-tag {
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--accent-green);
            background: rgba(46, 204, 113, 0.12);
            border: 1px solid rgba(46, 204, 113, 0.3);
            padding: 4px 10px;
            border-radius: 20px;
        }
        .module-card-title {
            font-size: 22px;
            font-weight: 800;
            color: var(--text-primary);
            margin-bottom: 12px;
            line-height: 1.3;
        }
        .module-card-desc {
            font-size: 13.5px;
            color: var(--text-secondary);
            line-height: 1.6;
            margin-bottom: 24px;
            flex-grow: 1;
        }
        .module-card-btn {
            background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
            color: #ffffff;
            border: none;
            padding: 14px 22px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 14px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            transition: all 0.25s ease;
            width: 100%;
            cursor: pointer;
        }
        .module-card:hover .module-card-btn {
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
            box-shadow: 0 4px 18px rgba(46, 204, 113, 0.4);
        }

        /* Card Add Placeholder */
        .module-card-add {
            border: 2px dashed var(--border-color);
            background: rgba(21, 27, 38, 0.5);
            text-align: center;
            align-items: center;
            justify-content: center;
            min-height: 280px;
        }
        .module-card-add:hover {
            border-color: var(--accent-green);
            background: rgba(46, 204, 113, 0.04);
            box-shadow: 0 10px 30px rgba(46, 204, 113, 0.15);
        }

        /* Back to Cover Navigation Header */
        .portal-back-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #111622;
            border: 1px solid var(--accent-purple);
            padding: 14px 24px;
            border-radius: 14px;
            margin-bottom: 25px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        .back-portal-btn {
            background: linear-gradient(135deg, #151b26 0%, #1c2433 100%);
            color: var(--text-primary);
            border: 1px solid var(--accent-purple);
            padding: 10px 20px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 13.5px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            transition: all 0.25s ease;
        }
        .back-portal-btn:hover {
            background: var(--accent-purple);
            color: #ffffff;
            box-shadow: 0 0 18px rgba(155, 89, 182, 0.5);
            transform: translateY(-2px);
        }
"""

if "</style>" in content:
    content = content.replace("</style>", portal_css + "\n    </style>")

# Create Cover Portal Page HTML
cover_portal_html = """
    <!-- ========================================================================= -->
    <!-- COVER PAGE HUB / PORTAL VIEW (DEFAULT LOAD VIEW)                         -->
    <!-- ========================================================================= -->
    <div id="cover-portal-view" class="portal-module-view active">
        <div class="cover-hero">
            <h1>Contiki-NG Cooja WSN Research Portal</h1>
            <p>Welcome to the Multi-Module Wireless Sensor Network Research Hub. Select a research module card below to launch protocol analytics, simulation diagnostics, or graph theoretical invariants across 16 network scales (29 to 10,000 Motes).</p>
            <div class="cover-badges">
                <div class="cover-badge">🚀 Active Modules: <span>1 Live Suite</span></div>
                <div class="cover-badge">📊 Network Scales: <span>16 Densities (29 – 10,000 Motes)</span></div>
                <div class="cover-badge">🏆 Winner Layout: <span>Lucas Golden Ratio (φ = 1.618)</span></div>
            </div>
        </div>

        <div class="modules-section-title">
            <span>🧩</span> Research Modules & Simulation Frameworks
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
                    <span>Launch Contiki-NG RPL-UDP Dashboard</span>
                    <span>→</span>
                </button>
            </div>

            <!-- Card Module 2 Placeholder: Add New Module -->
            <div class="module-card module-card-add" onclick="alert('Ready to integrate another module! You can add new simulation framework cards here.')">
                <div style="padding: 20px 0;">
                    <div style="font-size: 50px; color: var(--accent-green); margin-bottom: 12px;">➕</div>
                    <div style="font-size: 18px; font-weight: 800; color: var(--text-primary); margin-bottom: 8px;">Add Another Module</div>
                    <div style="font-size: 13px; color: var(--text-secondary); max-width: 280px; margin: 0 auto 16px;">
                        Expand portal with new simulation tools, TSCH scheduling, AI routing, or 6TiSCH protocol suites.
                    </div>
                    <span style="font-size: 12px; font-weight: 700; color: var(--accent-green); text-transform: uppercase; letter-spacing: 1px;">+ Expand Hub</span>
                </div>
            </div>
        </div>
    </div>
"""

body_start = content.find("<body>") + len("<body>")
body_end = content.rfind("</body>")

existing_body = content[body_start:body_end]

# Check if already wrapped
if '<div id="module-rpl-udp"' not in existing_body:
    # Wrap existing body into Module RPL-UDP with a Back Button Bar
    module_rpl_udp_html = f"""
    <!-- ========================================================================= -->
    <!-- MODULE 1: CONTIKI-NG COOJA SIMULATION USING RPL-UDP                       -->
    <!-- ========================================================================= -->
    <div id="module-rpl-udp" class="portal-module-view">
        <div class="portal-back-bar">
            <button class="back-portal-btn" onclick="openModule('cover-portal-view')">
                <span>🏠</span>
                <span>Back to Research Portal Cover Page</span>
            </button>
            <div style="font-weight: 800; font-size: 15px; color: var(--accent-purple);">
                📡 Module 1: Contiki-NG Cooja Simulation using RPL-UDP
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); font-weight: 600;">
                16 Scales (29 to 10,000 Motes)
            </div>
        </div>
        {existing_body}
    </div>
    """
    new_body_content = "<body>\n" + cover_portal_html + module_rpl_udp_html
else:
    new_body_content = "<body>\n" + existing_body

portal_js = """
    <script>
        function openModule(moduleId) {
            var modules = document.getElementsByClassName('portal-module-view');
            for (var i = 0; i < modules.length; i++) {
                modules[i].classList.remove('active');
            }
            var target = document.getElementById(moduleId);
            if (target) {
                target.classList.add('active');
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }
    </script>
"""

if "function openModule(" not in content:
    new_body_content += portal_js

new_full_html = content[:content.find("<body>")] + new_body_content + "\n</body>\n</html>"

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(new_full_html)

print("[+] SUCCESS: Modular Cover Page & Card Hub updated in dashboard.html!")
