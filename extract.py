import re
import json

try:
    with open('drive_html.txt', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the JSON script block containing the initial data
    # Often it looks like window._DRIVE_initial_data = {...}
    match = re.search(r'window\._DRIVE_initial_data\s*=\s*(.*?);</script>', html, re.DOTALL)
    if not match:
        # try another pattern
        match = re.search(r'AF_initDataCallback\(\{key: \'ds:0\', isError:  false , hash: \'2\', data:(.*?)\}\);', html, re.DOTALL)
        
    print("MP4 files found directly:")
    mp4s = set(re.findall(r'\"([^\"]+?\.mp4)\"', html))
    print(mp4s)
    
    print("All file names found directly:")
    # look for things that look like titles
    titles = set(re.findall(r'\[\"([^\"]+?\.(?:mp4|mkv|avi|mov|wmv))\"', html, re.IGNORECASE))
    print(titles)

except Exception as e:
    print(f"Error: {e}")
