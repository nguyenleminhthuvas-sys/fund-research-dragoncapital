import csv
import os
import shutil

context_map = {
    "UC-001": "Tác vụ này được thực hiện hàng ngày bởi Bộ phận Định giá (Fund Accounting) để thu thập giá đóng cửa của tất cả các cổ phiếu trong danh mục quỹ từ hai sở giao dịch HOSE và HNX. Căn cứ theo Bản cáo bạch quỹ BVFED (trang 72), giá chứng khoán niêm yết được tính bằng giá đóng cửa hoặc giá tham chiếu của ngày giao dịch gần nhất. Việc thực hiện thủ công bằng mắt sẽ rủi ro và mất nhiều thời gian, đặc biệt khi quy mô danh mục lên tới hàng chục mã chứng khoán.",
    "UC-003": "Nhân viên Đại lý phân phối và Đại lý chuyển nhượng phải nhận, rà soát và nhập liệu phiếu lệnh chứng chỉ quỹ (mua/bán/chuyển đổi) do khách hàng nộp tại quầy hoặc scan qua email. Dựa vào quy định tại Thông tư 98/2020/TT-BTC, lệnh phải được tiếp nhận và xử lý trước giờ cut-off (14h45) của ngày giao dịch, nếu chậm trễ sẽ bị hủy hoặc chuyển sang ngày T+1. Quy trình này đòi hỏi tính chính xác tuyệt đối để không ảnh hưởng đến số dư của nhà đầu tư.",
    "UC-020": "Dựa trên bài học từ quyết định xử phạt cảnh cáo của VSD (Trung tâm Lưu ký) đối với 4 công ty chứng khoán/quản lý quỹ vì nộp chậm xác nhận danh sách cổ đông, tác vụ này yêu cầu nhân viên Settlement phải đối soát chính xác danh sách chốt quyền do VSDC gửi về với sổ cổ đông nội bộ. Áp lực thời gian và khối lượng dữ liệu khổng lồ trong những đợt trả cổ tức hoặc đại hội cổ đông khiến việc so khớp thủ công dễ sinh ra sai sót nghiêm trọng.",
    "UC-023": "Mô tả trong Thông tư 98 yêu cầu Đại lý chuyển nhượng phải thu thập, phân loại và nhập liệu hàng trăm phiếu lệnh được gửi dồn dập từ các Đại lý phân phối qua fax hoặc email trước giờ đóng sổ. Chuyên viên Back Office đóng vai trò rà soát định danh, xác nhận chữ ký và số lượng đăng ký mua. Đây là một quy trình cực kỳ nhạy cảm với thời gian (time-critical).",
    "UC-009": "Nhân sự bộ phận Kế toán và Tuân thủ phải đối mặt với quy định bắt buộc của Bộ Tài chính: nộp báo cáo định kỳ về an toàn tài chính và quản trị rủi ro. Bài học thực tiễn từ vụ 2 công ty quản lý quỹ bị UBCKNN phạt nặng do trễ hạn báo cáo cho thấy khối lượng công việc tổng hợp số liệu để ra báo cáo là rào cản lớn. Tác vụ này cần sự giám sát trực tiếp của Giám đốc quỹ trước khi trình lên UBCKNN.",
    "UC-016": "Tham chiếu từ JD Kế toán Quỹ (Jobed.ai) và Bản cáo bạch quỹ, Kế toán Quỹ phải nhận sổ phụ ngân hàng từ Ngân hàng giám sát hàng ngày (thường là bản PDF quét hoặc excel chưa chuẩn hóa). Mục tiêu của công việc này là hạch toán và so khớp từng khoản tiền ra vào (tiền nhận mua CCQ, phí quản lý, lãi tiền gửi) nhằm chốt NAV nội bộ. Công việc tốn nhiều mắt nhìn để kiểm tra chéo từng dòng số dư.",
    "UC-024": "Để tuân thủ nghiêm ngặt Luật Phòng chống rửa tiền (PCRT 2022) và Thông tư 27/2025/TT-NHNN, khi mở tài khoản trực tiếp, nhân viên Đại lý phân phối phải lưu lại bản sao hoặc ảnh chụp CCCD/CMND của nhà đầu tư. Sau đó nhân viên gõ lại thông tin định danh vào phần mềm. Sai sót ở khâu này làm sai lệch định danh (eKYC) và dẫn tới vi phạm trong rà soát danh sách đen về sau.",
    "UC-014": "Được mô tả rất rõ trong các Mẫu JD Kế toán quỹ quốc tế (như VelvetJobs), nhân viên Fund Accounting phải thực hiện đối soát số dư và sổ cái (reconciliation) với bên cung cấp dịch vụ quản trị quỹ (Fund Administrator) như GlobeOp/SS&C. Hai bên thường dùng hai hệ thống ERP khác nhau nên định dạng file trả về không khớp nhau, khiến việc Vlookup hoặc dùng Excel trở nên mệt mỏi và dễ lỗi.",
    "UC-018": "Theo Quy chế hoạt động bù trừ thanh toán giao dịch chứng khoán (Quyết định 39/QĐ-HĐTV của VSDC), vào cuối mỗi ngày giao dịch, VSDC sẽ trả về thông báo kết quả giao dịch tạm tính. Nhân viên Settlement (Thanh toán bù trừ) phải đối chiếu chi tiết bảng này với sổ lệnh nội bộ để tìm ra các giao dịch bị loại bỏ, sai số lượng hoặc bị lùi thời hạn thanh toán do thiếu tiền/chứng khoán.",
    "UC-004": "Dựa trên quy định về mở tài khoản tại Bản cáo bạch, quá trình mở tài khoản và thay đổi thông tin nhà đầu tư yêu cầu một loạt các \"Giấy đề nghị giao dịch\" bằng văn bản cứng. Nhà đầu tư điền tay, nhân viên quầy kiểm tra và bộ phận Transfer Agency phải đánh máy lại toàn bộ số tài khoản ngân hàng, địa chỉ, thông tin FATCA vào hệ thống. Lỗi gõ sai một ký tự trong số tài khoản có thể dẫn tới tiền mua CCQ bị thất lạc."
}

# 1. Clear old deep_dives
if os.path.exists("12_deep_dives"):
    shutil.rmtree("12_deep_dives")
os.makedirs("12_deep_dives", exist_ok=True)

# 2. Get Top 10
uc_rows = []
with open("_data/usecase_registry.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        uc_rows.append(row)

uc_rows.sort(key=lambda x: float(x.get("tong_diem", 0)), reverse=True)
top_10 = uc_rows[:10]

# 3. Write new files
for i, uc in enumerate(top_10):
    uc_id = uc["uc_id"]
    ctx = context_map.get(uc_id, "Thông tin bối cảnh dựa trên tham chiếu nội bộ gốc.")
    
    content = f"""# {uc_id}: {uc["ten_use_case"]}

## 1. Bối cảnh nghiệp vụ
{ctx}
- **Khối chức năng**: {uc["khoi_chuc_nang"]}
- **Tham chiếu gốc (Raw Ref)**: `{uc["raw_ref"]}`

## 2. Quy trình hiện tại theo bước
{uc["quy_trinh_hien_tai_theo_buoc"]}

## 3. Thiết kế giải pháp (AI Intervention)
- **Công nghệ**: {uc["ai_type"]} ({uc["nang_luc_ai"]})
- **Điểm can thiệp**: {uc["ai_lam_gi_o_buoc_nao"]}

## 4. Dữ liệu cần có
- {uc["du_lieu_can_co"]}

## 5. Human-in-the-Loop
- {uc["human_in_the_loop"]}

## 6. Ràng buộc pháp lý
- {uc["rang_buoc_phap_ly"]}

## 7. KPI đo lường
- {uc["kpi_cai_thien"]} (Mục tiêu: cải thiện thời gian/chất lượng, không ấn định % khi chưa có baseline thực tế)

## 8. Những gì còn thiếu để triển khai được
- {uc["ghi_chu_thieu"]}
"""
    with open(f"12_deep_dives/{uc_id}.md", "w", encoding="utf-8") as f:
        f.write(content)

print("Việc 2 hoàn tất (Viết lại Deep Dive).")
