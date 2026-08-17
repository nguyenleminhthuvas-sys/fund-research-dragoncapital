# LOG — Compliance & Regulatory Reporting (Giai đoạn A + B + C)

**Ngày chạy:** 2026-08-17
**Phạm vi:** `00_control/PHASE2_PLAN.md` Mục 2.3 — Compliance & Regulatory Reporting
**Trạng thái:** ĐÃ MERGE vào `_data/task_registry.csv`, `_data/SOURCE_REGISTRY.csv`, `_data/usecase_registry.csv` (17/08/2026, sau khi Claude review toàn bộ + chạy Red Team trên phần mới).

## 0. Cập nhật sau review (Claude, không phải agent nghiên cứu)

- **Đã kiểm chứng chéo 1 trích dẫn với nguyên văn** (T-CO-001, Điều 90 khoản 4) — khớp chính xác từng chữ với `_raw/legal_v2/congbao-luat-chung-khoan-54-2019-vbhn24.md`.
- **Red Team phát hiện 4 dòng trích quá 15 từ** mà agent tự đếm sai (T-CO-005/006/007/008, đều 17 từ) — đã cắt lại đúng ≤15 từ.
- **Giai đoạn C — sinh use case:** tạo 9 use case (UC-047 đến UC-055) từ 11 task, áp đúng công thức chấm điểm đã audit (0,35/0,25/0,25/0,15) và ngưỡng xếp rổ thực tế (≥3,8 Quick win / ≥3,0 Chiến lược). Toàn bộ ở mức `CATALOGUE` (theo quyết định OQ-003 — không làm Giai đoạn E/phỏng vấn).
- **2 task bị loại** (T-CO-002, T-CO-003 — tác vụ thiết kế/tổ chức một lần, không phải quy trình lặp lại) đã ghi vào `10_usecases/REJECTED.csv` kèm lý do, không âm thầm bỏ qua.
- **Quyết định về `tang` (Middle Office vs Back Office):** giữ nguyên `Middle Office` cho 11 task mới (đúng theo AGENT_ROSTER.md phân loại Compliance Officer là vai trò Middle) — cột này không được render trong báo cáo (đã kiểm tra `report_template.html`), nên không ảnh hưởng người đọc. Ghi nhận đây là điểm không nhất quán với 87 dòng cũ (tất cả gán `Back Office`) — không sửa lại 87 dòng cũ vì ngoài phạm vi đợt này.
- **Tier T1 của S-COMP-003** (báo chí dẫn quyết định UBCKNN) — xác nhận khớp tiền lệ đã có trong registry (`S-ENF-005/006` cũng T1 cho báo chí dẫn quyết định chính thức) — giữ nguyên T1.
- **Không cập nhật T-BO-020** với `S-COMP-001` — cân nhắc nhưng để nguyên, đây là việc tùy chọn không bắt buộc.

---

---

## 1. Tóm tắt số liệu đạt được

- **Nguồn mới xác minh:** 5 (`S-COMP-001` đến `S-COMP-005`) — 2 T1 văn bản pháp luật gốc, 1 T1 báo chí dẫn quyết định UBCKNN, 2 T3 tài liệu vendor.
- **Task mới bóc tách:** 11 (`T-CO-001` đến `T-CO-011`) — 8 REG, 2 FACT, 1 INFERENCE.
- **File raw đã lưu:** 5 file trong `_raw/legal_v2/` (tổng ~570KB text).
- Không có trùng `source_id` hay `task_id` với registry gốc (đã kiểm tra bằng script).

## 2. Nguồn tìm được / xác minh được — chi tiết

| source_id | Văn bản | Tier | Cách xác minh |
|---|---|---|---|
| S-COMP-001 | Luật Chứng khoán 54/2019/QH14 (văn bản hợp nhất 24/VBHN-VPQH, cập nhật đến Luật 56/2024/QH15) | T1 | Tải PDF gốc 2 phần từ CDN Công báo Chính phủ (congbaocdn.chinhphu.vn), trích xuất bằng PyMuPDF — có text layer thật, không OCR. 254.682 ký tự. |
| S-COMP-002 | Thông tư 96/2020/TT-BTC (CBTT trên TTCK) | T1 | Tương tự — 2 phần PDF Công báo, 221.196 ký tự. |
| S-COMP-003 | Quyết định 1017/QĐ-XPHC xử phạt HD Capital (9/11/2023) | T1 (báo chí dẫn QĐ) | curl trực tiếp baodautu.vn, đối chiếu chéo với tinnhanhchungkhoan.vn (cùng số tiền/ngày/tên công ty, nhưng bài đó bị JS/paywall khi curl nên không đăng ký nguồn riêng). |
| S-COMP-004 | Confluence Signal (vendor) | T3 | curl trực tiếp, xác nhận nội dung investment monitoring + shareholding disclosure. |
| S-COMP-005 | Bloomberg AIM Compliance (vendor) | T3 | curl trực tiếp, xác nhận nội dung pre-trade/post-trade compliance. |

### Phát hiện quan trọng: các số điều khoản trong `PHASE2_PLAN.md` Mục 1.1 SAI

`PHASE2_PLAN.md` gợi ý verify "Luật CK Điều 97 (báo cáo UBCKNN), Điều 75 (tách biệt tài sản)" và
"TT96 Điều 9, 16-20, 23, 25" và "ND155 Điều 226 (kiểm soát nội bộ), Điều 230 (lịch báo cáo định kỳ),
Điều 240 (vốn khả dụng)". Sau khi đọc nguyên văn xác minh:

- **Luật CK Điều 97** thực tế = "Chứng chỉ hành nghề chứng khoán" — KHÔNG liên quan báo cáo UBCKNN.
- **Luật CK Điều 75** thực tế = "Điều kiện cấp Giấy phép thành lập và hoạt động KDCK" — KHÔNG liên quan tách biệt tài sản.
- Điều khoản ĐÚNG chủ đề thực tế: **Điều 90 khoản 4** (tách biệt tài sản ủy thác), **Điều 107** (báo cáo UBCKNN về quỹ đầu tư), **Điều 118, 123-128** (chương công bố thông tin, gồm cổ đông lớn/người nội bộ).
- **TT96 Điều 9** thực tế = "CBTT về việc đăng ký công ty đại chúng" — không phải CTQLQ. **Điều 16-20** là CBTT của tổ chức niêm yết/phát hành trái phiếu — không phải CTQLQ.
- Điều khoản ĐÚNG chủ đề: **Điều 22-25** (CBTT định kỳ/bất thường của CTCK/CTQLQ), **Điều 26-27** (quỹ đại chúng), **Điều 31** (cổ đông lớn), **Điều 33** (người nội bộ).
- **ND155/2020 KHÔNG có** "Điều 226 = kiểm soát nội bộ", "Điều 230 = lịch báo cáo định kỳ", "Điều 240 = vốn khả dụng" cho công ty quản lý quỹ. Đã tải và đọc toàn văn ND155 (7 phần PDF Công báo, ~1,1 triệu ký tự): Điều 226 thực tế = "Điều kiện, hồ sơ thay đổi thời hạn hoạt động quỹ thành viên"; Điều 230 = "Trình tự, thủ tục cấp/cấp lại/điều chỉnh Giấy chứng nhận đăng ký lập quỹ"; Điều 240 = "Giải thể quỹ đóng". Cụm từ "kiểm soát nội bộ" xuất hiện trong ND155 chỉ ở các điều khoản KHÔNG áp dụng cho CTQLQ (Điều 89 của Luật CK áp dụng qua dẫn chiếu, không phải ND155 trực tiếp) hoặc thuộc một văn bản KHÁC (nghi là TT121/2020/TT-BTC về công ty chứng khoán) bị gộp chung trong cùng số Công báo. "Vốn khả dụng" trong ND155 chỉ xuất hiện ở các điều khoản về công ty chứng khoán, không phải công ty quản lý quỹ.
- **Kết luận:** đã KHÔNG dùng ND155/2020 làm nguồn cho task nào trong đợt này — không tìm được điều khoản đúng chủ đề "kiểm soát nội bộ/lịch báo cáo định kỳ/vốn khả dụng của CTQLQ" trong chính văn bản này sau khi đọc toàn văn. Các nội dung này (kiểm soát nội bộ, khẩu vị rủi ro) đã được khối Back Office khai thác từ **Thông tư 99/2020/TT-BTC** và **Quyết định 428/QĐ-UBCK** ở 87 task hiện có (T-BO-055 đến T-BO-087) — không đào lại.

Đây là bằng chứng ủng hộ đúng cảnh báo Mục 1.1 của `PHASE2_PLAN.md`: các số điều khoản trong tóm tắt nội bộ chưa xác minh (`03_industry_vn/legal/*.md`) **không dùng được**, chỉ là gợi ý vị trí tìm.

## 3. Task bóc tách — tóm tắt

| task_id | Chủ đề | do_tin_cay | source_ids |
|---|---|---|---|
| T-CO-001 | Tách biệt tài sản ủy thác từng khách hàng / công ty | REG | S-COMP-001 |
| T-CO-002 | Kiểm soát nội bộ ngăn xung đột lợi ích với người có liên quan | REG | S-COMP-001 |
| T-CO-003 | Tách biệt nhân sự các vị trí có nguy cơ xung đột lợi ích | FACT | S-COMP-001, S-COMP-003 |
| T-CO-004 | Báo cáo giao dịch CK cá nhân nhân viên cho KSNB | FACT | S-COMP-003 |
| T-CO-005 | CBTT bất thường 24h khi vượt hạn mức/định giá sai NAV | REG | S-COMP-002 |
| T-CO-006 | CBTT bất thường 24h khi bị UBCKNN xử phạt/cảnh báo | REG | S-COMP-002 |
| T-CO-007 | Báo cáo UBCKNN khi CTQLQ trở thành cổ đông lớn (hộ NĐT ủy thác) | REG | S-COMP-001, S-COMP-002 |
| T-CO-008 | Công bố website thay đổi sở hữu cổ đông lớn/người nội bộ (3 ngày) | REG | S-COMP-002 |
| T-CO-009 | Tiếp nhận đăng ký giao dịch người nội bộ (≥3 ngày trước) | REG | S-COMP-002 |
| T-CO-010 | Công bố báo cáo tỷ lệ an toàn tài chính 30/6, 31/12 | REG | S-COMP-001, S-COMP-002 |
| T-CO-011 | Kiểm tra hạn mức đầu tư trước khi đặt lệnh (pre-trade check) | INFERENCE | S-COMP-002, S-COMP-004, S-COMP-005 |

**Tỷ lệ:** 8/11 REG (73%), 2/11 FACT (18%), 1/11 INFERENCE (9%) — tỷ lệ REG cao, đúng như PHASE2_PLAN dự đoán "khối có nền pháp lý sẵn rõ nhất".

Tất cả đã kiểm tra chéo với 87 task hiện có, đặc biệt T-BO-020 (báo cáo định kỳ UBCKNN — generic,
khác với T-CO-005/006/007/008/009 là các nghĩa vụ CBTT BẤT THƯỜNG/cụ thể mới, không trùng), T-BO-031
(kiểm soát tuân thủ hạn mức — hậu kiểm/định kỳ, khác T-CO-011 là tiền kiểm/theo từng lệnh), T-BO-049/050/051
(AML/KYC — chủ đề hoàn toàn khác, không đụng), T-BO-055 (khẩu vị rủi ro theo QĐ428 — quản trị rủi ro thị
trường/thanh khoản, khác T-CO-002/003 là xung đột lợi ích/tách biệt nhân sự theo Luật CK).

**Task cân nhắc nhưng KHÔNG thêm** vì trùng lặp/quá gần task đã có:
- "Báo cáo UBCKNN định kỳ/bất thường về danh mục đầu tư, hoạt động đầu tư, tình hình tài chính của quỹ"
  (Luật CK Điều 107) — bị loại vì nội dung thực chất trùng với T-BO-020 đã có (báo cáo định kỳ UBCKNN),
  dù T-BO-020 trích JD chung chung còn Điều 107 có căn cứ REG rõ hơn. Cân nhắc để người review quyết định
  có nên UPDATE source_ids của T-BO-020 (bổ sung S-COMP-001) thay vì tạo task mới hay không.

## 4. Không tìm được / nghi vấn cần người review kiểm tra

1. **ND155/2020/NĐ-CP không có điều khoản đúng như PHASE2_PLAN gợi ý** (xem Mục 2 ở trên) — đã đọc toàn
   văn 7 phần PDF Công báo (~1,1 triệu ký tự) và xác nhận. Không dùng ND155 làm nguồn cho đợt task này.
   Nếu người review biết văn bản khác có nội dung "kiểm soát nội bộ/vốn khả dụng CTQLQ" (có thể là TT99/2020
   đã dùng ở BO, hoặc Nghị định 245/2025/NĐ-CP sửa đổi ND155 — đã kiểm tra tóm tắt ND245/2025 và nội dung sửa
   đổi tập trung vào chứng quyền có bảo đảm/niêm yết/sở hữu nước ngoài, KHÔNG đề cập kiểm soát nội bộ CTQLQ),
   xin bổ sung riêng.
2. **T-CO-004** (báo cáo giao dịch CK cá nhân nhân viên) gắn `FACT` chỉ dựa trên 1 case xử phạt (S-COMP-003),
   CHƯA tìm được văn bản REG gốc mô tả rõ nghĩa vụ này (nghi là nằm trong TT99/2020 — "hạn chế đối với hoạt
   động của nhân viên làm việc tại công ty quản lý quỹ" — nhưng tôi chưa đọc lại TT99 gốc trong đợt này vì
   AS-005 đã coi TT99 là nguồn đã khai thác ở khối Back Office). Đề nghị người review đối chiếu TT99/2020
   bản gốc để nếu có điều khoản rõ, nâng `chi_tiet_ref`/`rang_buoc_phap_ly` lên REG.
3. **T-CO-011 (pre-trade compliance check)** gắn `INFERENCE` có chủ đích — pháp luật Việt Nam hiện xác minh
   được CHỈ quy định không được vượt hạn mức (kết quả), KHÔNG quy định cụ thể phải kiểm tra trước khi đặt
   lệnh (cơ chế). Task này dựa một phần vào tài liệu vendor quốc tế (Bloomberg AIM, Confluence) làm chuẩn
   ngành tham khảo — đúng theo yêu cầu PHASE2_PLAN Mục 2.3(a) nhưng CẦN phỏng vấn thực tế Compliance Officer
   tại một công ty quản lý quỹ VN để xác nhận có tồn tại bước kiểm tra tiền kiểm dạng này hay không trước khi
   nâng use case lên VERIFIED.
4. **S-COMP-003 (case HD Capital)** — tier T1 gán theo tiền lệ `S-ENF-001/002` trong registry gốc (báo chí
   dẫn số quyết định cụ thể được coi T1), nhưng bản thân tôi CHƯA truy cập được văn bản gốc Quyết định
   1017/QĐ-XPHC trên ssc.gov.vn (không tìm thấy bản PDF công khai qua tìm kiếm). Đề nghị người review cân
   nhắc hạ tier xuống T4 nếu muốn áp dụng chuẩn nghiêm ngặt hơn tiền lệ, hoặc tìm bản gốc trên ssc.gov.vn để
   nâng độ tin cậy.
5. **Case xử phạt khác** được tìm thấy nhưng KHÔNG dùng vì đã cũ hoặc không đủ chi tiết mới: "Cùng lúc 2 công
   ty quản lý quỹ bị UBCKNN phạt" (cafef.vn, 2016) — An Phát và Hợp Lực Việt Nam, vi phạm về công bố thông
   tin chậm và thông báo người phụ trách CBTT — nội dung tương tự case Amber Capital đã dùng, không đủ khác
   biệt để làm case mới, và văn bản gốc không tìm thấy → không đăng ký làm nguồn.
6. **Không tìm được** case xử phạt UBCKNN nào khác về "xung đột lợi ích" ngoài HD Capital trong phạm vi tìm
   kiếm đã thực hiện — không loại trừ khả năng có case khác chưa tìm ra do giới hạn công cụ tìm kiếm (WebSearch
   chỉ trả kết quả tiếng Việt/Anh phổ biến, không truy cập trực tiếp kho quyết định xử phạt của ssc.gov.vn).
7. **Cột `tang` (tầng) dùng "Middle Office" thay vì "Back Office"** — 87 task hiện có đều gán `tang=Back Office`
   kể cả các task về compliance/quản trị rủi ro (T-BO-055 đến T-BO-087), dù `AGENT_ROSTER.md` (Mục 5,
   `IMPLEMENTATION_PLAN.md`) xếp "Compliance Officer" và "Head of Risk" vào nhóm **Middle**. 11 task mới trong
   đợt này được gán `tang=Middle Office` cho đúng với định nghĩa tầng trong schema gốc. Đây là CHỦ ĐÍCH, không
   phải lỗi — nhưng tạo ra sự KHÔNG NHẤT QUÁN với 87 dòng cũ nếu gộp chung. Người review cần quyết định: (a)
   giữ nguyên khác biệt này (coi 87 dòng cũ là lỗi phân loại chưa sửa), hoặc (b) đổi `tang` của 11 dòng mới
   thành `Back Office` cho nhất quán với dữ liệu hiện có, hoặc (c) sửa lại cả 87 dòng cũ (phạm vi lớn hơn,
   không thuộc nhiệm vụ đợt này).
8. **thuvienphapluat.vn và vbpl.vn đều chặn bằng Cloudflare challenge** (HTTP 403 "Just a moment...") khi
   truy cập trực tiếp (cả qua WebFetch lẫn curl) trong phiên làm việc này — khác với ghi chú trong
   `SOURCE_REGISTRY.csv` gốc rằng `S-TT98-001` (thuvienphapluat.vn) đã dùng được trước đây. Có thể do
   Cloudflare bật bảo vệ chặt hơn theo thời gian, hoặc do khác IP/phiên. Đã chuyển sang dùng
   `congbao.chinhphu.vn` (Công báo Chính phủ, cũng là nguồn T1 chính thức) làm nguồn thay thế thành công.
   Người review nên biết: nếu tái sử dụng quy trình này cho 3 khối còn lại (Corporate Actions, Client
   Reporting, Data Management), nên thử `congbao.chinhphu.vn` trước thay vì `thuvienphapluat.vn`.

## 5. Danh sách file đã tạo

- `_data/staging_compliance_sources.csv` — 5 dòng nguồn mới (S-COMP-001 đến 005)
- `_data/staging_compliance_tasks.csv` — 11 dòng task mới (T-CO-001 đến 011)
- `_raw/legal_v2/congbao-luat-chung-khoan-54-2019-vbhn24.md` (336KB, chứa header ghi chú + toàn văn trích PDF)
- `_raw/legal_v2/congbao-thong-tu-96-2020-tt-btc.md` (273KB)
- `_raw/legal_v2/baodautu-hdcapital-xu-phat-1017-qd-xphc.md` (9,6KB)
- `_raw/legal_v2/confluence-signal-product.md` (8,2KB)
- `_raw/legal_v2/bloomberg-aim-compliance-product.md` (24KB)
- `_data/staging_compliance_LOG.md` — file này

**KHÔNG có file gốc nào (`task_registry.csv`, `SOURCE_REGISTRY.csv`) bị sửa.**
