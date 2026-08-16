import csv

# 1. Update existing tasks with REJECTED and UC mappings
tasks = []
with open('_data/task_registry.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        tasks.append(row)

for t in tasks:
    if t[0] == 'T-BO-058':
        t[17] = 'UC-031'
    elif t[0] == 'T-BO-059':
        t[17] = 'UC-032'
    elif t[0] == 'T-BO-060':
        t[17] = 'REJECTED (Phụ thuộc vào mô hình định lượng Quant/VaR, không phù hợp GenAI)'
    elif t[0] == 'T-BO-061':
        t[17] = 'REJECTED (Quyết định mang tính chiến lược của Ban điều hành)'
    elif t[0] == 'T-BO-062':
        t[17] = 'REJECTED (Đã được thiết kế ở UC-028)'
    elif t[0] == 'T-BO-063':
        t[17] = 'UC-033'
    elif t[0] == 'T-BO-064':
        t[17] = 'REJECTED (Sử dụng mô hình tài chính Quant, không phải AI ngôn ngữ)'
    elif t[0] == 'T-BO-065':
        t[17] = 'REJECTED (Đã được thiết kế ở UC-029)'
    elif t[0] == 'T-BO-066':
        t[17] = 'REJECTED (Quy trình lưu trữ hệ thống, không cần AI)'
    elif t[0] == 'T-BO-067':
        t[17] = 'REJECTED (Cần sự giám sát, đánh giá chuyên môn độc lập của con người)'

with open('_data/task_registry.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(tasks)

# 2. Append new UCs
new_ucs = [
    [
        'UC-031', 'T-BO-058', 'Performance & Risk Management', 'Trợ lý AI rà soát và đối chiếu chính sách QTRR nội bộ với pháp luật',
        '3-Phân tích chuyên sâu', 'AI Agent',
        'Chính sách rủi ro nội bộ có thể bị lỗi thời hoặc thiếu sót so với các Thông tư, Quyết định mới của UBCKNN.',
        '1. Thu thập chính sách nội bộ & quy chế pháp luật. 2. So sánh đối chiếu. 3. Chỉ ra điểm khác biệt/thiếu sót. 4. Báo cáo Ban điều hành.',
        'Bước 2, 3: AI đóng vai trò pháp chế, đọc cả 2 văn bản và lập bảng so sánh (Gap analysis) để highlight các điều khoản chưa tuân thủ.',
        'CRO hoặc Pháp chế quỹ sẽ đọc báo cáo Gap Analysis và tự tay điều chỉnh chính sách nội bộ.',
        'Tài liệu chính sách QTRR (Word/PDF), Văn bản quy phạm pháp luật', 'QĐ 428/QĐ-UBCK', 'Đảm bảo tuân thủ tuyệt đối, tiết kiệm công sức rà soát thủ công',
        'CATALOGUE', 'S-REG-QD428', '_raw/legal/thuvienphapluat-QD428-2013.md', 'Chưa phỏng vấn mức độ thường xuyên thay đổi của chính sách', 'Y',
        '4', '3', '4', '3', '3.60', 'Chiến lược',
        'Giá trị: 4 (bảo vệ tuân thủ cốt lõi), Khả thi: 3 (LLM đọc luật tốt nhưng cần tuning ngữ cảnh quỹ), Dữ liệu: 4 (Văn bản có sẵn), Rủi ro: 3 (Có Human-in-the-loop).'
    ],
    [
        'UC-032', 'T-BO-059', 'Performance & Risk Management', 'Trợ lý AI tổng hợp tin tức vĩ mô để cảnh báo rủi ro thị trường',
        '2-Tổng hợp & phân tích', 'AI Agent',
        'Chuyên viên rủi ro mất nhiều thời gian đọc tin tức hàng ngày để nhận diện rủi ro tiềm ẩn (thị trường, thanh khoản, v.v.).',
        '1. Đọc tin tức, báo cáo ngành. 2. Trích lọc thông tin rủi ro. 3. Tóm tắt và gửi email/thông báo nội bộ.',
        'Bước 1, 2: AI tự động crawl các trang tin tức/báo cáo vĩ mô, lọc ra các key events ảnh hưởng đến danh mục của quỹ và tóm tắt thành gạch đầu dòng.',
        'Chuyên viên chỉ dùng tin tức AI tóm tắt làm nguồn tham khảo, quyết định nhận diện rủi ro cuối cùng là của con người.',
        'Tin tức tài chính, báo cáo ngành, API dữ liệu', 'QĐ 428/QĐ-UBCK Điều 8-12', 'Tiết kiệm 1-2h đọc báo mỗi ngày',
        'CATALOGUE', 'S-REG-QD428', '_raw/legal/thuvienphapluat-QD428-2013.md', '', 'Y',
        '4', '4', '4', '2', '3.70', 'Chiến lược',
        'Giá trị: 4 (Tăng tốc nhận diện rủi ro), Khả thi: 4 (Tóm tắt tin tức là điểm mạnh của LLM), Dữ liệu: 4 (Nguồn tin mở dồi dào), Rủi ro: 2 (Sai thì chỉ là tin rác, rủi ro thấp).'
    ],
    [
        'UC-033', 'T-BO-063', 'Performance & Risk Management', 'Tự động soạn thảo dự thảo Báo cáo ngoại lệ (Exception Report)',
        '4-Sinh nội dung', 'RPA + AI',
        'Khi có vi phạm hạn mức, việc chắp bút báo cáo giải trình mất thời gian, làm chậm trễ quy trình báo cáo Ban điều hành.',
        '1. Phát hiện vi phạm. 2. Thu thập dữ liệu vị thế & thị trường. 3. Soạn báo cáo ngoại lệ. 4. Đệ trình phê duyệt.',
        'Bước 3: Dựa trên log vi phạm, AI tự động lấy dữ liệu từ hệ thống, điền vào mẫu Exception Report chuẩn và sinh sẵn câu giải trình ban đầu.',
        'Chuyên viên phải đọc lại toàn bộ và sửa phần nguyên nhân (Root cause) và phương án khắc phục trước khi đệ trình.',
        'Hệ thống hạn mức rủi ro, Template báo cáo ngoại lệ', 'QĐ 428/QĐ-UBCK Điều 19', 'Rút ngắn thời gian xử lý sự cố',
        'CATALOGUE', 'S-REG-QD428', '_raw/legal/thuvienphapluat-QD428-2013.md', 'Tần suất ngoại lệ thường không cao', 'Y',
        '3', '4', '5', '3', '3.75', 'Chiến lược',
        'Giá trị: 3 (Chỉ tiết kiệm chút thời gian soạn thảo), Khả thi: 4 (Templated generation), Dữ liệu: 5 (Log vi phạm có cấu trúc rõ ràng), Rủi ro: 3 (Văn bản trình sếp).'
    ]
]

ucs = []
with open('_data/usecase_registry.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header_uc = next(reader)
    for row in reader:
        ucs.append(row)

ucs.extend(new_ucs)

with open('_data/usecase_registry.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header_uc)
    writer.writerows(ucs)

print("Use cases generated and manual scores applied without functions.")
