import os
from bs4 import BeautifulSoup
import re

files_to_check = [
    "_raw/jd/ambercapital-ho-tro-van-hanh.html",
    "_raw/jd/hdcap-van-hanh.html",
    "_raw/jd/tvsc-nhan-vien-moi-gioi.html",
    "_raw/enforcement/tinnhanhchungkhoan-canh-cao.html",
    "_raw/enforcement/vsd-cac-hinh-thuc-xu-ly-vi-pham.html"
]

base_dir = "/Users/mac/Documents/Skill - Chị Chi Share/fund-research-dragoncapital"

results = []

for rel_path in files_to_check:
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        results.append({"file": rel_path, "status": "Not found"})
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # 1. Extract URL
    url = None
    canonical = soup.find("link", rel="canonical")
    if canonical and canonical.get("href"):
        url = canonical.get("href")
    
    if not url:
        og_url = soup.find("meta", property="og:url")
        if og_url and og_url.get("content"):
            url = og_url.get("content")
            
    if not url:
        base = soup.find("base")
        if base and base.get("href"):
            url = base.get("href")
            
    title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
            
    # 2. Extract Text and Count Characters
    text = soup.get_text(separator=" ", strip=True)
    char_count = len(text)
    
    text_lower = text.lower()
    
    # 3. Keyword Check
    is_jd = "jd/" in rel_path
    if is_jd:
        keywords = ["mô tả công việc", "trách nhiệm", "yêu cầu", "kinh nghiệm"]
    else:
        keywords = ["xử phạt", "vi phạm", "triệu đồng", "quyết định"]
        
    keyword_matches = sum([1 for kw in keywords if kw in text_lower])
    has_most_keywords = keyword_matches >= 2 # at least half? Let's report the matched count
    
    # Condition: > 3000 chars AND has most keywords
    has_real_content = char_count >= 3000 and has_most_keywords
    
    results.append({
        "file": os.path.basename(rel_path),
        "url": url,
        "title": title,
        "char_count": char_count,
        "matched_keywords": f"{keyword_matches}/{len(keywords)}",
        "has_real_content": has_real_content,
        "rel_path": rel_path
    })

for res in results:
    print(f"File: {res.get('file')}")
    print(f"URL: {res.get('url')}")
    print(f"Title: {res.get('title')}")
    print(f"Char Count: {res.get('char_count')}")
    print(f"Keywords: {res.get('matched_keywords')}")
    print(f"Has Content: {res.get('has_real_content')}")
    print("-" * 40)
