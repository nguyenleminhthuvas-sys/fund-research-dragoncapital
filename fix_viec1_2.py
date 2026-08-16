import csv
import os

# 1. Load tasks and remove T-BO-058 -> 067
tasks = []
with open('_data/task_registry.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        if row[0] not in [f'T-BO-0{i}' for i in range(58, 68)]:
            # Fix column 17 (rang_buoc_phap_ly)
            if 'UC-' in row[17] or 'REJECTED' in row[17]:
                row[17] = "" # Clear it
            tasks.append(row)

with open('_data/task_registry.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(tasks)

# 2. Remove UC-031, UC-032, UC-033 from usecase_registry
ucs = []
with open('_data/usecase_registry.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    uc_header = next(r)
    for row in r:
        if row[0] not in ['UC-031', 'UC-032', 'UC-033']:
            ucs.append(row)

with open('_data/usecase_registry.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(uc_header)
    w.writerows(ucs)

# 3. Remove S-REG-QD428 from SOURCE_REGISTRY.csv
sources = []
with open('_data/SOURCE_REGISTRY.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    src_header = next(r)
    for row in r:
        if row[0] != 'S-REG-QD428':
            sources.append(row)

with open('_data/SOURCE_REGISTRY.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(src_header)
    w.writerows(sources)

# 4. Move QD428 files
os.makedirs('01_lexicon/agent_notes', exist_ok=True)
if os.path.exists('_raw/legal/thuvienphapluat-QD428-2013.md'):
    os.rename('_raw/legal/thuvienphapluat-QD428-2013.md', '01_lexicon/agent_notes/thuvienphapluat-QD428-2013.md')
if os.path.exists('_raw/legal/thuvienphapluat-QD428-2013_clean.txt'):
    os.rename('_raw/legal/thuvienphapluat-QD428-2013_clean.txt', '01_lexicon/agent_notes/thuvienphapluat-QD428-2013_clean.txt')

# 5. Write CHANGELOG
with open('CHANGELOG.md', 'a', encoding='utf-8') as f:
    f.write("\n## [YYYY-MM-DD]\n")
    f.write("- Xóa 10 tác vụ (T-BO-058 -> T-BO-067) bịa từ QĐ 428 vì file raw bị lỗi 410, không có dữ liệu thực.\n")
    f.write("- Xóa UC-031, UC-032, UC-033 tương ứng.\n")
    f.write("- Xóa S-REG-QD428 khỏi SOURCE_REGISTRY.\n")
    f.write("- Sửa lại cột rang_buoc_phap_ly: xóa các giá trị UC- và REJECTED ghi nhầm cột.\n")
    f.write("- Chuyển các file _raw/legal/thuvienphapluat-QD428-2013 lỗi sang 01_lexicon/agent_notes/.\n")
