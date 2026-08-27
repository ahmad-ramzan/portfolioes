import re

filepath = r'drive_html.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

folder_id = '1uLNET2E70wdJ37H2bLWGGOBr_NeHuM9y'

all_ids = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html)) - {folder_id}

print(f"File IDs ({len(all_ids)}):")

paired = []
for fid in sorted(all_ids):
    for m in re.finditer(re.escape(fid), html):
        pos = m.start()
        ahead = html[pos:pos+1500]
        # Look for video file names
        name_match = re.search(r'([^\s"\'<>\\]+\.(?:mp4|mov|avi))', ahead, re.IGNORECASE)
        if name_match:
            paired.append((fid, name_match.group(1)))
            break

# If we couldn't find the name, just use the ID
if not paired:
    for fid in sorted(all_ids):
        paired.append((fid, f'Video {fid[:5]}'))

print(f"\nTotal paired: {len(paired)}")

print("\n// Real Estate items")
for fid, name in paired:
    clean = name.replace('.mp4','').replace('.mov','').replace('_',' ').strip()
    print(f"                            {{ t: '{clean}', u: 'https://drive.google.com/file/d/{fid}/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id={fid}&sz=w640' }},")
