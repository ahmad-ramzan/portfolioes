import re

filepath = r'C:\Users\Ch Asad Waqas Kamboh\.gemini\antigravity-ide\brain\c15a5903-88af-4361-b0b1-c8975ea93146\.system_generated\steps\261\content.md'

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

folder_id = '1BsC30EsCUPKhvN2Q6MHKhItVYBPPa-Np'

all_ids = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html)) - {folder_id}
known_parents = {'1r0rJez9wJbpRhFf5Z3EFYFxRJWowV3Ux', '18H72DWJseCfeZq651FRrrDgDEc3AjYhu'}
all_ids -= known_parents

print(f"File IDs ({len(all_ids)}):")

paired = []
for fid in sorted(all_ids):
    for m in re.finditer(re.escape(fid), html):
        pos = m.start()
        ahead = html[pos:pos+800]
        name_match = re.search(r'([^"\'<>\s]+\.(?:jpg|png|jpeg|mp4))', ahead, re.IGNORECASE)
        if name_match:
            paired.append((fid, name_match.group(1)))
            print(f"  {fid} -> {name_match.group(1)}")
            break

print(f"\nTotal paired: {len(paired)}")

# Output JS items
print("\n// 20 Animations items")
for fid, name in paired:
    clean = name.replace('.mp4','').replace('.jpg','').replace('.png','').replace('_',' ').strip()
    print(f"                            {{ t: '{clean}', u: 'https://drive.google.com/file/d/{fid}/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id={fid}&sz=w640' }},")
