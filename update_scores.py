import csv
import json
import os

scores_map = {
    "UC-001": [4, 5, 5, 2, "Lấy giá đóng cửa HOSE/HNX phải làm hàng ngày, sai sót ảnh hưởng trực tiếp NAV | Cấu trúc website bảng giá cố định, dễ dàng dùng RPA/Crawler trích xuất không cần train model | Dữ liệu public trên sàn chứng khoán, dễ dàng lấy bằng API | Sai sót dẫn đến định giá sai chứng chỉ quỹ, ảnh hưởng quyền lợi NĐT nên rủi ro cao."],
    "UC-002": [4, 2, 3, 2, "Tác vụ định giá trái phiếu hàng ngày theo TT98, tiết kiệm thời gian nội suy | Yêu cầu mô hình định lượng phức tạp (ví dụ cubic spline) thay vì chỉ đọc văn bản | Dữ liệu VBMA thường yêu cầu tài khoản trả phí để lấy API/File chuẩn | Định giá sai tài sản quỹ ảnh hưởng NAV báo cáo giám sát."],
    "UC-003": [5, 4, 4, 3, "Xử lý hàng trăm lệnh mua bán CCQ trước giờ cut-off 14h45, trễ là bị hủy | Form phiếu lệnh do công ty phát hành có cấu trúc cố định, OCR template chạy rất tốt | Nguồn file scan nội bộ từ đại lý hoặc quầy dễ tiếp cận | Nhân sự vẫn phải duyệt lại lệnh trên phần mềm trước khi khớp nên rủi ro được kiểm soát."],
    "UC-004": [4, 4, 4, 3, "Nhập liệu thủ công Giấy đề nghị giao dịch dễ sai số tài khoản NĐT | Form đề nghị cố định, công nghệ OCR dễ dàng trích xuất text in | File scan lưu sẵn trên hệ thống văn thư nội bộ | Lỗi số tài khoản có thể gây chuyển nhầm tiền nhưng có bước check tên khớp số TK."],
    "UC-005": [2, 5, 4, 4, "Việc gửi thông báo khớp lệnh có thể tự động hóa bằng mail merge thông thường, ít cần AI sâu | LLM sinh text từ biến dữ liệu (tên, số tiền) cực kỳ đơn giản | Dữ liệu giao dịch khớp lệnh có sẵn trên Core system | Lỗi câu từ chủ yếu ảnh hưởng trải nghiệm khách hàng, không ảnh hưởng tài chính."],
    "UC-006": [3, 4, 4, 2, "Tiết kiệm công sức kế toán phải tự nhớ mã tài khoản cho hàng trăm bút toán | Dùng thuật toán phân loại văn bản (NLP) để map diễn giải vào mã tài khoản khá khả thi | Dữ liệu lịch sử hạch toán có sẵn dồi dào trong ERP để huấn luyện | Sai mã tài khoản dẫn đến sai lệch BCTC quỹ nên cần đối soát chặt chẽ."],
    "UC-007": [3, 3, 2, 2, "Giảm tải áp lực tìm kiếm chứng từ giải trình vào mỗi kỳ kiểm toán quỹ | Xây dựng hệ thống RAG trên hàng ngàn file PDF scan chứng từ đòi hỏi indexing rất phức tạp | Dữ liệu hóa đơn, hợp đồng thường nằm rải rác ở nhiều thư mục, chưa chuẩn hóa | Cung cấp sai số liệu cho kiểm toán viên có thể dẫn đến rủi ro đình chỉ BCTC."],
    "UC-008": [4, 2, 2, 5, "Nâng cao năng lực giám sát gian lận/lỗi quy trình từ hàng ngàn lệnh giao dịch qua Đại lý | Mô hình phát hiện bất thường (Anomaly Detection) dễ báo động giả (false positive) cần tinh chỉnh nhiều | Phải tích hợp dữ liệu log từ hệ thống của bên thứ ba (Đại lý chuyển nhượng) | AI chỉ đưa ra cảnh báo cho Tuân thủ viên, không tự động chặn lệnh nên rủi ro thấp."],
    "UC-009": [5, 4, 4, 2, "Trực tiếp giải quyết nguy cơ bị phạt do nộp chậm báo cáo cho UBCKNN | Biểu mẫu UBCK có cấu trúc cố định, dùng RPA kết hợp LLM sinh giải trình rất phù hợp | Data lấy trực tiếp từ hệ thống Core Kế toán nội bộ | Nộp sai số liệu cho cơ quan quản lý sẽ chịu chế tài pháp lý nghiêm trọng."],
    "UC-010": [2, 4, 4, 5, "Tác vụ phân tích quản trị tần suất thấp (theo tháng), chỉ phục vụ Ban giám đốc đọc nhanh | LLM hiện nay tóm tắt và sinh nhận xét từ bảng số liệu rất xuất sắc | Dữ liệu quản trị nội bộ đã được số hóa gọn gàng trên phần mềm | Hoàn toàn lưu hành nội bộ, không rủi ro pháp lý hay thiệt hại tài chính."],
    "UC-011": [3, 4, 3, 3, "Tự động hóa bản tin tháng giúp tiết kiệm công sức tổng hợp tin tức thị trường gửi NĐT | Việc kết hợp số liệu NAV và tin thị trường để sinh bài viết là thế mạnh của GenAI | Yêu cầu crawl thêm tin tức kinh tế vĩ mô từ các trang báo bên ngoài | Bản tin gửi ra đại chúng nếu sai sót thông tin sẽ ảnh hưởng uy tín quỹ."],
    "UC-012": [2, 5, 4, 4, "Chỉ là tiện ích nháp email đốc thúc kiểm toán, luật sư, không tạo giá trị đột phá | Tích hợp AI vào email (như Copilot cho Outlook) là tính năng có sẵn, dễ dùng | Dữ liệu chỉ xoay quanh hòm thư cá nhân của nhân sự vận hành | Chuyên viên luôn tự đọc lại email trước khi bấm Gửi nên rất an toàn."],
    "UC-013": [4, 2, 2, 1, "Tối ưu hóa khối lượng đặt lệnh giúp giảm trượt giá, bảo vệ lợi nhuận của Quỹ | Phải xây dựng mô hình thuật toán tối ưu hóa (slippage model) thay vì AI tạo sinh đơn thuần | Yêu cầu dữ liệu order book độ trễ thấp (realtime) từ HOSE/HNX rất tốn kém | Đặt lệnh sai khối lượng gây thiệt hại tài chính trực tiếp và ngay lập tức."],
    "UC-014": [4, 4, 3, 5, "Đối chiếu hàng ngàn dòng file của Fund Administrator bằng mắt rất mệt mỏi | Việc map các cột khác tên và tìm dòng chênh lệch bằng script rất khả thi và chính xác | File dữ liệu phụ thuộc vào định dạng xuất của đối tác Fund Administrator | Đây là chốt chặn kiểm tra lỗi, AI chỉ highlight nghi vấn nên không gây thêm rủi ro."],
    "UC-015": [3, 3, 2, 3, "Giảm áp lực lục lọi hồ sơ trả lời câu hỏi bất chợt của kiểm toán viên | Việc bóc tách ý nghĩa từ hợp đồng phức tạp bằng RAG có thể bị ảo giác (hallucination) | Kho chứng từ lưu trữ lộn xộn, nhiều file pdf scan mờ, chữ ký chèn lên chữ | Rủi ro trung bình do người dùng luôn kiểm tra lại file gốc trước khi forward."],
    "UC-016": [4, 4, 4, 4, "Nhập liệu sổ phụ ngân hàng PDF thủ công để đóng sổ hằng ngày cực kỳ tốn công | Các thư viện Table OCR hiện tại bóc tách định dạng sao kê ngân hàng rất tốt | File PDF được cung cấp định kỳ trực tiếp từ Ngân hàng giám sát | Chỉ dùng để đối chiếu khớp số dư ERP, chuyên viên kiểm tra lệnh lệch nên an toàn."],
    "UC-017": [5, 4, 3, 2, "Cảnh báo chặn lệnh vượt rào, ngăn chặn trực tiếp rủi ro bị UBCK phạt như vụ MB Capital | Thuật toán tính tỷ lệ trần/sàn theo Luật là logic toán học rõ ràng, dễ lập trình | Cần liên kết realtime với Core giao dịch để chặn lệnh trước khi đẩy lên sàn | Bỏ sót vi phạm sẽ dẫn đến biên bản xử phạt hành chính nặng."],
    "UC-018": [3, 5, 4, 4, "Giảm tải việc dò bằng mắt giữa bảng kê VSDC và sổ lệnh ERP nội bộ cuối ngày | File kết quả VSDC có cấu trúc cột chuẩn, dùng script đối chiếu dễ hơn dùng AI | File được tải trực tiếp từ cổng giao tiếp điện tử của VSDC | Mục đích là tra soát tìm lỗi, nhân viên vẫn là người quyết định xử lý chênh lệch."],
    "UC-019": [2, 2, 2, 2, "Tình huống thiếu tiền thanh toán bù trừ rất ít khi phát sinh trong quỹ lớn | Xây dựng mô hình tối ưu hóa chi phí vay vốn khá phức tạp so với tần suất sử dụng | Cần dữ liệu lãi suất vay liên ngân hàng biến động liên tục | Gợi ý vay sai nguồn làm quỹ phải chịu chi phí lãi vay cao hơn mức cần thiết."],
    "UC-020": [5, 4, 4, 3, "Xử lý trực tiếp rủi ro bị VSDC ra văn bản cảnh cáo do chậm chốt danh sách cổ đông | Bóc tách và so khớp danh sách chốt quyền VSDC với Core nội bộ là bài toán OCR/RPA cơ bản | File danh sách được VSDC gửi sẵn, chỉ cần tải về xử lý | Kế toán viên kiểm tra lại các dòng cảnh báo lệnh khớp tên trước khi ký xác nhận."],
    "UC-021": [3, 5, 4, 2, "Tiết kiệm thời gian tự gõ tay các hợp đồng chuyển nhượng chứng khoán OTC dài dòng | Dùng LLM hoặc template engine điền thông tin định danh vào form hợp đồng vô cùng dễ | Dữ liệu căn cước của 2 bên mua/bán đã có sẵn trên hệ thống quản lý cổ đông | Lỗi sai số lượng hoặc giá trị trên hợp đồng sẽ dẫn tới tranh chấp pháp lý phức tạp."],
    "UC-022": [3, 2, 2, 1, "Xử lý các lệnh phong tỏa tài khoản mang tính khẩn cấp để chống tẩu tán tài sản | Công văn của tòa án/công an thường scan mờ, có dấu đỏ đè lên chữ khiến OCR hay đọc sai | Đầu vào là văn bản giấy do cán bộ mang tới, tính chuẩn hóa dữ liệu rất kém | Khóa nhầm tài khoản bị khách hàng kiện, khóa chậm bị cơ quan điều tra kỷ luật."],
    "UC-023": [5, 4, 4, 3, "Giải quyết tắc nghẽn khi hàng trăm lệnh từ các Đại lý phân phối đổ về gần giờ cut-off | Phiếu lệnh theo form thống nhất của công ty quản lý quỹ, OCR bóc tách độ tin cậy cao | Tự động lấy file đính kèm từ email của Đại lý phân phối rất thuận lợi | Sai sót lệnh mua CCQ ảnh hưởng NAV nhưng có chuyên viên duyệt lệnh cuối cùng."],
    "UC-024": [4, 5, 4, 2, "Rút ngắn thời gian gõ tay thông tin CCCD khi nhà đầu tư mở tài khoản chứng chỉ quỹ trực tiếp | Công nghệ eKYC và OCR căn cước công dân đã cực kỳ hoàn thiện, có sẵn API thương mại | Ảnh chụp giấy tờ do khách hàng tự cung cấp có thể bị chói lóa cần tiền xử lý | Sai sót xác thực nhân thân dẫn đến rủi ro rửa tiền, vi phạm Luật PCRT."],
    "UC-025": [5, 3, 3, 2, "Chặn đứng rủi ro bị phạt 40 triệu đồng do không rà soát khách hàng theo Nghị định 156 | So khớp mờ (Fuzzy logic) tên tiếng Việt không dấu với danh sách đen quốc tế khá hóc búa | Phải liên tục cập nhật danh sách đen (UN, OFAC) từ các nguồn bên ngoài | Bỏ lọt đối tượng khủng bố/rửa tiền sẽ khiến công ty bị thu hồi giấy phép."],
    "UC-026": [5, 3, 4, 2, "Trực tiếp giải quyết nguy cơ bị phạt 400 triệu đồng do không nộp báo cáo rủi ro AML | Việc tổng hợp hàng ngàn giao dịch đáng ngờ thành báo cáo định kỳ yêu cầu data pipeline tốt | Dữ liệu cảnh báo rửa tiền đã được lưu trữ sẵn trong hệ thống quản lý rủi ro | Báo cáo gửi lên Ngân hàng Nhà nước, sai số liệu sẽ bị thanh tra toàn diện."]
}

# Read existing csv
with open("_data/usecase_registry.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

# Map header indexes
idx = {h: i for i, h in enumerate(header)}

new_rows = []
for row in rows:
    uc_id = row[idx["uc_id"]]
    if uc_id in scores_map:
        sc = scores_map[uc_id]
        gia_tri = sc[0]
        kha_thi = sc[1]
        du_lieu = sc[2]
        rui_ro = sc[3]
        ly_do = sc[4]
        
        row[idx["diem_gia_tri"]] = str(gia_tri)
        row[idx["diem_kha_thi"]] = str(kha_thi)
        row[idx["diem_du_lieu"]] = str(du_lieu)
        row[idx["diem_rui_ro"]] = str(rui_ro)
        row[idx["ly_do_cham"]] = ly_do
        
        # tong_diem = gia_tri*0.35 + kha_thi*0.25 + du_lieu*0.25 + rui_ro*0.15
        tong = (gia_tri * 0.35) + (kha_thi * 0.25) + (du_lieu * 0.25) + (rui_ro * 0.15)
        row[idx["tong_diem"]] = f"{tong:.2f}"
        
        if tong >= 3.8:
            ro = "Quick win"
        elif tong >= 3.0:
            ro = "Chiến lược"
        else:
            ro = "Nghiên cứu"
        row[idx["ro"]] = ro
        
    new_rows.append(row)

with open("_data/usecase_registry.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(new_rows)
