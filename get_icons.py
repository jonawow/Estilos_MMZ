import re
with open(r'C:\Users\Jonathan\.gemini\antigravity-ide\brain\42cd5a6d-8e93-4f39-a4b6-ea2345af7e7e\.system_generated\tasks\task-625.log', 'r', encoding='utf-8') as f:
    content = f.read()
urls = re.findall(r'-webkit-mask-image: url\("(data:image/svg\+xml.*?)"\)', content)
# We only want the unique ones
unique_urls = list(set(urls))
for i, url in enumerate(unique_urls):
    print(f"ICON {i+1}: {url[:100]}...")
    # write to a file so we can copy them later
    with open(f"icon_{i+1}.txt", "w", encoding="utf-8") as out:
        out.write(url)
