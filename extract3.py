import re
import json

def extract_files():
    with open('drive_html.txt', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the big AF_initDataCallback that contains the file list.
    # Usually it's the one with the most data.
    matches = re.findall(r'AF_initDataCallback\(\{key: \'(ds:\d+)\',.*?data:(\[.*?\])\}\);', html, re.DOTALL)
    
    files = []
    
    def search_tree(obj):
        if isinstance(obj, list):
            # Drive file items often have their ID at index 0 or somewhere
            # We look for a list that contains both an ID (len 33) and an mp4 filename
            # Actually, the file name might be deeply nested.
            # Let's collect all strings in this list tree.
            strings = []
            def get_strings(o):
                if isinstance(o, str): strings.append(o)
                elif isinstance(o, list):
                    for item in o: get_strings(item)
            get_strings(obj)
            
            # Check if this node seems to represent a file
            has_mp4 = any(s.endswith('.mp4') or s.endswith('.mkv') or s.endswith('.avi') for s in strings)
            # Find a potential ID
            potential_ids = [s for s in strings if re.match(r'^[a-zA-Z0-9_-]{33}$', s)]
            
            if has_mp4 and potential_ids:
                filename = next(s for s in strings if s.endswith('.mp4') or s.endswith('.mkv') or s.endswith('.avi'))
                files.append((potential_ids[0], filename))
                
            for item in obj:
                search_tree(item)

    for key, data_str in matches:
        try:
            # The data string might not be strict JSON (might have undefined, etc)
            # We can try to clean it up or just regex search
            pass
        except Exception:
            pass
            
    # Simpler regex approach: find all occurrences of 33-char ID followed eventually by .mp4 name
    # within the same JSON array scope.
    # Since it's hard, let's just use regex to find all strings that look like IDs
    ids = re.findall(r'\"([a-zA-Z0-9_-]{33})\"', html)
    names = re.findall(r'\"([^\"]+?\.(?:mp4|mkv|avi))\"', html)
    
    print("Found IDs:", len(set(ids)))
    print("Found Names:", len(set(names)))
    
    # We can't easily pair them.
    
extract_files()
