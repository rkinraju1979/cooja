import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read(50000)

classes = set(re.findall(r'class="([^"]+)"', text))
print("FOUND CLASSES:", sorted(list(classes)))
