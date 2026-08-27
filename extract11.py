import urllib.request
import re

url = "https://drive.google.com/drive/folders/1SqQj-Bb4Y16LS1TGl2rESKvvQHL-Huxm"
folder_id = "1SqQj-Bb4Y16LS1TGl2rESKvvQHL-Huxm"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    ids = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html)) - {folder_id}
    print(f"URL: {url} -> {len(ids)} items found")
    
    res = ""
    for fid in ids:
        res += f"                            {{ t: 'AI UGC Ads Video', u: 'https://drive.google.com/file/d/{fid}/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id={fid}&sz=w640' }},\n"
    
    # Now read other-projects.html and replace
    with open('other-projects.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    target = "                            { t: 'AI UGC Ads — Folder 2', u: 'https://drive.google.com/drive/folders/1SqQj-Bb4Y16LS1TGl2rESKvvQHL-Huxm', img: 'assets/thumbnails/thumbnail_product.png' },"
    
    # We want to replace the target with res, but we should strip the last comma if needed, or leave it. The original had a comma.
    # Our res has a newline and comma for each item. 
    res = res.rstrip(',\n') + ","
    
    if target in html_content:
        new_html = html_content.replace(target, res)
        with open('other-projects.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Replaced successfully!")
    else:
        print("Target block not found!")
        
except Exception as e:
    print(f"Error fetching {url}: {e}")
