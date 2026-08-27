import re

filepath = r'C:\Users\Ch Asad Waqas Kamboh\.gemini\antigravity-ide\brain\d9010bba-af13-43e3-b24b-2b9d1ae7a9f7\.system_generated\steps\71\content.md'

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

folder_id = '1znPTgkXnM1kMygBVZjalHYTue-VF-sha'
all_ids = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html)) - {folder_id}

print(f"Found {len(all_ids)} IDs")

for fid in all_ids:
    print(fid)
