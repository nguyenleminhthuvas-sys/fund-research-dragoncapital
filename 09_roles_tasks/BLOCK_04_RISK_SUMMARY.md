# TỔNG KẾT KHỐI 4 - PERFORMANCE & RISK MANAGEMENT (BACK OFFICE)

> Bản này thay thế bản cũ — bản cũ mô tả một phiên bản đã lỗi thời của T-BO-058→067 và
> UC-030→033 (đã bị xoá vì hỏng schema, xem CHANGELOG.md 2026-08-16). Nội dung dưới đây
> ghi lại đúng dữ liệu hiện hành trong `task_registry.csv` và `usecase_registry.csv`.

## 1. Thống kê dữ liệu
- **Tổng số tác vụ cấp 3 đã xác định:** 33 tác vụ (T-BO-054 đến T-BO-087). T-BO-057 (kiểm soát
  sử dụng tài sản ủy thác) không tính vào khối này — hiện thuộc khối Transfer Agency & Nhà đầu tư.
- **Phân loại vận hành/quản trị:** 22 tác vụ **Vận hành**, 11 tác vụ **Quản trị** (T-BO-062, 063,
  064, 065, 067, 068, 069, 071, 072, 077, 082 — nghĩa vụ tổ chức/thẩm quyền một lần từ
  QĐ 428/QĐ-UBCK, không phải nền để sinh use case).
- **Phân bố nhãn độ tin cậy:** `REG` (nghĩa vụ pháp lý) 32 tác vụ, `FACT` 1 tác vụ. Không có tác
  vụ nào gắn `INFERENCE` trong khối này.
- **Số lượng pain point đã xác minh:** **1** (T-BO-056 — "Chậm trễ trong việc tổng hợp dữ liệu
  rủi ro từ nhiều nguồn khác nhau để làm báo cáo").
- **Số lượng cần phỏng vấn:** 33/33 tác vụ.

## 2. Danh sách nguồn đã sử dụng
- **Tier 1 (Pháp lý):** Quyết định 428/QĐ-UBCK — Quy chế hướng dẫn thiết lập, vận hành hệ thống
  quản trị rủi ro (2013), nguồn chính của 30/33 tác vụ; Thông tư 99/2020/TT-BTC (T-BO-055, 056).
- **Tier 2:** Bản cáo bạch Quỹ Đầu tư Cổ phiếu Năng động Bảo Việt (BVFED) — T-BO-054.

**Lưu ý xác minh:** 2 `source_id` đang dùng trong `task_registry.csv` cho khối này —
`S-DOC-BVFED` (T-BO-054) và `S-REG-TT99` (T-BO-055, T-BO-056) — **không tồn tại trong
SOURCE_REGISTRY.csv**. `raw_ref` của các dòng này vẫn trỏ tới file có thật
(`_raw/company/baovietfund-bvfed-ban-cao-bach-2018-11.pdf`,
`_raw/legal/thuvienphapluat-TT99-2020.md`), nhưng mã `source_id` cần đăng ký lại trong registry
trước khi coi các dòng này là "đã kiểm chứng nguồn" theo LUẬT KIỂM NGUỒN (mục 3.10
`00_control/GLOBAL_RULES.md`). Riêng `S-REG-QD428` (30/33 tác vụ) đã đăng ký đúng, trạng thái
ĐANG DÙNG.

## 3. Use case đã sinh (16 use case)
- **Quick win** (tổng điểm ≥ 3.8): UC-027, UC-028, UC-040, UC-043 (4 use case).
- **Chiến lược** (3.0–3.79): UC-029, UC-035, UC-036, UC-037, UC-038, UC-039, UC-041, UC-042,
  UC-045, UC-046 (10 use case).
- **Nghiên cứu** (< 3.0): UC-034, UC-044 (2 use case).
- 11/33 tác vụ (nhóm Quản trị) không sinh use case — lý do cụ thể từng tác vụ ghi tại
  `10_usecases/REJECTED.csv` (thẩm quyền HĐQT, quyết định nhân sự một lần, hoặc điều khoản dẫn
  chiếu Thông tư 212/2012/TT-BTC).

## 4. Khoảng trống trung thực (Gap Analysis)
- **Chưa có tài liệu T1 nào của Dragon Capital (DCVFM)** riêng cho công tác quản trị rủi ro —
  toàn bộ nghĩa vụ pháp lý trích từ văn bản chung (QĐ 428, TT99), áp dụng cho mọi công ty quản
  lý quỹ tại VN, chưa xác nhận DCVFM triển khai đúng như văn bản mô tả.
- **32/33 tác vụ chưa có pain point thực tế xác minh** (chỉ T-BO-056 có) — nguồn hiện tại là văn
  bản quy định "phải làm gì", không mô tả "khó ở đâu"; cần phỏng vấn để lấp.
- **2 source_id lệch chuẩn** (`S-DOC-BVFED`, `S-REG-TT99`) cần đăng ký lại trong
  SOURCE_REGISTRY.csv trước khi coi các dòng T-BO-054/055/056 là đã kiểm chứng đầy đủ.

## 5. Hành động cần bổ sung sau
- Đăng ký lại 2 source_id lệch chuẩn (`S-DOC-BVFED` → hợp nhất vào `S-BVFED-001` đã có sẵn;
  `S-REG-TT99` → đăng ký mã T1 mới cho Thông tư 99/2020/TT-BTC) trong SOURCE_REGISTRY.csv.
- Phỏng vấn bộ phận Quản trị rủi ro DCVFM theo 32 tác vụ còn thiếu pain point (bộ câu hỏi tham
  khảo: `09_roles_tasks/INTERVIEW_GUIDE_RISK.md`).
- Xác nhận công ty có/không có tiểu ban quản trị rủi ro (liên quan T-BO-064, T-BO-067) để biết
  2 tác vụ này có áp dụng trong thực tế hay không.

## HANDOFF
- Trạng thái: READY_FOR_AUDIT
