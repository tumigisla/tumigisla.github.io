#!/usr/bin/env python3
import sys
from datetime import datetime

def create_post(title):
    # Get today's date in ISO8601 format
    date_iso = datetime.now().strftime('%Y-%m-%d')

    # Create the filename
    title_slug = title.replace(' ', '-').lower()
    filename = f'_posts/{date_iso}-{title_slug}.md'

    # Define the contents of the post
    contents = f"""---
layout: post
title: "{title}"
date: {date_iso} 00:00:00 +0000
---"""

    # Create the _posts directory if it doesn't exist
    import os
    os.makedirs('_posts', exist_ok=True)

    # Write the contents to the file
    with open(filename, 'w') as file:
        file.write(contents)

    print(f'Post created: {filename}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: new_post.py 'Title of the post'")
        sys.exit(1)

    post_title = sys.argv[1]
    create_post(post_title)
