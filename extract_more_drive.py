import re

results = {}

folders = {
    'Ai viral health video': {
        'path': r'C:\Users\Ch Asad Waqas Kamboh\.gemini\antigravity-ide\brain\c15a5903-88af-4361-b0b1-c8975ea93146\.system_generated\steps\285\content.md',
        'folder_id': '1AZ-89a97TIQVmwTL6xXrNveVnYwGGhSR',
    },
    'Texas MCN': {
        'path': r'C:\Users\Ch Asad Waqas Kamboh\.gemini\antigravity-ide\brain\c15a5903-88af-4361-b0b1-c8975ea93146\.system_generated\steps\287\content.md',
        'folder_id': '11T3zNItMnrMdXIL3B81K66R7IJSjOWW6',
    },
    'UGC SPANISH VIDEO': {
        'path': r'C:\Users\Ch Asad Waqas Kamboh\.gemini\antigravity-ide\brain\c15a5903-88af-4361-b0b1-c8975ea93146\.system_generated\steps\288\content.md',
        'folder_id': '166vIgVSigyiuZRKAb8Cq0jqvxQgJwIpg',
    },
}

for folder_name, info in folders.items():
    print(f"\n{'='*60}")
    print(f"FOLDER: {folder_name}")
    print(f"{'='*60}")
    
    with open(info['path'], 'r', encoding='utf-8') as f:
        html = f.read()
    
    all_ids = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html)) - {info['folder_id']}
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
    
    results[folder_name] = paired

print("\n\n" + "="*60)
print("JS DATA ITEMS")
print("="*60)
for folder_name, pairs in results.items():
    print(f"\n// {folder_name} ({len(pairs)} files)")
    for fid, name in pairs:
        clean = name.replace('.mp4','').replace('.jpg','').replace('.png','').replace('_',' ').strip()
        print(f"            {{ t: '{clean}', u: 'https://drive.google.com/file/d/{fid}/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id={fid}&sz=w640' }},")
