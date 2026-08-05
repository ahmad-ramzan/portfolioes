import re

with open(r'c:\Users\Ch Asad Waqas Kamboh\portfolioes\other-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any titles like "8th Influencer Image 1" -> "Influencer Image 1", "9th UGC Image 1" -> "UGC Image 1"
html = re.sub(r"t:\s*'8th Influencer (Image|Video) (\d+)'", r"t: 'Influencer \1 \2'", html)
html = re.sub(r"t:\s*'9th UGC Image (\d+)'", r"t: 'Fashion UGC Image \1'", html)

# Fix double brackets syntax like },]
html = re.sub(r"\}\s*,\s*\]\s*\}\s*,\s*\]\s*\}\s*,\s*\]", "}\n                        ]\n                    }", html)
html = re.sub(r"\}\s*,\s*\]\s*\}\s*,\s*\]", "}\n                        ]\n                    }", html)
html = re.sub(r"\}\s*,\s*\]", "}", html)

with open(r'c:\Users\Ch Asad Waqas Kamboh\portfolioes\other-projects.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished fixing titles and syntax!")
