import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

print(f"[+] Total file size of dashboard.html: {len(text) / (1024*1024):.2f} MB")

modules = re.findall(r'id="(module-[^"]+|cover-portal-view)"', text)
print("[+] Found views/modules:", modules)

cards = re.findall(r'<div class="module-card-title">([^<]+)</div>', text)
print("[+] Found Module Card Titles on Cover Portal:")
for i, title in enumerate(cards, 1):
    print(f"    {i}. {title}")

if len(modules) >= 4 and len(cards) == 3:
    print("\n[✔] VERIFIED: Cover page contains 3 Card-Type Modules and all 3 module views are wired!")
else:
    print("\n[!] WARNING: Module count or card count mismatch.")
