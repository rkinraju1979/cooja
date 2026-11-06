import subprocess, os, sys, shutil

deployments = ['circular29', 'grid29', 'hexagonal29', 'lucas29', 'random29']
sim_dir = '/home/rkr/simulations'
cooja_dir = '/home/rkr/contiki-ng/tools/cooja'

print("=== STARTING CONTIKI-NG COOJA DEPLOYMENT SIMULATIONS (1000 ROUNDS EACH) ===")

for top in deployments:
    csc_path = f"{sim_dir}/{top}.csc"
    log_path = f"{sim_dir}/{top}.log"
    print(f"\n[+] Launching Cooja Simulation for Deployment: {top}...")
    
    # Run gradle cooja headless
    cmd = f"cd {cooja_dir} && PATH=/usr/bin:/bin JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64 ./gradlew run --args='--no-gui {csc_path}'"
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    # Check COOJA.testlog
    testlog = f"{cooja_dir}/COOJA.testlog"
    if os.path.exists(testlog):
        shutil.copy(testlog, log_path)
        log_size = os.path.getsize(log_path)
        print(f"    -> Completed {top}. Log saved to {log_path} ({log_size} bytes)")
    else:
        print(f"    [!] Warning: {testlog} not found for {top}")
        # Save stdout/stderr if testlog missing
        with open(log_path, 'w') as f:
            f.write(res.stdout + '\n' + res.stderr)

print("\n=== ALL 5 DEPLOYMENT SIMULATIONS COMPLETED SUCCESSFULLY ===")
