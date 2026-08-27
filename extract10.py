import re

with open('extract_out.txt', 'r') as f:
    extracted_items = f.read()

# Make sure it ends correctly with comma for all items except maybe we can just let it have trailing commas inside the list
# Wait, let's just make it a string to replace
replacement_str = extracted_items + """
                            { t: 'Pixel Anime Studio — YouTube', u: 'https://www.youtube.com/@pixelanimestudio', img: 'assets/thumbnails/thumbnail_anime.png' },
                            { t: 'Pixel Anime Studio — Instagram', u: 'https://www.instagram.com/pixelanimestudio/', img: 'assets/thumbnails/thumbnail_anime.png' }"""

with open('other-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find the specific block to replace
target_block = """                            { t: 'Main Portfolio', u: 'https://drive.google.com/drive/u/3/folders/1X3syFxnJ2FitPJcddmAS1_6IGiRWZA_g', img: 'assets/thumbnails/thumbnail_anime.png' },

                            { t: 'Cash Cow — Faceless YouTube', u: 'https://drive.google.com/drive/folders/1aLZtGfyLAJUvC3lVVjyh2ij_OYui63D0?usp=sharing', img: 'assets/thumbnails/thumbnail_anime.png' },
                            { t: 'Short Reels Collection', u: 'https://drive.google.com/drive/folders/1IO9o0s8WRc2Tz_2Ug8i3shabaZwuBVNN', img: 'assets/thumbnails/thumbnail_anime.png' },
                            { t: 'Pixel Anime Studio — YouTube', u: 'https://www.youtube.com/@pixelanimestudio', img: 'assets/thumbnails/thumbnail_anime.png' },
                            { t: 'Pixel Anime Studio — Instagram', u: 'https://www.instagram.com/pixelanimestudio/', img: 'assets/thumbnails/thumbnail_anime.png' }"""

if target_block in html:
    new_html = html.replace(target_block, replacement_str)
    with open('other-projects.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced successfully!")
else:
    print("Target block not found!")
