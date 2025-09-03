import os
import re

python3_dir = '/home/user/apps/leetcode-solutions/python3'
readme_path = '/home/user/apps/leetcode-solutions/README.md'

def get_question_info(filename):
    # Example: 001-two-sum.py
    match = re.match(r'(\d+)-([a-z0-9\-]+)\.py', filename)
    if not match:
        return None
    num = match.group(1)
    slug = match.group(2)
    # Convert slug to title
    title = slug.replace('-', ' ').title()
    url = f'https://leetcode.com/problems/{slug}'
    return num, title, url

file_infos = []
for fname in os.listdir(python3_dir):
    if fname.endswith('.py'):
        info = get_question_info(fname)
        if info:
            num, title, url = info
            file_infos.append((int(num), fname, title, url))

file_infos.sort()  # Sort by integer question number

rows = [
    f'| [{num}. {title}]({url}) | [python3](python3/{fname}) |'
    for num, fname, title, url in file_infos
]

if rows:
    table = [
        '',
        '| Question | Solutions |',
        '| :------- | :-------- |',
    ] + rows

    with open(readme_path, 'a', encoding='utf-8') as f:
        f.write('\n'.join(table) + '\n')
