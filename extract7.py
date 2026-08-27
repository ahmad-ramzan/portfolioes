import re

file1 = r'C:\Users\Ch Asad Waqas Kamboh\.gemini\antigravity-ide\brain\d9010bba-af13-43e3-b24b-2b9d1ae7a9f7\.system_generated\steps\171\content.md'
file2 = r'C:\Users\Ch Asad Waqas Kamboh\.gemini\antigravity-ide\brain\d9010bba-af13-43e3-b24b-2b9d1ae7a9f7\.system_generated\steps\172\content.md'
file3 = r'C:\Users\Ch Asad Waqas Kamboh\.gemini\antigravity-ide\brain\d9010bba-af13-43e3-b24b-2b9d1ae7a9f7\.system_generated\steps\173\content.md'

with open(file1, 'r', encoding='utf-8') as f:
    html1 = f.read()

with open(file2, 'r', encoding='utf-8') as f:
    html2 = f.read()

with open(file3, 'r', encoding='utf-8') as f:
    html3 = f.read()

folder1 = '1ibgij3X43xBq5E6VbpAp_Axaie7Qubtt'
folder2 = '1TAxBtbHsB0_HWJMPvu_TStTcLeGdpRu0'
folder3 = '1vgQOy9iAvpRYqTuWti7T9VnL6Ih1n5yK'

ids1 = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html1)) - {folder1}
ids2 = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html2)) - {folder2}
ids3 = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html3)) - {folder3}

print(f"// AI Main UGC Videos ({len(ids1)} items)")
for fid in ids1:
    print(f"                            {{ t: 'AI Main UGC Video', u: 'https://drive.google.com/file/d/{fid}/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id={fid}&sz=w640' }},")

print(f"\n// AI Short Character Reels ({len(ids2)} items)")
for fid in ids2:
    print(f"                            {{ t: 'AI Short Character Reel', u: 'https://drive.google.com/file/d/{fid}/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id={fid}&sz=w640' }},")

print(f"\n// SaaS Product Videos ({len(ids3)} items)")
for fid in ids3:
    print(f"                            {{ t: 'SaaS Product Video', u: 'https://drive.google.com/file/d/{fid}/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id={fid}&sz=w640' }},")
