import csv
import re

with open('_raw/legal/quyet-dinh-428-qd-ubck.txt', 'r') as f:
    lines = f.readlines()

tasks = []
task_id_counter = 58

def add_task(dieu, name, desc, raw_ref_line, chi_tiet):
    global task_id_counter
    tasks.append([
        f'T-BO-{task_id_counter:03d}', 'Back Office', 'Performance & Risk Management', 'Quản trị rủi ro',
        name, desc, '', '', '', '', 'Quản trị rủi ro', '', 'Định kỳ', '', '', '', '',
        f'Quyết định 428/QĐ-UBCK, Điều {dieu}', 'REG', 'S-REG-QD428', chi_tiet, 'Y',
        f'_raw/legal/quyet-dinh-428-qd-ubck.txt#L{raw_ref_line}'
    ])
    task_id_counter += 1

current_dieu = None
for i, line in enumerate(lines):
    text = line.strip()
    match = re.match(r'^Điều\s+(\d+)\.', text)
    if match:
        current_dieu = match.group(1)
    
    if current_dieu == '4' and 'xây dựng cơ cấu tổ chức về quản trị rủi ro riêng biệt' in text.lower():
        add_task('4', 'Xây dựng cơ cấu tổ chức quản trị rủi ro', 'Công ty thiết lập hệ thống quản trị rủi ro, xây dựng cơ cấu tổ chức riêng biệt', i+1, 'xây dựng cơ cấu tổ chức về quản trị rủi ro riêng biệt')
        current_dieu = None # Prevent duplicates
    elif current_dieu == '6' and 'dự thảo chiến lược và chính sách quản trị rủi ro' in text.lower():
        add_task('6', 'Dự thảo chiến lược và chính sách', 'Ban điều hành dự thảo chiến lược và chính sách trình hội đồng quản trị', i+1, 'Dự thảo chiến lược và chính sách quản trị rủi ro')
        current_dieu = None
    elif current_dieu == '10' and 'xác định khẩu vị rủi ro dưới hình thức tuyên bố' in text.lower():
        add_task('10', 'Xác định khẩu vị rủi ro', 'Công ty xác định khẩu vị rủi ro dưới hình thức tuyên bố bằng văn bản', i+1, 'xác định khẩu vị rủi ro dưới hình thức tuyên bố')
        current_dieu = None
    elif current_dieu == '11' and 'chính sách quản trị rủi ro cần được xây dựng bằng văn bản' in text.lower():
        add_task('11', 'Xây dựng chính sách rủi ro bằng văn bản', 'Chính sách quản trị rủi ro được xây dựng bằng văn bản', i+1, 'Chính sách quản trị rủi ro cần được xây dựng bằng văn bản')
        current_dieu = None
    elif current_dieu == '12' and 'xây dựng chiến lược, chính sách quản trị rủi ro cho các quỹ' in text.lower():
        add_task('12', 'Xây dựng chiến lược quản trị rủi ro cho các quỹ', 'Xây dựng chiến lược, chính sách quản trị rủi ro cho các quỹ, danh mục', i+1, 'xây dựng chiến lược, chính sách quản trị rủi ro cho các quỹ')
        current_dieu = None

# We must be careful because the exact quotes might not match due to line breaks or slightly different words.
# Let's extract tasks dynamically by reading the first 7 articles.
