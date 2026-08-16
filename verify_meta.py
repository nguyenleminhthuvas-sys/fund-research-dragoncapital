import re
import json

with open('12_report/FINAL_REPORT.html', 'r', encoding='utf-8') as f:
    html = f.read()

meta_match = re.search(r'const META = (\{.*?\});', html, re.DOTALL)
if meta_match:
    meta = json.loads(meta_match.group(1))
    
    roadmap = meta.get('roadmap', [])
    waves = {item['wave'] for item in roadmap if 'wave' in item}
    deps = sum(len(item.get('dependencies', [])) for item in roadmap)
    print(f"Roadmap: {len(waves)} waves, {deps} dependencies")
    
    arch = meta.get('architecture', [])
    print(f"Architecture: {len(arch)} capabilities")
else:
    print("META not found")
