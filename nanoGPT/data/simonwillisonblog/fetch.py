import httpx
import json
import re

fp = open("input.nl-json", "w")

tag_re = re.compile('<.*?>')

url = "https://datasette.simonwillison.net/simonwillisonblog/blog_entry.json?_col=title&_col=body&_shape=objects&_size=max"

while url:
    data = httpx.get(url).json()
    for item in data["rows"]:
        title = item["title"]
        body = tag_re.sub('', item["body"])
        fp.write(json.dumps([title, body]) + "\n")
    url = data["next_url"]