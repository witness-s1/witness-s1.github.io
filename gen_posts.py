import html2text
import feedparser
import argparse
import re
import os

def gen_posts():
    parser = argparse.ArgumentParser()
    parser.add_argument("feed_id", type=int)
    args = parser.parse_args()

    url = f"https://caraba1st.com/tid-{args.feed_id}.xml"
    feed = feedparser.parse(url)
    for entry in feed["entries"]:
        entry_title = entry["title"] + ".markdown"
        filename = re.sub(r'[\/:"*?<>|]+', '', entry_title)
        with open(os.path.join("_posts", filename), "w") as out:
            out.write(html2text.html2text(entry["content"][0]["value"]))

if __name__ == "__main__":
    gen_posts()
