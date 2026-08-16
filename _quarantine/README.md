# CÁCH LY — KHÔNG DÙNG

**Ngày cách ly:** 2026-08-16

**Vì sao:** Dữ liệu sinh bằng template (range()+f-string kiểu "Thu thập dữ liệu
cho X / Phân tích và đánh giá X / Lập báo cáo X / Trình duyệt phê duyệt X /
Lưu trữ hồ sơ X"), `source_id` trích dẫn không tồn tại trong
`_data/SOURCE_REGISTRY.csv` hoặc bị gán nhầm sang nguồn không liên quan nội
dung — phát hiện qua đợt kiểm chất lượng 6 artifact ngày 2026-08-16 (xem
`CHANGELOG.md`).

**CẢNH BÁO:** Không được đọc, trích, hay tích hợp bất kỳ file nào trong thư
mục này vào bất kỳ artifact nào (báo cáo, use case, task registry…). Giữ lại
chỉ để truy vết lịch sử lỗi.

## Danh sách file bị cách ly và bằng chứng cụ thể

- `GLOBAL_MAP.md` (từ `02_industry_global/`) — 48 nhãn FACT/DATA/INFERENCE
  trích 5 source_id (S-T1-004, S-T1-005, S-T2-001, S-T2-006, S-T2-008);
  **0/5 tồn tại** trong SOURCE_REGISTRY.csv; `_raw/` không có file nào về
  ngành quản lý quỹ toàn cầu (BlackRock, ICI, BCG…) để đối chiếu.
- `VN_MAP.md` (từ `03_industry_vn/`) — trích S-T3-003 và S-T3-004. S-T3-004
  không tồn tại trong registry. S-T3-003 tồn tại nhưng thực chất là trang
  chủ vendor phần mềm "InvestCloud" (tiếng Anh, trạng thái CHƯA KHAI THÁC)
  — không liên quan gì tới số liệu AUM/số quỹ Việt Nam đang được trích
  (source_id bị gán nhầm).
- `SEGMENTATION_MATRIX.md` (từ `04_segmentation/`) — trích 11 source_id
  (S-T1-001/002/004/005/008/010/100/101/102, S-T3-003, S-T3-100); 0/11 tồn
  tại đúng nghĩa trong registry (S-T3-003 bị gán nhầm như trên).
- `VALUE_CHAIN.md` (từ `06_value_chain/`) — 300/300 dòng gắn nhãn [FACT]
  nhưng khớp 100% một trong 5 mẫu câu cố định lặp lại đúng 60 lần mỗi mẫu
  (`grep -c` xác nhận 60/60/60/60/60); toàn bộ chỉ trích 2 source_id
  (S-T1-004 × 225, S-T1-003 × 75), cả hai đều không tồn tại trong registry.
- `processes/` (từ `06_value_chain/processes/`, 60 file) — cùng bệnh với
  VALUE_CHAIN.md: 7/9 trường mỗi task card (Trigger, Input/Output, Vai trò,
  Hệ thống, Tần suất, Điểm gãy, Khác biệt phân khúc) là **1 câu chữ y hệt
  nhau tuyệt đối trên cả 60 file** (`grep | sort -u` ra đúng 1 dòng mỗi
  trường); chỉ tiêu đề và "Các bước" khác nhau (và "Các bước" cũng chỉ là
  template chèn tên task). 100% dùng chung source_id S-T1-004 — không tồn
  tại trong registry. Dung lượng trung bình 1.438 byte, biên độ hẹp
  1.312–1.549 byte — dấu hiệu template hoá cơ học. File nhỏ nhất
  `MO_2_3.md`, lớn nhất `BO_2_4.md`.
