import re

def replace_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Audio & CAD & Figma
    content = content.replace("tile: 'audio'", "img: 'assets/thumbnails/audio_waveform_thumb.png'")
    content = content.replace("tile: 'cad'", "img: 'assets/thumbnails/cad_drawing_thumb.png'")
    
    # Specific targeted replaces for other things
    content = re.sub(r"t:\s*'[^']*3D[^']*'.*?tile:\s*'(video|drive)'", lambda m: m.group(0).replace(m.group(0)[-13:], "img: 'assets/thumbnails/3d_animation_thumb.png'"), content)
    
    # Just replace all remaining tile: 'video' and tile: 'drive' with generic placeholders
    content = content.replace("tile: 'video'", "img: 'assets/thumbnails/music_video_thumb.png'")
    content = content.replace("tile: 'drive'", "img: 'assets/thumbnails/thumbnail_learning.png'")
    
    # For index.html apps
    apps = ['TrakMD Website', 'TrakMD — Google Play', 'TrakMD — App Store', 'Fujitec eClaim', 'Mashraben Aab', 'Crypto App', 'Zenklub — Google Play', 'Zenklub — App Store']
    for app in apps:
        # regex to match the item and insert img if missing
        pattern = r"(t:\s*'" + app + r"',\s*u:\s*'[^']+')"
        content = re.sub(pattern + r"\s*}", r"\1, img: 'assets/thumbnails/app_mockup_thumb.png' }", content)

    # For missing youtube links
    yt_links = ['Veo — Company Shorts (YouTube)', 'Pixel Anime Studio — YouTube', 'Pixel Anime Studio — Instagram']
    for yt in yt_links:
        pattern = r"(t:\s*'" + re.escape(yt) + r"',\s*u:\s*'[^']+')"
        content = re.sub(pattern + r"\s*}", r"\1, img: 'assets/thumbnails/thumbnail_learning.png' }", content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

replace_in_file('other-projects.html')
replace_in_file('index.html')
print("Done!")
