import re

with open('drive_html.txt', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern usually looks like ["FILE_ID", "filename.mp4", ... ]
# Let's search for the ID right before the filename
matches = re.findall(r'\[\"([a-zA-Z0-9_-]{28,35})\",\"([^\"]+?\.mp4)\"', html)
unique_files = {filename: fid for fid, filename in matches}

for filename, fid in unique_files.items():
    print(f"File: {filename}, Link: https://drive.google.com/file/d/{fid}/view")
    
# Check if thumbnail links are also nearby
# Let's just print out a few raw matches around the filename to inspect
# if no matches, try a different regex
if not matches:
    print("No matches for [ID, filename] pattern.")
    # let's try just finding the 33-char ids near the mp4 names
    mp4_matches = re.finditer(r'\"([^\"]+?\.mp4)\"', html)
    for m in list(mp4_matches)[:2]:
        start = max(0, m.start() - 200)
        end = min(len(html), m.end() + 200)
        print("CONTEXT around", m.group(1))
        print(html[start:end])
        print("-" * 40)
