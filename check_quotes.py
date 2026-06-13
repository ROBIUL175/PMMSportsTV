import re

content = open('index.html', encoding='utf-8').read()

# Let's find any text outside HTML tags and script/style blocks
# Remove scripts
content_no_script = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
# Remove styles
content_no_style = re.sub(r'<style.*?>.*?</style>', '', content_no_script, flags=re.DOTALL)
# Remove comments
content_no_comments = re.sub(r'<!--.*?-->', '', content_no_style, flags=re.DOTALL)

# Let's find all text between tag boundaries
text_runs = re.findall(r'>([^<]+)<', content_no_comments)
for text in text_runs:
    trimmed = text.strip()
    if trimmed and '"' in trimmed:
        print(f"Found double quote in text: {repr(trimmed)}")
