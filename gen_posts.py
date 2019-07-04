import html2text
import feedparser
import argparse
import re
import os
from datetime import datetime, timedelta

def gen_posts():
    parser = argparse.ArgumentParser()
    parser.add_argument("feed_id", type=int)
    args = parser.parse_args()

    url = f"https://caraba1st.com/tid-{args.feed_id}.xml"
    feed = feedparser.parse(url)
    time_now = datetime.now()
    for idx, entry in enumerate(feed["entries"]):
        # Filter invalid characters.
        title = re.sub(r'[\/:"*?<>|]+', '', entry["title"]) 
        # Jeyll force all posts should have time at beginning.
        filename = time_now.strftime(f"%Y-%m-%d-{title}.md")
        # Shift blog post time to order them correctly.
        delta = timedelta(minutes=idx)
        with open(os.path.join("_posts", filename), "w") as out:
            header = f"""
---
layout: post
title: "{entry["title"]}"
date: {time_now - delta}
---

""".lstrip()
            out.write(header)
            out.write(html2text.html2text(entry["content"][0]["value"]))

if __name__ == "__main__":
    gen_posts()
