#!/usr/bin/env python3
import json
import os
from pathlib import Path

# 讀取翻譯映射
with open('knowledge/_translations.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

# 獲取所有已翻譯的中文文件
translated_zh = set(translations.values())

# 掃描所有中文文件
all_zh_files = []
categories = ['Art', 'Culture', 'Technology', 'Economy', 'Nature', 'Society', 'Geography', 'Music', 'Food', 'Lifestyle', 'People', 'About']

for category in categories:
    category_path = Path(f'knowledge/{category}')
    if category_path.exists():
        for file in category_path.glob('*.md'):
            if not file.name.startswith('_') and 'ROADMAP' not in file.name:
                relative_path = f'{category}/{file.name}'
                all_zh_files.append(relative_path)

# 找出未翻譯的文件
untranslated = []
for file in all_zh_files:
    if file not in translated_zh:
        untranslated.append(file)

# 按分類優先序排序
priority_order = ['Art', 'Culture', 'Technology', 'Economy', 'Nature', 'Society', 'Geography', 'Music', 'Food', 'Lifestyle', 'People', 'About']

untranslated_by_category = {}
for category in priority_order:
    category_files = [f for f in untranslated if f.startswith(f'{category}/')]
    if category_files:
        untranslated_by_category[category] = sorted(category_files)

print(f"總共 {len(untranslated)} 篇文章尚未翻譯")
for category, files in untranslated_by_category.items():
    print(f"\n{category} ({len(files)} 篇):")
    for file in files:
        print(f"  - {file}")