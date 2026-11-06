import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

cover_start = text.find('id="cover-portal-view"')
cover_end = text.find('id="module-rpl-udp"')

print("Cover Portal Segment (first 1000 chars):")
print(text[cover_start:cover_start+1000])

print("\n--------------------\n")
print("Cover Portal Grid Segment:")
grid_start = text.find('<div class="modules-grid">')
grid_end = text.find('<div id="module-rpl-udp"')
print(text[grid_start:grid_end])
