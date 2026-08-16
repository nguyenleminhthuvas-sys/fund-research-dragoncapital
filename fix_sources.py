import csv
import os

source_registry = '_data/SOURCE_REGISTRY.csv'
task_registry = '_data/task_registry.csv'
usecase_registry = '_data/usecase_registry.csv'

# We already appended to SOURCE_REGISTRY in the failed run (partially)? Let's check.
# Wait, the crash was AFTER appending to SOURCE_REGISTRY. So it might have already appended!
# Let's read existing source IDs to prevent duplicate append.
existing_sources = set()
with open(source_registry, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            existing_sources.add(row[0].strip())

new_sources = [
    ['S-ENF-006', 'T1', 'Báo chí xử phạt', 'Thời báo Tài chính Việt Nam xử phạt Amber/Thành Công', 'Thời báo Tài chính VN', 'https://thoibaotaichinhvietnam.vn/quan-ly-quy-amber-bi-xu-phat-hon-400-trieu-dong-do-co-nhieu-vi-pham-trong-linh-vuc-chung-khoan-187796.html', '2025-11-01', '2026-08-16', 'vi', '5', 'Xử phạt Amber và Thành Công', 'File: thoibaotaichinhvietnam-xu-phat.md', 'ĐANG DÙNG'],
    ['S-ENF-007', 'T1', 'Quyết định xử phạt UBCKNN', 'Kết luận thanh tra tại Công ty Cổ phần Quản lý quỹ đầu tư MB', 'Thanh tra Chính phủ', 'https://thanhtra.com.vn/ket-luan-thanh-tra-E17BD7A25/ket-luan-thanh-tra-tai-cong-ty-co-phan-quan-ly-quy-dau-tu-mb-44d731b81.html', '2025-01-22', '2026-08-16', 'vi', '5', 'Kết luận thanh tra MB Capital', 'File: thanhtra-mb-capital-xu-phat-120kl.md', 'ĐANG DÙNG'],
    ['S-REG-003', 'T1', 'Văn bản pháp luật', 'Thông tư 99/2020/TT-BTC hướng dẫn hoạt động của công ty quản lý quỹ đầu tư chứng khoán', 'Bộ Tài chính', 'https://thuvienphapluat.vn/van-ban/Doanh-nghiep/Thong-tu-99-2020-TT-BTC-huong-dan-hoat-dong-cua-cong-ty-quan-ly-quy-dau-tu-chung-khoan-461198.aspx', '2020-11-16', '2026-08-16', 'vi', '5', 'Quy định rủi ro TT99', 'File: thuvienphapluat-TT99-2020.md', 'ĐANG DÙNG']
]

sources_to_add = [row for row in new_sources if row[0] not in existing_sources]

if sources_to_add:
    with open(source_registry, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in sources_to_add:
            writer.writerow(row)

# 2. Update task_registry and usecase_registry
mapping = {
    'S-DOC-BVFED': 'S-BVFED-001',
    'S-REG-TT98': 'S-TT98-001',
    'S-ENF-AMBER': 'S-ENF-006',
    'S-ENF-TCTC': 'S-ENF-006',
    'S-REG-TT99': 'S-REG-003',
    'S-ENF-120KL': 'S-ENF-007'
}

def update_csv(filepath, id_col):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    
    if id_col in header:
        source_idx = header.index(id_col)
    else:
        print(f"Error: {id_col} not found in {filepath}")
        return

    for row in rows:
        if len(row) > source_idx:
            cell = row[source_idx]
            if cell:
                # ids can be separated by comma or semicolon
                ids = cell.replace(';', ',').split(',')
                new_ids = []
                for id in ids:
                    id = id.strip()
                    if id in mapping:
                        new_ids.append(mapping[id])
                    else:
                        new_ids.append(id)
                # deduplicate while preserving order
                seen = set()
                dedup = []
                for item in new_ids:
                    if item and item not in seen:
                        seen.add(item)
                        dedup.append(item)
                row[source_idx] = ','.join(dedup)
                
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

update_csv(task_registry, 'source_ids')
update_csv(usecase_registry, 'source_ids')

print("DONE UPDATE")
