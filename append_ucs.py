import csv

new_ucs = [
    [
        'UC-027', 'T-BO-054', 'Performance & Risk Management', 'Theo dõi hiệu quả danh mục đầu tư so với Benchmark', 
        '2-Tổng hợp & phân tích', 'RPA + AI', 
        'Cần tính toán nhanh các chỉ số phức tạp (Sharpe, Tracking error) mỗi ngày để PM có chiến lược tái cơ cấu.', 
        '1. Lấy NAV & Index. 2. Làm sạch data. 3. Áp dụng công thức tài chính. 4. Đưa vào báo cáo.', 
        'Bước 2, 3: AI tự động làm sạch dữ liệu chuỗi thời gian, điền ngày nghỉ lễ và tính toán tự động các chỉ số tài chính dựa trên công thức cấu hình sẵn.', 
        'PM kiểm tra lại các điểm dữ liệu bất thường (outliers) trước khi dùng báo cáo.', 
        'Dữ liệu NAV, Index HNX/VNIndex', 'Bản cáo bạch quỹ, TT98', 'Tiết kiệm thời gian tính toán', 
        'CATALOGUE', 'S-DOC-BVFED', '_raw/company/baovietfund-bvfed-ban-cao-bach-2018-11.pdf', 'Chưa có thông tin thời gian xử lý thủ công', 'Y',
        '4', '5', '4', '4', '4.25', 'Quick win', 
        'Tự động tính toán các chỉ số performance giúp PM nắm bắt nhanh hiệu quả | Công thức chuẩn toán học, dữ liệu số rõ ràng dễ tính bằng code/AI | Dữ liệu NAV và index sẵn có, nhưng cần chuẩn hóa đồng bộ thời gian | Rủi ro tính sai công thức dẫn đến báo cáo sai lệch.'
    ],
    [
        'UC-028', 'T-BO-055', 'Performance & Risk Management', 'Cảnh báo rủi ro danh mục và quản lý hạn mức nội bộ', 
        '2-Tổng hợp & phân tích', 'RPA + AI', 
        'Quỹ vượt hạn mức đầu tư (VD vụ MB Capital) sẽ dẫn đến việc bị thanh tra UBCKNN xử phạt hành chính và mất uy tín.', 
        '1. Đọc dữ liệu EOD. 2. Kiểm tra các hạn mức TT98, nội bộ. 3. Ghi nhận vi phạm. 4. Gửi email.', 
        'Bước 2, 3, 4: Hệ thống tự động so khớp tỷ trọng tài sản thực tế với hạn mức, kích hoạt email cảnh báo đỏ nếu >90% mức trần.', 
        'Chuyên viên rủi ro đưa ra quyết định xử lý (mua/bán) khi nhận được cảnh báo.', 
        'Dữ liệu danh mục EOD, Bộ quy tắc hạn mức (Rule engine)', 'TT98/2020/TT-BTC, TT99/2020/TT-BTC', 'Giảm rủi ro phạt vi phạm', 
        'CATALOGUE', 'S-REG-TT99', '_raw/legal/thuvienphapluat-TT99-2020.md', 'Cần phỏng vấn hệ thống lõi có support cảnh báo chưa', 'Y',
        '5', '4', '4', '5', '4.50', 'Quick win', 
        'Giảm thiểu triệt để rủi ro vi phạm pháp luật và thiệt hại uy tín, giá trị cực cao | Đòi hỏi dữ liệu realtime hoặc EOD chính xác | Danh mục được chốt EOD, hạn mức là tĩnh, dữ liệu khá sạch | Cảnh báo sai/sót có thể dẫn đến phạt nặng từ UBCKNN như vụ MB Capital.'
    ],
    [
        'UC-029', 'T-BO-056', 'Performance & Risk Management', 'Báo cáo quản trị rủi ro tự động', 
        '4-Sinh nội dung', 'AI Agent', 
        'Báo cáo định kỳ tốn nhiều thời gian chắp vá số liệu từ nhiều bộ phận, dễ xảy ra sai sót khi nhập liệu.', 
        '1. Thu thập dữ liệu rủi ro kỳ này. 2. Soạn báo cáo Word theo mẫu. 3. Trình phê duyệt.', 
        'Bước 2: AI tự động điền các thông số định lượng vào biểu mẫu chuẩn theo TT99 và sinh các câu nhận xét định tính cơ bản.', 
        'Trưởng bộ phận rủi ro duyệt báo cáo và chỉnh sửa văn phong.', 
        'Dữ liệu cảnh báo, Log vi phạm', 'TT99/2020/TT-BTC', 'Thời gian hoàn thành báo cáo', 
        'CATALOGUE', 'S-REG-TT99', '_raw/legal/thuvienphapluat-TT99-2020.md', 'Chưa rõ tần suất làm báo cáo của quỹ', 'Y',
        '4', '4', '3', '3', '3.60', 'Chiến lược', 
        'Giảm tải khối lượng làm báo cáo định kỳ cho bộ phận QTRR | Biểu mẫu TT99 khá rõ ràng, thông số chủ yếu là định lượng | Cần tổng hợp cả đánh giá định tính và định lượng từ nhiều nguồn | Báo cáo cần được kiểm duyệt trước khi nộp UBCKNN, ít rủi ro tự động hóa ngay.'
    ]
]

with open('_data/usecase_registry.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(new_ucs)
