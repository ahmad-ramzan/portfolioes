import re

def clean_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replaces
    replacements = {
        "2nd Day — Product Shots": "Product Shot Designs",
        "5th Day — Influencer UGC": "Influencer UGC Ads",
        "6th Day — Influencer Images": "Influencer Style Concepts",
        "8th Day — Influencer Images": "Lifestyle & Social UGC",
        "9th Day — UGC Images": "Fashion & Outfit Prompts",
        "10th Day — AI UGC Actors": "AI UGC Actors & Characters",
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    # Remove any remaining "Xth Day — ..." sub-groups if any
    content = re.sub(r"\s*\{\s*sub:\s*'[^']*Day[^']*'.*?\}\s*,\s*", "", content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

clean_html('other-projects.html')
print("Successfully cleaned up category names!")
