import re

with open('drive_html.txt', 'r', encoding='utf-8') as f:
    html = f.read()

names = re.findall(r'"([^"]+?\.(?:mp4|mkv|avi))"', html)
names = list(set(names))

pairs = {}
for name in names:
    escaped_name = re.escape(name)
    pattern = r'"([a-zA-Z0-9_-]{33})".{0,1000}?"' + escaped_name + r'"'
    match = re.search(pattern, html)
    if match:
        pairs[name] = match.group(1)
    else:
        pattern2 = r'"' + escaped_name + r'".{0,1000}?"([a-zA-Z0-9_-]{33})"'
        match2 = re.search(pattern2, html)
        if match2:
            pairs[name] = match2.group(1)

for name, id_ in pairs.items():
    print(f'{name} -> {id_}')
print(f'Total paired: {len(pairs)}')
