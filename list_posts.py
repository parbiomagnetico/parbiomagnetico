import json

with open('src/data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

for p in posts:
    print(f"{p['id']}: {p['active']} - {p['title']}")
