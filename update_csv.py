import csv

# 1. Update T-BO-031 in task_registry.csv
with open('_data/task_registry.csv', 'r') as f:
    tasks = list(csv.reader(f))

for row in tasks:
    if row[0] == 'T-BO-031':
        # Append sources
        row[18] = row[18] + ',REG,FACT,FACT'
        row[19] = row[19] + ',S-REG-TT98,S-ENF-120KL,S-ENF-TCTC'
        row[20] = row[20] + ',Thông tư 98/2020/TT-BTC,Kết luận thanh tra MB Capital 120/KL-TT,Thời báo Tài chính xử phạt Thành Công'
        row[22] = row[22] + ',_raw/legal/thuvienphapluat-TT98-2020-461197.md,_raw/enforcement/thanhtra-mb-capital-xu-phat-120kl.md,_raw/enforcement/thoibaotaichinhvietnam-xu-phat.md'

# 2. Add 3 new tasks
new_tasks = [
    ['T-BO-054', 'Back Office', 'Performance & Risk Management', 'Đo lường hiệu quả', 'Đo lường và đánh giá hiệu quả hoạt động danh mục đầu tư (Performance Measurement)', 'Theo dõi tỷ suất lợi nhuận của danh mục, so sánh với chỉ số tham chiếu (benchmark) để đánh giá hiệu quả đầu tư định kỳ.', 'Dữ liệu NAV, danh mục đầu tư, chỉ số thị trường', 'Kế toán quỹ / Hệ thống thị trường', 'Báo cáo hiệu quả đầu tư (Performance Report)', 'Ban điều hành / Nhà đầu tư', 'Quản trị rủi ro / Phân tích', '', 'Định kỳ', '', '', '', '', 'UC-027', 'FACT', 'S-DOC-BVFED', 'Quỹ BVFED - Bảo Việt Fund', 'Y', '_raw/company/baovietfund-bvfed-ban-cao-bach-2018-11.pdf'],
    ['T-BO-055', 'Back Office', 'Performance & Risk Management', 'Quản trị rủi ro', 'Nhận diện, đánh giá và thiết lập hạn mức rủi ro', 'Nhận diện các rủi ro thị trường, thanh khoản, hoạt động; đánh giá mức độ và thiết lập hạn mức cảnh báo rủi ro nội bộ.', 'Quy định nội bộ, dữ liệu giao dịch', 'Ban điều hành / Bộ phận đầu tư', 'Sổ tay quản trị rủi ro, cảnh báo rủi ro', 'Kiểm soát nội bộ', 'Quản trị rủi ro', '', 'Liên tục', '', '', '', '', 'UC-028', 'REG', 'S-REG-TT99', 'Thông tư 99/2020/TT-BTC', 'Y', '_raw/legal/thuvienphapluat-TT99-2020.md'],
    ['T-BO-056', 'Back Office', 'Performance & Risk Management', 'Báo cáo', 'Lập báo cáo hoạt động quản trị rủi ro và kiểm soát nội bộ', 'Lập các báo cáo định kỳ về kiểm soát nội bộ, kết quả đo lường rủi ro và tình hình tuân thủ để gửi UBCKNN và Ban điều hành.', 'Dữ liệu cảnh báo, tình hình tuân thủ', 'Quản trị rủi ro / Kiểm soát tuân thủ', 'Báo cáo quản trị rủi ro, Báo cáo kiểm soát nội bộ', 'UBCKNN / Ban điều hành', 'Quản trị rủi ro / Kiểm soát nội bộ', '', 'Định kỳ (tháng/quý/năm)', '', '', '', 'Chậm trễ trong việc tổng hợp dữ liệu rủi ro từ nhiều nguồn khác nhau để làm báo cáo', 'UC-029', 'REG', 'S-REG-TT99', 'Thông tư 99/2020/TT-BTC', 'Y', '_raw/legal/thuvienphapluat-TT99-2020.md']
]
tasks.extend(new_tasks)

with open('_data/task_registry.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(tasks)

# 3. Add 3 new use cases to usecase_registry.csv
with open('_data/usecase_registry.csv', 'r') as f:
    ucs = list(csv.reader(f))

new_ucs = [
    ['UC-027', 'Back Office', 'Performance & Risk Management', 'Theo dõi hiệu quả danh mục đầu tư so với Benchmark', 'CATALOGUE',
     'Đọc dữ liệu NAV hàng ngày và biến động chỉ số thị trường (VNIndex, HNX).',
     'Trích xuất tỷ suất sinh lời danh mục và tỷ suất sinh lời benchmark.',
     'Tính toán tracking error, Alpha, Beta, Sharpe ratio.',
     'So sánh tỷ suất danh mục quỹ với benchmark tham chiếu.',
     '',
     'Tạo báo cáo phân tích hiệu quả hoạt động (Performance report).',
     '',
     '4', 'Tự động tính toán các chỉ số performance giúp PM nắm bắt nhanh hiệu quả.',
     '5', 'Công thức chuẩn toán học, dữ liệu số rõ ràng dễ tính bằng code/AI.',
     '4', 'Dữ liệu NAV và index sẵn có, nhưng cần chuẩn hóa đồng bộ thời gian.',
     '4', 'Rủi ro tính sai công thức dẫn đến báo cáo sai lệch.',
     '4.25', 'Quick win',
     'FACT', 'S-DOC-BVFED', 'Quỹ BVFED - Bảo Việt Fund', '_raw/company/baovietfund-bvfed-ban-cao-bach-2018-11.pdf'],
    
    ['UC-028', 'Back Office', 'Performance & Risk Management', 'Cảnh báo rủi ro danh mục và quản lý hạn mức nội bộ', 'CATALOGUE',
     'Đọc dữ liệu danh mục đầu tư hiện tại và các hạn mức quy định nội bộ/TT98.',
     'Trích xuất các vị thế lớn, loại tài sản, thanh khoản.',
     'Tính toán tỷ trọng tài sản thực tế và mô phỏng VaR.',
     'So sánh tỷ trọng thực tế với hạn mức nội bộ và luật.',
     'Quyết định gửi cảnh báo nếu chạm ngưỡng rủi ro (VD: > 90% hạn mức).',
     'Tạo tin nhắn/email cảnh báo gửi bộ phận đầu tư.',
     'Gửi thông báo qua hệ thống nội bộ/email.',
     '5', 'Giảm thiểu rủi ro vi phạm pháp luật và thiệt hại uy tín, giá trị cực cao.',
     '4', 'Đòi hỏi dữ liệu realtime hoặc EOD chính xác.',
     '4', 'Danh mục được chốt EOD, hạn mức là tĩnh, dữ liệu khá sạch.',
     '5', 'Cảnh báo sai/sót có thể dẫn đến phạt nặng từ UBCKNN như vụ MB Capital.',
     '4.5', 'Quick win',
     'REG', 'S-REG-TT99', 'Thông tư 99/2020/TT-BTC', '_raw/legal/thuvienphapluat-TT99-2020.md'],
    
    ['UC-029', 'Back Office', 'Performance & Risk Management', 'Báo cáo quản trị rủi ro tự động', 'CATALOGUE',
     'Đọc sổ tay rủi ro, kết quả cảnh báo và danh mục.',
     'Lấy các vi phạm hoặc cảnh báo trong kỳ.',
     'Phân tích xu hướng rủi ro thanh khoản, rủi ro thị trường.',
     '',
     '',
     'Điền các thông số vào biểu mẫu báo cáo quản trị rủi ro theo TT99.',
     '',
     '4', 'Giảm tải khối lượng làm báo cáo định kỳ cho bộ phận QTRR.',
     '4', 'Biểu mẫu TT99 khá rõ ràng, thông số chủ yếu là định lượng.',
     '3', 'Cần tổng hợp cả đánh giá định tính và định lượng từ nhiều nguồn.',
     '3', 'Báo cáo cần được kiểm duyệt trước khi nộp UBCKNN, ít rủi ro tự động hóa ngay.',
     '3.6', 'Chiến lược',
     'REG', 'S-REG-TT99', 'Thông tư 99/2020/TT-BTC', '_raw/legal/thuvienphapluat-TT99-2020.md']
]

ucs.extend(new_ucs)

with open('_data/usecase_registry.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(ucs)
