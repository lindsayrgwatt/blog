import os
import re

# Path to your Pelican content directory containing the Markdown files
content_path = '/Users/lindsayrgwatt/Documents/lindsayrgwatt/blog/content'

wp_image_pattern = r'wp-image-\d+'
wp_block_pattern = r'wp-block-[\w-]+'
wp_embed_pattern = r'<!--\s*wp:[^>]*?-->'

old_youtube_pattern = re.compile(
    r'<object.*?src="http://www\.youtube\.com/v/([a-zA-Z0-9_-]+).*?".*?</object>',
    re.DOTALL
)

def fix_image_urls(content):
    content = content.replace("http://lindsayrgwatt.com/blog/wp-content/uploads", "{static}/images")
    content = content.replace("https://lindsayrgwatt.com/blog/wp-content/uploads", "{static}/images")
    return content

def remove_wp_tags(content):
    content = re.sub(wp_image_pattern, '', content)
    content = re.sub(wp_block_pattern, '', content)
    content = re.sub(wp_embed_pattern, '', content)
    
    content = content.replace("<!-- wp:paragraph -->", "")
    content = content.replace("<!-- /wp:paragraph -->", "")
    content = content.replace("<!-- /wp:image -->", "")
    content = content.replace("<!-- /wp:column -->", "")
    content = content.replace("<!-- /wp:list -->","")
    content = content.replace("<!-- /wp:gallery -->","")
    content = content.replace("<!-- /wp:list-item -->","")
    content = content.replace("<!-- /wp:heading -->","")
    content = content.replace("<!-- /wp:embed -->","")
    content = content.replace("<!-- /wp:columns -->","")
    content = content.replace("<!-- /wp:separator -->","")
    content = content.replace('<!-- wp:list {"ordered":true} -->',"")
    
    return content

def fix_dollar_sign(content):
    content = content.replace('\$', '$')
    
    return content

def update_youtube_links(content):
    # Won't fix them all. Still need to manually fix some
    content = content.replace("http://www.youtube.com","https://www.youtube.com")    

    updated_content = old_youtube_pattern.sub(r'<iframe width="480" height="385" src="https://www.youtube.com/embed/\1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', content)
    
    return content

def fix_article(filepath):
    print(f"Processing {filepath}")
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Apply the fixes
    content = fix_image_urls(content)
    content = remove_wp_tags(content)
    content = update_youtube_links(content)
    content = fix_dollar_sign(content)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

# Iterate through all markdown files in the content directory
for root, dirs, files in os.walk(content_path):
    for file in files:
        if file.endswith('.md'):
            fix_article(os.path.join(root, file))