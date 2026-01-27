import json

def audit_posts():
    try:
        with open('src/data/posts.json', 'r', encoding='utf-8') as f:
            posts = json.load(f)
        
        with open('audit_results.txt', 'w', encoding='utf-8') as out:
            out.write(f"Total posts: {len(posts)}\n")
            out.write("-" * 50 + "\n")
            out.write(f"{'ID':<5} | {'Active':<8} | {'Length':<8} | {'Title'}\n")
            out.write("-" * 50 + "\n")
            
            short_posts = []
            for p in posts:
                content = p.get('content', '')
                length = len(content)
                if length < 2000:
                    short_posts.append(p)
                    out.write(f"{p['id']:<5} | {str(p.get('active', False)):<8} | {length:<8} | {p['title']}\n")
            
            out.write("-" * 50 + "\n")
            out.write(f"Found {len(short_posts)} posts shorter than 2000 characters.\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    audit_posts()
