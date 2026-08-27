import urllib.request
import re

url1 = "https://drive.google.com/drive/u/3/folders/1X3syFxnJ2FitPJcddmAS1_6IGiRWZA_g"
url2 = "https://drive.google.com/drive/folders/1aLZtGfyLAJUvC3lVVjyh2ij_OYui63D0"
url3 = "https://drive.google.com/drive/folders/1IO9o0s8WRc2Tz_2Ug8i3shabaZwuBVNN"

def get_ids(url, folder_id):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        ids = set(re.findall(r'"([a-zA-Z0-9_-]{33})"', html)) - {folder_id}
        print(f"URL: {url} -> {len(ids)} items found")
        for fid in ids:
            print(fid)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

get_ids(url1, "1X3syFxnJ2FitPJcddmAS1_6IGiRWZA_g")
get_ids(url2, "1aLZtGfyLAJUvC3lVVjyh2ij_OYui63D0")
get_ids(url3, "1IO9o0s8WRc2Tz_2Ug8i3shabaZwuBVNN")
