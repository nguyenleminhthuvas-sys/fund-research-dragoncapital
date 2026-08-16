import csv
import os

# 1. Update tasks T-BO-031, T-BO-051, T-BO-044
tasks = []
with open('_data/task_registry.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if row[0] == 'T-BO-031':
            row[16] = "Tỷ lệ đầu tư vào một tổ chức phát hành vượt mức trần 20% (chiếm tới 33%), vi phạm TT98 và bị UBCKNN xử phạt 120 triệu (MB Capital)"
        elif row[0] == 'T-BO-051':
            row[16] = "Không nộp báo cáo kiểm toán nội bộ và báo cáo đánh giá rủi ro về PCRT cho Ngân hàng Nhà nước và UBCKNN, bị phạt 92.5 triệu đồng (Amber Capital)"
        elif row[0] == 'T-BO-044':
            row[16] = "Thiếu thông tin nhận biết khách hàng ủy thác/tư vấn đầu tư trước khi ký hợp đồng và không cập nhật KYC định kỳ hàng năm, bị phạt 65 triệu đồng (Amber Capital)"
        tasks.append(row)

# Append new tasks from MB Capital and Amber Capital
new_tasks = [
    # T-BO-057
    ['T-BO-057', 'Back Office', 'Performance & Risk Management', 'Tái cơ cấu danh mục', 'Điều chỉnh, tái cơ cấu danh mục khi phát sinh sai lệch', 'Điều chỉnh danh mục trong thời hạn 3 tháng khi các tỷ lệ đầu tư bị sai lệch do biến động thị trường hoặc vi phạm', 'Danh mục thực tế, kế hoạch giao dịch', 'Quản trị rủi ro / Đầu tư', 'Lệnh giao dịch, Báo cáo tái cơ cấu', 'Ban điều hành', 'Bộ phận Đầu tư', '', 'Định kỳ/Khi phát sinh', '', '', '', 'Quỹ không thể điều chỉnh lại cơ cấu danh mục đầu tư trong thời hạn 3 tháng kể từ thời điểm phát sinh sai lệch, vi phạm TT98 (MB Capital)', 'REJECTED (Low Feasibility)', 'FACT', 'S-ENF-120KL', 'Kết luận thanh tra MB Capital 120/KL-TT', 'N', '_raw/enforcement/thanhtra-mb-capital-xu-phat-120kl.md'],
    # T-BO-058
    ['T-BO-058', 'Back Office', 'Performance & Risk Management', 'Quản lý vòng đời quỹ', 'Thực hiện thanh lý tài sản và báo cáo giải thể quỹ', 'Thực hiện thu hồi các khoản phải thu, thanh lý tài sản và hoàn tất hồ sơ giải thể quỹ gửi UBCKNN', 'Hồ sơ tài sản, biên bản họp', 'Ban điều hành', 'Báo cáo giải thể', 'UBCKNN', 'Kế toán quỹ / Pháp chế', '', 'Khi phát sinh', '', '', '', 'Quá trình thanh lý tài sản và giải thể quỹ kéo dài nhiều năm do các khoản phải thu khó đòi bị gia hạn liên tục, vi phạm tiến độ báo cáo giải thể (MB Capital)', 'REJECTED (Manual process)', 'FACT', 'S-ENF-120KL', 'Kết luận thanh tra MB Capital 120/KL-TT', 'N', '_raw/enforcement/thanhtra-mb-capital-xu-phat-120kl.md'],
    # T-BO-059
    ['T-BO-059', 'Back Office', 'Performance & Risk Management', 'Báo cáo cơ quan quản lý', 'Lập báo cáo hoạt động tư vấn đầu tư gửi UBCKNN', 'Lập báo cáo định kỳ hàng tháng về số lượng hợp đồng, giá trị tư vấn đầu tư gửi UBCKNN', 'Hợp đồng tư vấn đầu tư', 'Phát triển kinh doanh', 'Báo cáo hoạt động', 'UBCKNN', 'Tuân thủ / Báo cáo', '', 'Hàng tháng', '', '', '', 'Không báo cáo hoặc báo cáo thiếu nội dung về hoạt động tư vấn đầu tư gửi UBCKNN, dẫn đến bị xử phạt 65 triệu đồng (Amber Capital)', 'UC-030', 'FACT', 'S-ENF-AMBER', 'Thời báo Tài chính xử phạt Amber Capital', 'Y', '_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md'],
    # T-BO-060
    ['T-BO-060', 'Back Office', 'Client Reporting', 'Báo cáo khách hàng', 'Báo cáo tình hình danh mục đầu tư cho khách hàng ủy thác', 'Tổng hợp số liệu danh mục, hiệu quả đầu tư và gửi báo cáo định kỳ cho các khách hàng ủy thác', 'Dữ liệu giao dịch, NAV', 'Kế toán quỹ', 'Báo cáo danh mục định kỳ', 'Khách hàng ủy thác', 'Chăm sóc khách hàng', '', 'Hàng tháng', '', '', '', 'Bỏ sót việc báo cáo tình hình danh mục đầu tư định kỳ hàng tháng cho khách hàng ủy thác, vi phạm quy định (Amber Capital)', 'UC-031', 'FACT', 'S-ENF-AMBER', 'Thời báo Tài chính xử phạt Amber Capital', 'Y', '_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md'],
    # T-BO-061
    ['T-BO-061', 'Back Office', 'Performance & Risk Management', 'Quản lý tài sản ủy thác', 'Kiểm soát mục đích sử dụng tài sản ủy thác', 'Kiểm soát các giao dịch, hợp đồng đặt cọc để đảm bảo tài sản ủy thác không bị sử dụng sai mục đích (như cho vay trái phép)', 'Hợp đồng, chứng từ giao dịch', 'Đầu tư / Kế toán', 'Biên bản kiểm duyệt', 'Ban điều hành', 'Kiểm soát nội bộ', '', 'Liên tục', '', '', '', 'Sử dụng tài sản ủy thác (ký hợp đồng đặt cọc) để cho vay trái phép, bị xử phạt nặng 187 triệu đồng (Amber Capital)', 'UC-032', 'FACT', 'S-ENF-AMBER', 'Thời báo Tài chính xử phạt Amber Capital', 'Y', '_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md']
]
tasks.extend(new_tasks)

with open('_data/task_registry.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(tasks)


# 2. Append use cases
new_ucs = [
    [
        'UC-030', 'T-BO-059', 'Performance & Risk Management', 'Tự động trích xuất dữ liệu hợp đồng tư vấn và điền báo cáo hoạt động gửi UBCKNN', 
        '1-Trích xuất & phân loại', 'RPA + AI', 
        'Không báo cáo đầy đủ về hợp đồng tư vấn đầu tư dẫn đến bị phạt 65 triệu đồng.', 
        '1. Đọc hợp đồng. 2. Trích xuất giá trị, thời hạn. 3. Điền biểu mẫu báo cáo. 4. Gửi duyệt.', 
        'Bước 2, 3: AI trích xuất thông tin trọng yếu từ hợp đồng tư vấn (PDF/Word) và tự động populate vào báo cáo định kỳ tháng.', 
        'Chuyên viên kiểm tra lại số liệu trên báo cáo trước khi ký số nộp UBCKNN.', 
        'File hợp đồng tư vấn, Template báo cáo', 'Quy định báo cáo UBCKNN', 'Không bị phạt, tiết kiệm thời gian', 
        'CATALOGUE', 'S-ENF-AMBER', '_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md', 'Chưa khảo sát số lượng hợp đồng tư vấn', 'Y',
        '4', '4', '4', '2', '3.70', 'Chiến lược', 
        'Giá trị: 4 (tránh phạt 65tr), Khả thi: 4 (trích xuất HĐ khá chuẩn), Dữ liệu: 4 (hợp đồng có sẵn), Rủi ro: 2 (có người duyệt).'
    ],
    [
        'UC-031', 'T-BO-060', 'Client Reporting', 'Tự động sinh báo cáo danh mục định kỳ cho khách hàng ủy thác', 
        '4-Sinh nội dung', 'RPA + AI', 
        'Quên gửi hoặc gửi chậm báo cáo cho khách hàng ủy thác dẫn đến bị UBCKNN phạt.', 
        '1. Tổng hợp NAV. 2. Lập báo cáo từng KH. 3. Gửi email.', 
        'Bước 2, 3: Bot tự động kết xuất dữ liệu, AI sinh nhận xét ngắn gọn về hiệu quả danh mục và tự động gửi email cho KH.', 
        'Review xác suất 10% báo cáo trước khi hệ thống tự động gửi.', 
        'Dữ liệu NAV, Email khách hàng', 'Hợp đồng ủy thác', 'Đúng hạn 100%, tránh rủi ro phạt', 
        'CATALOGUE', 'S-ENF-AMBER', '_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md', 'Cần kiểm tra định dạng báo cáo', 'Y',
        '5', '5', '5', '3', '4.70', 'Quick win', 
        'Giá trị: 5 (bảo vệ uy tín & tránh phạt), Khả thi: 5 (rule-based và templated), Dữ liệu: 5 (dữ liệu kế toán chuẩn), Rủi ro: 3.'
    ],
    [
        'UC-032', 'T-BO-061', 'Performance & Risk Management', 'AI phân tích ngữ nghĩa hợp đồng để phát hiện rủi ro lách luật cho vay', 
        '3-Phân tích chuyên sâu', 'AI Agent', 
        'Sử dụng tài sản ủy thác ký hợp đồng đặt cọc lách luật cho vay bị phạt 187 triệu đồng.', 
        '1. Soạn hợp đồng. 2. Kiểm duyệt pháp lý. 3. Ký kết.', 
        'Bước 2: AI rà soát ngôn ngữ hợp đồng, đối chiếu với luật chứng khoán để phất cờ cảnh báo (red flag) nếu bản chất hợp đồng là cho vay.', 
        'Pháp chế và kiểm soát nội bộ đưa ra quyết định cuối cùng.', 
        'Bản thảo hợp đồng', 'Luật Chứng khoán', 'Phát hiện sớm rủi ro gian lận', 
        'CATALOGUE', 'S-ENF-AMBER', '_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md', 'Phụ thuộc vào mô hình LLM tiếng Việt', 'Y',
        '5', '3', '3', '4', '3.85', 'Quick win', 
        'Giá trị: 5 (ngăn chặn vi phạm đặc biệt nghiêm trọng), Khả thi: 3 (phân tích ngữ nghĩa pháp lý tiếng Việt khó), Dữ liệu: 3, Rủi ro: 4.'
    ]
]

with open('_data/usecase_registry.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(new_ucs)

print("Tasks and UCs appended.")
