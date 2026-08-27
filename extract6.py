import re

file1 = r'C:\Users\Ch Asad Waqas Kamboh\.gemini\antigravity-ide\brain\d9010bba-af13-43e3-b24b-2b9d1ae7a9f7\.system_generated\steps\148\content.md'
file2 = r'C:\Users\Ch Asad Waqas Kamboh\.gemini\antigravity-ide\brain\d9010bba-af13-43e3-b24b-2b9d1ae7a9f7\.system_generated\steps\149\content.md'

with open(file1, 'r', encoding='utf-8') as f:
    html1 = f.read()

with open(file2, 'r', encoding='utf-8') as f:
    html2 = f.read()

folder1 = '17F75eILF0_ZRiunf41Ucf3xUYsZ97vu6'
folder2 = '1Zj10QnnhTcmAUZsGYUkmQKQM_9Mfsvjk'

ids1 = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html1)) - {folder1}
ids2 = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html2)) - {folder2}

print(f"// Spokesperson Full Folder ({len(ids1)} items)")
for fid in ids1:
    print(f"                            {{ t: 'Spokesperson Full Folder Video', u: 'https://drive.google.com/file/d/{fid}/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id={fid}&sz=w640' }},")

print(f"\n// AI UGC Ads - Folder 1 ({len(ids2)} items)")
for fid in ids2:
    print(f"                            {{ t: 'AI UGC Ads Video', u: 'https://drive.google.com/file/d/{fid}/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id={fid}&sz=w640' }},")

