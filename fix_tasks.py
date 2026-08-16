import csv
import sys

# Load current tasks
tasks = []
with open('_data/task_registry.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        tasks.append(row)

# Load current UCs
ucs = []
with open('_data/usecase_registry.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header_uc = next(reader)
    for row in reader:
        ucs.append(row)

# Filter out mistakenly created tasks (T-BO-057 to T-BO-061) and UCs (UC-030 to UC-032) from previous bad run
tasks = [t for t in tasks if t[0] not in ['T-BO-057', 'T-BO-058', 'T-BO-059', 'T-BO-060', 'T-BO-061']]
ucs = [u for u in ucs if u[0] not in ['UC-030', 'UC-031', 'UC-032']]

# Re-apply pain points correctly to existing tasks for MB Capital & Amber Capital
for t in tasks:
    if t[0] == 'T-BO-031': # Kiểm soát tuân thủ hạn mức
        t[16] = 'Tỷ lệ đầu tư vào trái phiếu NVL vượt mức 20% (chiếm 33% danh mục); không thể điều chỉnh cơ cấu trong thời hạn 3 tháng (MB Capital)'
        t[18] = 'FACT'
        if 'S-ENF-120KL' not in t[19]:
            t[19] += ',S-ENF-120KL'
            t[20] += ',Kết luận thanh tra MB Capital 120/KL-TT'
            t[22] += ',_raw/enforcement/thanhtra-mb-capital-xu-phat-120kl.md'
    elif t[0] == 'T-BO-020': # Báo cáo nội bộ và UBCKNN
        t[16] = 'Không báo cáo hoạt động tư vấn đầu tư định kỳ gửi UBCKNN dẫn đến bị xử phạt (Amber Capital)'
        t[18] = 'FACT'
        if 'S-ENF-AMBER' not in t[19]:
            t[19] += ',S-ENF-AMBER'
            t[20] += ',Thời báo Tài chính xử phạt Amber Capital'
            t[22] += ',_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md'
    elif t[0] == 'T-BO-022': # Cập nhật báo cáo nhà đầu tư
        t[16] = 'Không thực hiện báo cáo tình hình danh mục đầu tư định kỳ hàng tháng cho khách hàng ủy thác (Amber Capital)'
        t[18] = 'FACT'
        if 'S-ENF-AMBER' not in t[19]:
            t[19] += ',S-ENF-AMBER'
            t[20] += ',Thời báo Tài chính xử phạt Amber Capital'
            t[22] += ',_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md'
    elif t[0] == 'T-BO-044': # KYC
        t[16] = 'Không thực hiện tổng hợp và cập nhật thông tin nhận biết khách hàng định kỳ và trước khi ký hợp đồng (Amber Capital)'
        t[18] = 'FACT'
        if 'S-ENF-AMBER' not in t[19]:
            t[19] += ',S-ENF-AMBER'
            t[20] += ',Thời báo Tài chính xử phạt Amber Capital'
            t[22] += ',_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md'
    elif t[0] == 'T-BO-051': # Báo cáo đánh giá rủi ro rửa tiền
        t[16] = 'Không nộp báo cáo kiểm toán nội bộ và báo cáo đánh giá cập nhật rủi ro rửa tiền cho NHNN và UBCKNN (Amber Capital)'
        t[18] = 'FACT'
        if 'S-ENF-AMBER' not in t[19]:
            t[19] += ',S-ENF-AMBER'
            t[20] += ',Thời báo Tài chính xử phạt Amber Capital'
            t[22] += ',_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md'

# Create a new task for Amber's cho vay trái phép because no existing task matches it perfectly
tasks.append([
    'T-BO-057', 'Back Office', 'Tuân thủ', 'Kiểm soát tài sản',
    'Kiểm soát mục đích sử dụng tài sản ủy thác',
    'Kiểm soát hợp đồng và giao dịch để không sử dụng tài sản ủy thác lách luật cho vay',
    'Bản thảo hợp đồng, chứng từ giao dịch', 'Đầu tư / Pháp chế',
    'Ý kiến kiểm soát pháp lý', 'Ban điều hành', 'Kiểm soát nội bộ / Tuân thủ', '',
    'Trước khi ký kết', '', '', '',
    'Sử dụng tài sản uỷ thác để cho vay dưới mọi hình thức (ký hợp đồng đặt cọc mua cổ phiếu để cho vay), bị phạt 187 triệu (Amber Capital)',
    'UC-030', 'FACT', 'S-ENF-AMBER', 'Thời báo Tài chính xử phạt Amber Capital', 'Y',
    '_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md'
])

# New Use Case for Amber's cho vay trái phép
ucs.append([
    'UC-030', 'T-BO-057', 'Tuân thủ', 'AI phân tích ngữ nghĩa hợp đồng để phát hiện rủi ro lách luật cho vay',
    '3-Phân tích chuyên sâu', 'AI Agent',
    'Sử dụng tài sản ủy thác ký hợp đồng đặt cọc lách luật cho vay bị phạt nặng.',
    '1. Tải bản thảo hợp đồng. 2. Kiểm tra điều khoản. 3. Phê duyệt.',
    'Bước 2: AI rà soát ngôn ngữ hợp đồng, đối chiếu luật để cảnh báo nếu bản chất là cho vay.',
    'Chuyên viên pháp chế duyệt lại kết quả cảnh báo của AI.',
    'Bản thảo hợp đồng', 'Luật Chứng khoán', 'Phát hiện sớm rủi ro gian lận',
    'CATALOGUE', 'S-ENF-AMBER', '_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md', '', 'Y',
    '5', '3', '3', '4', '3.85', 'Quick win',
    'Giá trị: 5 (ngăn chặn vi phạm đặc biệt nghiêm trọng), Khả thi: 3 (phân tích ngữ nghĩa tiếng Việt khó), Dữ liệu: 3, Rủi ro: 4.'
])


# Now, generate 10 tasks for QĐ 428/QĐ-UBCK (T-BO-058 to T-BO-067)
qd428_tasks = [
    # 1. Xây dựng và rà soát chính sách rủi ro (Điều 4,5)
    ['T-BO-058', 'Back Office', 'Performance & Risk Management', 'Chính sách rủi ro',
     'Xây dựng và rà soát chính sách quản trị rủi ro',
     'Xây dựng các bộ chính sách quản trị rủi ro cho công ty và quỹ, định kỳ rà soát và cập nhật',
     'Quy định pháp luật, chiến lược kinh doanh', 'Ban điều hành', 'Tài liệu chính sách quản trị rủi ro', 'Hội đồng quản trị', 'Quản trị rủi ro', '', 'Định kỳ/Khi có thay đổi', '', '', '', '', '', 'REG', 'S-REG-QD428', 'QĐ 428/QĐ-UBCK Điều 4', 'N', '_raw/legal/thuvienphapluat-QD428-2013.md'],
    
    # 2. Nhận diện rủi ro theo từng loại (Điều 8-12)
    ['T-BO-059', 'Back Office', 'Performance & Risk Management', 'Nhận diện rủi ro',
     'Nhận diện các rủi ro trọng yếu',
     'Nhận diện rủi ro thị trường, thanh khoản, hoạt động, pháp lý và tín dụng trong mọi hoạt động đầu tư',
     'Dữ liệu thị trường, báo cáo vĩ mô', 'Đầu tư', 'Báo cáo nhận diện rủi ro', 'Ban điều hành', 'Quản trị rủi ro', '', 'Liên tục', '', '', '', '', '', 'REG', 'S-REG-QD428', 'QĐ 428/QĐ-UBCK Điều 8-12', 'N', '_raw/legal/thuvienphapluat-QD428-2013.md'],
    
    # 3. Đo lường rủi ro, phương pháp và tần suất (Điều 14)
    ['T-BO-060', 'Back Office', 'Performance & Risk Management', 'Đo lường rủi ro',
     'Đo lường rủi ro danh mục đầu tư',
     'Áp dụng các mô hình (như VaR) để đo lường định lượng rủi ro của từng quỹ theo tần suất quy định',
     'Dữ liệu giá tài sản, danh mục', 'Hệ thống IT', 'Kết quả đo lường rủi ro định lượng', 'Quản trị rủi ro', 'Quản trị rủi ro', '', 'Hàng ngày', '', '', '', '', '', 'REG', 'S-REG-QD428', 'QĐ 428/QĐ-UBCK Điều 14', 'N', '_raw/legal/thuvienphapluat-QD428-2013.md'],
    
    # 4. Thiết lập, phê duyệt hạn mức (Điều 15)
    ['T-BO-061', 'Back Office', 'Performance & Risk Management', 'Hạn mức rủi ro',
     'Thiết lập và phê duyệt hạn mức rủi ro',
     'Đề xuất các hạn mức rủi ro cụ thể cho từng quỹ để Ban điều hành phê duyệt',
     'Mức chấp nhận rủi ro, kết quả đo lường', 'Ban điều hành', 'Danh mục hạn mức rủi ro được duyệt', 'Các bộ phận', 'Quản trị rủi ro', '', 'Định kỳ', '', '', '', '', '', 'REG', 'S-REG-QD428', 'QĐ 428/QĐ-UBCK Điều 15', 'N', '_raw/legal/thuvienphapluat-QD428-2013.md'],
    
    # 5. Theo dõi và cảnh báo khi tiệm cận (Điều 17)
    ['T-BO-062', 'Back Office', 'Performance & Risk Management', 'Cảnh báo rủi ro',
     'Theo dõi và cảnh báo sớm vi phạm hạn mức',
     'Giám sát liên tục danh mục, phát tín hiệu cảnh báo cho bộ phận đầu tư khi các chỉ số tiệm cận hoặc vượt hạn mức rủi ro',
     'Tín hiệu thị trường, NAV hàng ngày', 'Hệ thống rủi ro', 'Thông báo cảnh báo rủi ro', 'Đầu tư / Ban điều hành', 'Quản trị rủi ro', '', 'Hàng ngày', '', '', '', '', '', 'REG', 'S-REG-QD428', 'QĐ 428/QĐ-UBCK Điều 17', 'N', '_raw/legal/thuvienphapluat-QD428-2013.md'],
    
    # 6. Xử lý khi vượt hạn mức, báo cáo ngoại lệ (Điều 18, 19)
    ['T-BO-063', 'Back Office', 'Performance & Risk Management', 'Xử lý vi phạm',
     'Xử lý vi phạm và báo cáo ngoại lệ (Exception reporting)',
     'Lập phương án khắc phục ngay khi hạn mức bị vượt và báo cáo ngoại lệ lên Ban điều hành hoặc UBCKNN nếu trọng yếu',
     'Thông báo vượt hạn mức', 'Đầu tư', 'Báo cáo ngoại lệ, Phương án khắc phục', 'Ban điều hành / UBCKNN', 'Quản trị rủi ro', '', 'Khi phát sinh', '', '', '', '', '', 'REG', 'S-REG-QD428', 'QĐ 428/QĐ-UBCK Điều 18, 19', 'N', '_raw/legal/thuvienphapluat-QD428-2013.md'],
    
    # 7. Kiểm thử sức chịu đựng (Stress test) (Điều 20)
    ['T-BO-064', 'Back Office', 'Performance & Risk Management', 'Kiểm thử rủi ro',
     'Thực hiện kiểm thử sức chịu đựng (Stress test)',
     'Định kỳ chạy các kịch bản stress test (khủng hoảng thị trường, thanh khoản cạn kiệt) để đánh giá khả năng chịu đựng của quỹ',
     'Kịch bản vĩ mô, dữ liệu lịch sử', 'Hệ thống IT', 'Báo cáo kết quả stress test', 'Ban điều hành', 'Quản trị rủi ro', '', 'Hàng quý / năm', '', '', '', '', '', 'REG', 'S-REG-QD428', 'QĐ 428/QĐ-UBCK Điều 20', 'N', '_raw/legal/thuvienphapluat-QD428-2013.md'],
    
    # 8. Báo cáo rủi ro nội bộ và báo cáo UBCKNN (Điều 22, 23)
    ['T-BO-065', 'Back Office', 'Performance & Risk Management', 'Báo cáo rủi ro',
     'Lập báo cáo rủi ro nội bộ và gửi UBCKNN',
     'Tổng hợp tình hình rủi ro, kết quả giám sát định kỳ để lập báo cáo gửi Ban điều hành, Hội đồng quản trị và cơ quan quản lý',
     'Dữ liệu giám sát rủi ro', 'Nội bộ', 'Báo cáo rủi ro định kỳ', 'Ban điều hành / UBCKNN', 'Quản trị rủi ro', '', 'Tháng/Quý/Năm', '', '', '', '', '', 'REG', 'S-REG-QD428', 'QĐ 428/QĐ-UBCK Điều 22, 23', 'N', '_raw/legal/thuvienphapluat-QD428-2013.md'],
    
    # 9. Lưu trữ hồ sơ rủi ro (Điều 25)
    ['T-BO-066', 'Back Office', 'Performance & Risk Management', 'Lưu trữ tài liệu',
     'Lưu trữ hồ sơ và tài liệu quản trị rủi ro',
     'Tổ chức lưu trữ an toàn, bảo mật tất cả hồ sơ, báo cáo rủi ro để phục vụ thanh tra, kiểm toán',
     'Báo cáo rủi ro, biên bản xử lý', 'Nội bộ', 'Hệ thống lưu trữ hồ sơ rủi ro', 'Kiểm toán / UBCKNN', 'Quản trị rủi ro / Hành chính', '', 'Định kỳ', '', '', '', '', '', 'REG', 'S-REG-QD428', 'QĐ 428/QĐ-UBCK Điều 25', 'N', '_raw/legal/thuvienphapluat-QD428-2013.md'],
    
    # 10. Vai trò Ban điều hành & Kiểm soát nội bộ (Điều 27, 28)
    ['T-BO-067', 'Back Office', 'Performance & Risk Management', 'Phân định trách nhiệm',
     'Giám sát độc lập hoạt động quản trị rủi ro',
     'Bộ phận kiểm soát nội bộ rà soát, đánh giá tính tuân thủ và hiệu quả của hệ thống quản trị rủi ro',
     'Quy trình quản trị rủi ro', 'Quản trị rủi ro', 'Báo cáo đánh giá hệ thống quản trị rủi ro', 'Hội đồng quản trị', 'Kiểm soát nội bộ', '', 'Định kỳ', '', '', '', '', '', 'REG', 'S-REG-QD428', 'QĐ 428/QĐ-UBCK Điều 27', 'N', '_raw/legal/thuvienphapluat-QD428-2013.md']
]

tasks.extend(qd428_tasks)

with open('_data/task_registry.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(tasks)

with open('_data/usecase_registry.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header_uc)
    writer.writerows(ucs)

print(f"Tasks adjusted. Total tasks: {len(tasks)}. Total UCs: {len(ucs)}")
