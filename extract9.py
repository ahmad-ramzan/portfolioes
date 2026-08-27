with open('C:\\Users\\Ch Asad Waqas Kamboh\\.gemini\\antigravity-ide\\brain\\c665b29f-20c7-4568-be25-16dd9e3ba3e9\\.system_generated\\tasks\\task-20.log', 'r') as f:
    lines = f.read().splitlines()

res = ""
current_group = ""

for line in lines:
    if "1X3syFxnJ2FitPJcddmAS1_6IGiRWZA_g" in line:
        current_group = "Main Portfolio Video"
        res += "// Main Portfolio\n"
    elif "1aLZtGfyLAJUvC3lVVjyh2ij_OYui63D0" in line:
        current_group = "Cash Cow — Faceless YouTube Video"
        res += "\n// Cash Cow\n"
    elif "1IO9o0s8WRc2Tz_2Ug8i3shabaZwuBVNN" in line:
        current_group = "Short Reel"
        res += "\n// Short Reels\n"
    elif line and not line.startswith("URL:") and not line.startswith("Log:"):
        fid = line.strip()
        if len(fid) == 33:
            res += f"                            {{ t: '{current_group}', u: 'https://drive.google.com/file/d/{fid}/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id={fid}&sz=w640' }},\n"

with open('extract_out.txt', 'w') as f:
    f.write(res)
print("done")
