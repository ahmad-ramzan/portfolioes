import re

# Read the extracted items
with open('extract_out.txt', 'r') as f:
    text = f.read()

# Parse the text into lists
main_items = []
cash_cow_items = []
short_reels_items = []

current_list = None
for line in text.splitlines():
    line = line.strip()
    if line.startswith('// Main Portfolio'):
        current_list = main_items
    elif line.startswith('// Cash Cow'):
        current_list = cash_cow_items
    elif line.startswith('// Short Reels'):
        current_list = short_reels_items
    elif line.startswith('{'):
        current_list.append("                            " + line)

# Build the replacement string
replacement = """            {
                id: 'anim', label: 'Animation Studio', h: '2D & 3D Animation Studio',
                groups: [
                    {
                        sub: 'Main Portfolio', items: [
""" + "\n".join(main_items) + """
                        ]
                    },
                    {
                        sub: 'Cash Cow — Faceless YouTube', items: [
""" + "\n".join(cash_cow_items) + """
                        ]
                    },
                    {
                        sub: 'Short Reels Collection', items: [
""" + "\n".join(short_reels_items) + """
                        ]
                    },
                    {
                        sub: 'Pixel Anime Studio', items: [
                            { t: 'Pixel Anime Studio — YouTube', u: 'https://www.youtube.com/@pixelanimestudio', img: 'assets/thumbnails/thumbnail_anime.png' },
                            { t: 'Pixel Anime Studio — Instagram', u: 'https://www.instagram.com/pixelanimestudio/', img: 'assets/thumbnails/thumbnail_anime.png' }
                        ]
                    }
                ]
            },"""

with open('other-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = """            {
                id: 'anim', label: 'Animation Studio', h: '2D & 3D Animation Studio',
                groups: [
                    {
                        sub: null, items: [
                            { t: 'Main Portfolio', u: 'https://drive.google.com/drive/u/3/folders/1X3syFxnJ2FitPJcddmAS1_6IGiRWZA_g', img: 'assets/thumbnails/thumbnail_anime.png' },

                            { t: 'Cash Cow — Faceless YouTube', u: 'https://drive.google.com/drive/folders/1aLZtGfyLAJUvC3lVVjyh2ij_OYui63D0?usp=sharing', img: 'assets/thumbnails/thumbnail_anime.png' },
                            { t: 'Short Reels Collection', u: 'https://drive.google.com/drive/folders/1IO9o0s8WRc2Tz_2Ug8i3shabaZwuBVNN', img: 'assets/thumbnails/thumbnail_anime.png' },
                            { t: 'Pixel Anime Studio — YouTube', u: 'https://www.youtube.com/@pixelanimestudio', img: 'assets/thumbnails/thumbnail_anime.png' },
                            { t: 'Pixel Anime Studio — Instagram', u: 'https://www.instagram.com/pixelanimestudio/', img: 'assets/thumbnails/thumbnail_anime.png' }
                        ]
                    }
                ]
            },"""

if target in html:
    new_html = html.replace(target, replacement)
    with open('other-projects.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced successfully!")
else:
    print("Target block not found!")
