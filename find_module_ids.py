import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

mod_ids = re.findall(r'id="(module-[^"]+)"', text)
print("All module IDs found in dashboard.html:")
for m in set(mod_ids):
    print(" -", m)
