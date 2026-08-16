import csv
import re
import os

# 1. Update task_registry
tasks = []
with open('_data/task_registry.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        # Dedup: T-BO-031
        if row[0] == 'T-BO-031':
            row[19] = row[19] + ',S-REG-QD428' if 'S-REG-QD428' not in row[19] else row[19]
            row[20] = row[20] + ' | tuân thủ các hạn mức đầu tư'
            row[22] = row[22] + ',_raw/legal/quyet-dinh-428-qd-ubck.txt#L295'
        # Dedup: T-BO-055
        elif row[0] == 'T-BO-055':
            row[19] = row[19] + ',S-REG-QD428' if 'S-REG-QD428' not in row[19] else row[19]
            row[17] = row[17] + ' | Quyết định 428/QĐ-UBCK, Điều 5, 10'
            row[20] = row[20] + ' | xác định khẩu vị rủi ro dưới hình thức tuyên bố'
            row[22] = row[22] + ',_raw/legal/quyet-dinh-428-qd-ubck.txt#L248'
        # Dedup: T-BO-056
        elif row[0] == 'T-BO-056':
            row[19] = row[19] + ',S-REG-QD428' if 'S-REG-QD428' not in row[19] else row[19]
            row[17] = row[17] + ' | Quyết định 428/QĐ-UBCK, Điều 13, 14'
            row[20] = row[20] + ' | lập báo cáo định kỳ về danh mục đầu tư và kiểm soát rủi ro'
            row[22] = row[22] + ',_raw/legal/quyet-dinh-428-qd-ubck.txt#L296'
        
        tasks.append(row)

# Append manual tasks for Điều 3, 6, 11, 15
new_tasks = [
    [
        'T-BO-058', 'Back Office', 'Performance & Risk Management', 'Quản trị rủi ro',
        'Đánh giá và cập nhật chiến lược, chính sách quản trị rủi ro định kỳ',
        'Đánh giá lại, điều chỉnh và bổ sung các chiến lược, chính sách và quy trình quản lý rủi ro cho phù hợp với quy mô hoạt động và bối cảnh thị trường.',
        'Chiến lược, chính sách và quy trình QTRR hiện tại', 'Ban điều hành', 'Chiến lược, chính sách QTRR cập nhật', 'Hội đồng quản trị',
        'Quản trị rủi ro', '', 'Định kỳ hàng năm', '', '', '', '',
        'Quyết định 428/QĐ-UBCK, Điều 3', 'REG', 'S-REG-QD428', 'các chiến lược, chính sách và quy trình quản lý rủi ro của công ty phải được đánh giá lại, điều chỉnh', 'Y',
        '_raw/legal/quyet-dinh-428-qd-ubck.txt#L117'
    ],
    [
        'T-BO-059', 'Back Office', 'Performance & Risk Management', 'Quản trị rủi ro',
        'Dự thảo chiến lược và chính sách quản trị rủi ro trình Hội đồng quản trị',
        'Dự thảo các chiến lược và chính sách quản trị rủi ro để trình lên Hội đồng quản trị hoặc chủ sở hữu phê duyệt và ban hành.',
        'Đề xuất từ bộ phận nghiệp vụ', 'Bộ phận nghiệp vụ', 'Dự thảo chiến lược và chính sách QTRR', 'Hội đồng quản trị',
        'Ban điều hành', 'Quản trị rủi ro', 'Khi phát sinh', '', '', '', '',
        'Quyết định 428/QĐ-UBCK, Điều 6', 'REG', 'S-REG-QD428', 'Dự thảo chiến lược và chính sách quản trị rủi ro trình hội đồng quản trị', 'Y',
        '_raw/legal/quyet-dinh-428-qd-ubck.txt#L176'
    ],
    [
        'T-BO-060', 'Back Office', 'Performance & Risk Management', 'Quản trị rủi ro',
        'Phổ biến chính sách quản trị rủi ro bằng văn bản cho toàn công ty',
        'Xây dựng chính sách quản trị rủi ro bằng văn bản và đảm bảo mọi cá nhân, bộ phận được tiếp cận và nắm vững trách nhiệm.',
        'Chính sách QTRR đã được phê duyệt', 'Hội đồng quản trị', 'Văn bản phổ biến chính sách QTRR', 'Toàn bộ nhân viên',
        'Quản trị rủi ro', 'Nhân sự', 'Khi ban hành chính sách mới', '', '', '', '',
        'Quyết định 428/QĐ-UBCK, Điều 11', 'REG', 'S-REG-QD428', 'Chính sách quản trị rủi ro cần được xây dựng bằng văn bản, đảm bảo mọi cá nhân và bộ phận', 'Y',
        '_raw/legal/quyet-dinh-428-qd-ubck.txt#L263'
    ],
    [
        'T-BO-061', 'Back Office', 'Performance & Risk Management', 'Quản trị rủi ro',
        'Lưu trữ hồ sơ và tài liệu của hệ thống quản trị rủi ro',
        'Ghi nhận và lưu trữ đầy đủ các chính sách, quy trình, hệ thống đánh giá rủi ro và các báo cáo vi phạm để phục vụ việc giám sát.',
        'Chính sách, quy trình, báo cáo rủi ro', 'Các bộ phận', 'Hồ sơ lưu trữ QTRR', 'UBCKNN / Kiểm toán nội bộ',
        'Quản trị rủi ro', 'Kiểm soát nội bộ', 'Liên tục', '', '', '', '',
        'Quyết định 428/QĐ-UBCK, Điều 15', 'REG', 'S-REG-QD428', 'đảm bảo các chính sách, quy trình, hệ thống được ghi nhận và lưu trữ đầy đủ', 'Y',
        '_raw/legal/quyet-dinh-428-qd-ubck.txt#L321'
    ]
]
tasks.extend(new_tasks)

with open('_data/task_registry.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(tasks)

# 2. Update SOURCE_REGISTRY S-REG-QD428 to exactly 13 columns
sources = []
with open('_data/SOURCE_REGISTRY.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    src_header = next(r)
    for row in r:
        sources.append(row)

# Append correct row
sources.append([
    'S-REG-QD428', 'T1', 'Quy định pháp lý', 'Quyết định 428/QĐ-UBCK 2013 hướng dẫn thiết lập hệ thống quản trị rủi ro',
    'Ủy ban Chứng khoán Nhà nước', 'https://luatvietnam.vn/dau-tu/quyet-dinh-428-qd-ubck-uy-ban-chung-khoan-nha-nuoc-225841-d1.html',
    '2013-07-11', '2026-08-16', 'vi', '5', 'Quản trị rủi ro công ty quản lý quỹ', '', 'ĐANG DÙNG'
])

with open('_data/SOURCE_REGISTRY.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(src_header)
    w.writerows(sources)

# 3. Add Use Cases for the new tasks
ucs = []
with open('_data/usecase_registry.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    uc_header = next(r)
    for row in r:
        ucs.append(row)

ucs.extend([
    [
        'UC-031', 'Back Office', 'Performance & Risk Management', 'Đánh giá chiến lược quản lý rủi ro',
        'Hệ thống theo dõi lịch đánh giá định kỳ các chính sách quản trị rủi ro và thông báo cho ban điều hành.',
        'Hệ thống gửi cảnh báo khi đến kỳ đánh giá hàng năm; lưu trữ lịch sử các phiên bản chính sách; theo dõi trạng thái phê duyệt.',
        'Quản trị rủi ro', 'Hệ thống Quản trị rủi ro', 'T-BO-058', 'Medium', 'Y', '', '',
        'Hỗ trợ theo dõi chu kỳ đánh giá rủi ro; giảm thiểu rủi ro pháp lý; lưu trữ phiên bản chính sách'
    ],
    [
        'UC-032', 'Back Office', 'Performance & Risk Management', 'Quy trình dự thảo và phê duyệt chính sách',
        'Tự động hóa luồng trình duyệt và phổ biến chính sách rủi ro mới.',
        'Ban điều hành tạo dự thảo trên hệ thống; Hệ thống định tuyến phê duyệt tới HĐQT; Khi được phê duyệt, tự động gửi thông báo phổ biến tới toàn thể nhân viên.',
        'Quản trị rủi ro', 'Hệ thống Quản trị rủi ro', 'T-BO-059,T-BO-060', 'High', 'Y', '', '',
        'Đảm bảo quy trình phê duyệt minh bạch; lưu vết kiểm toán rõ ràng; 100% nhân viên nhận được thông báo.'
    ],
    [
        'UC-033', 'Back Office', 'Performance & Risk Management', 'Lưu trữ hồ sơ quản trị rủi ro tập trung',
        'Kho dữ liệu tập trung (Centralized Repository) để lưu trữ mọi tài liệu liên quan đến QTRR.',
        'Hệ thống tự động lưu trữ có phân quyền truy cập, ghi log lịch sử xem/sửa tài liệu, phục vụ trích xuất hồ sơ ngay lập tức khi UBCKNN hoặc Kiểm toán yêu cầu.',
        'Quản trị rủi ro', 'Hệ thống Quản trị rủi ro', 'T-BO-061', 'Low', 'Y', '', '',
        'Lưu trữ hồ sơ an toàn; truy xuất nhanh chóng phục vụ kiểm toán; tránh thất lạc thông tin.'
    ]
])

with open('_data/usecase_registry.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(uc_header)
    w.writerows(ucs)
