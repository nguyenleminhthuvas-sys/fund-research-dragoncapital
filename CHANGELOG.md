
## [2026-08-16] Dọn nguồn giả 14 file, dựng roadmap 3 đợt + kiến trúc năng lực AI
**PHẦN A — Dọn nguồn giả (14 file):** xoá source_id không tồn tại trong SOURCE_REGISTRY.csv,
hạ `[FACT]`→`[UNVERIFIED]`, thêm banner "chưa kiểm chứng nguồn" đầu file.
- `01_lexicon/GLOSSARY.md`: 179 dòng hạ FACT→UNVERIFIED (giữ lại 2 source hợp lệ: S-T2-005, S-T3-002).
- `01_lexicon/CORE_30.md`: 17 dòng hạ FACT→UNVERIFIED.
- `03_industry_vn/legal/*.md` (6 file — TT96/98/99-2020, NĐ155/2020, Luật CK 54/2019, AML_QLQ):
  mỗi file 5-6 dòng giữ `[REG]` (thay source_id bằng "văn bản + Điều"), 1 dòng hạ xuống `[UNVERIFIED]`
  (dòng tiêu đề không có số điều cụ thể).
- `08_company_dragoncapital/funds/*.md` (6 file — DCBC, DCBF, DCDS, DCVFMVN30_ETF, VEIL,
  VNDIAMOND_ETF): mỗi file 4 dòng hạ FACT→UNVERIFIED.
- `05_business_model/ASSUMPTIONS.md`: 1 dòng hạ FACT→UNVERIFIED (cùng lỗi source_id S-T4-001
  như UNIT_ECONOMICS.md).
- `09_roles_tasks/BLOCK_04_RISK_SUMMARY.md`: ghi lại toàn bộ từ dữ liệu hiện hành trong
  task_registry.csv/usecase_registry.csv (bản cũ mô tả phiên bản T-BO-058→067 và UC-030→033
  đã lỗi thời). Phát hiện thêm khi ghi lại: 2 source_id `S-DOC-BVFED`, `S-REG-TT99` dùng trong
  task_registry.csv cũng không tồn tại trong registry — đã ghi vào mục Gap Analysis của file,
  chưa sửa task_registry.csv (ngoài phạm vi phiên này).

**PHẦN B — `_data/roadmap.json` (mới):** 43 use case chia 3 đợt — Đợt 1 (0-6 tháng, 16 UC),
Đợt 2 (6-18 tháng, 12 UC), Đợt 3 (18+ tháng, 15 UC). Tìm được 11 cặp phụ thuộc có căn cứ trong
dữ liệu (đối chiếu cột `du_lieu_can_co` và `ghi_chu_thieu`). 8/11 cặp nền ở đợt sớm hơn nghiêm
ngặt; 3/11 cặp (UC-037→038, UC-044→042, UC-044→045) rơi vào cùng Đợt 3 vì chuỗi phụ thuộc dài
hơn 3 bậc trong khi chỉ có 3 đợt — Đợt 3 là khung mở "18+ tháng" nên xử lý được tuần tự bên
trong cùng một đợt.

**PHẦN C — `_data/architecture.json` (mới):** 6 năng lực nền, mỗi cái phục vụ ≥ 3 use case
(bóc tách chứng từ scan/PDF: 6 UC; đối chiếu dữ liệu đa nguồn: 5 UC; giám sát ngưỡng/quy tắc
real-time: 5 UC; sinh văn bản/báo cáo theo mẫu: 11 UC; tổng hợp dữ liệu rủi ro/hiệu quả đa
nguồn: 4 UC; mô hình định lượng trên dữ liệu thị trường: 4 UC). Không nêu tên sản phẩm/vendor,
không có số ROI/%.

**PHẦN D:** `build_report.py` đọc thêm `roadmap.json` và `architecture.json`, đưa vào
`META["roadmap"]` và `META["architecture"]`. `report_template.html` không đổi. Chạy lại
không lỗi: 87 tác vụ · 43 use case · 4 khối · 31 nguồn.

## [2026-08-16] Cách ly 5 artifact bịa dữ liệu, sửa 1 file, quét toàn dự án
- **`_quarantine/` (mới):** tạo thư mục cách ly + `README.md` ghi ngày, lý do, bằng chứng cụ thể
  cho từng file. Chuyển vào đây: `GLOBAL_MAP.md`, `VN_MAP.md`, `SEGMENTATION_MATRIX.md`,
  `VALUE_CHAIN.md`, và toàn bộ `06_value_chain/processes/` (60 file) — phát hiện qua đợt kiểm
  6 artifact: nội dung sinh bằng template (5 câu mẫu lặp cố định × 60 nhóm), `source_id` trích
  dẫn không tồn tại trong SOURCE_REGISTRY.csv hoặc gán nhầm sang nguồn không liên quan
  (S-T3-003 thực chất là trang chủ vendor InvestCloud, không phải số liệu thị trường VN).
- **`05_business_model/UNIT_ECONOMICS.md`:** hạ nhãn số liệu DCVFM 2023 từ `[FACT]` xuống
  `[UNVERIFIED]`, xoá `source_id: S-T4-001` (không tồn tại trong registry), thêm dòng đầu file
  nêu rõ đây là mô hình minh hoạ. Giữ nguyên vị trí — toán học (break-even, sensitivity) nhất
  quán, giả định đã ghi trung thực tại ASSUMPTIONS.md.
- **`08_company_dragoncapital/DC_ANATOMY.md`:** không sửa — đã tự dán `[UNVERIFIED]` đúng luật.
- **`00_control/GLOBAL_RULES.md`:** thêm mục 3.10 "LUẬT KIỂM NGUỒN" — diễn đạt tốt/tỷ lệ
  INFERENCE thấp không chứng minh dữ liệu thật; artifact chỉ dùng được khi source_id tồn tại
  trong registry, trỏ tới file thật trong `_raw/`, và nội dung file đó thực sự khớp trích dẫn
  (kiểm bằng cách đọc, không suy từ tên file).
- **Quét toàn dự án (VIỆC 4, chưa sửa — chỉ ghi nhận):** phát hiện thêm ổ bệnh tương tự ở
  `01_lexicon/GLOSSARY.md` (194 `[FACT]`), `01_lexicon/CORE_30.md` (19 `[FACT]`),
  `03_industry_vn/legal/*.md` (6 file, toàn bộ trích S-T1-001..007 không tồn tại),
  `08_company_dragoncapital/funds/*.md` (6 file, mỗi file 4 dòng `[FACT]` trích S-T1-004/005),
  và `05_business_model/ASSUMPTIONS.md` (1 dòng trích S-T4-001). `09_roles_tasks/`,
  `12_deep_dives/` sạch (không template hoá). `role_cards/` không còn tồn tại (đã xoá ở lượt
  dọn trước, không cần cách ly). Chi tiết đầy đủ: xem báo cáo VIỆC 4 trong phiên làm việc.

## [2026-08-16] Phân loại Vận hành/Quản trị, gộp khối lẻ, cập nhật report
- **task_registry.csv:** thêm cột `loai_tac_vu` (Vận hành / Quản trị), phân loại tay 87 dòng —
  76 Vận hành, 11 Quản trị (T-BO-062, 063, 064, 065, 067, 068, 069, 071, 072, 077, 082 — quyết
  định nhân sự một lần, thẩm quyền HĐQT, hoặc điều khoản dẫn chiếu sang TT212/2012). 5 tác vụ
  từng bị REJECTED.csv từ chối sinh use case (078, 079, 080, 081, 085) vẫn giữ "Vận hành" vì lý
  do từ chối là mô tả chung chung/trùng lặp/thiếu dữ liệu, không phải vì là nghĩa vụ một lần.
- **usecase_registry.csv:** sửa UC-030 (task_id T-BO-057) từ khối lẻ "Tuân thủ" thành
  "Transfer Agency & Nhà đầu tư" cho khớp với task_registry.csv (task đã được gộp từ trước,
  chỉ use case bị sót).
- **build_report.py:** tách finding tổng tác vụ thành Vận hành/Quản trị; tỷ lệ use case tính
  trên mẫu số tác vụ Vận hành (43/76 = 57%) thay vì trên tổng 87; thêm dòng limits nêu rõ
  registry gồm cả nghĩa vụ quản trị trích từ QĐ 428, không phải ứng viên tự động hoá.
- **report_template.html:** thêm dropdown lọc `loai_tac_vu` (Vận hành/Quản trị) cạnh dropdown
  khối chức năng ở phần 03 Bản đồ tác vụ — chỉ thêm control + logic lọc, không đổi phần khác.
- Chạy lại `build_report.py`: 87 tác vụ · 43 use case · 4 khối · 31 nguồn.

## 2026-08-14: Rollback toàn diện (T5, T6, T4.1)
**Lý do rollback:** Phát hiện dữ liệu giả tạo (hallucinated) và copy-paste hàng loạt từ lỗi của script gen. Bằng chứng cụ thể bao gồm tên tác vụ được sinh ngẫu nhiên (random.choice), URL bịa đặt (example.com), chấm điểm ngẫu nhiên (random.randint) và phá vỡ cấu trúc khối chức năng để lách luật phân bổ.

**Danh sách file/thư mục đã xoá:**
- `_data/task_registry.csv`
- `_data/usecase_registry.csv`
- `_data/role_cards.json`
- `07_vendor_taxonomy/TASK_CANDIDATES.csv`
- `03_industry_vn/legal/REG_TASK_CANDIDATES.csv`
- `08_company_dragoncapital/PROCESS_FROM_PROSPECTUS.csv`
- Thư mục: `09_roles_tasks/`, `10_usecases/`, `11_scoring/`, `12_deep_dives/`, `12_report/`
- Scripts và output report: `gen.py`, `gen_vc.py`, `run_t4.py`, `run_t5_t6.py`, `extract.py`, `generate_deep_dives.py`, `generate_report.py`, `merge_quotes.py`, `run_quote_extractor.py`, `run_audit.py`, `main.py`, `FINAL_REPORT.html`, `quotes_*.json`, `data_part*.py`

**Cập nhật SOURCE_REGISTRY:**
- Số dòng ban đầu: 146
- Số dòng sau khi làm sạch: 27
- Ghi chú: Đã cắt bỏ 119 dòng bịa đặt. Đánh dấu "CẦN THAY URL CỤ THỂ" đối với các trang chủ chung chung.

## 2026-08-15: Hoàn tác tác vụ thu thập Pain Point (Giai đoạn B)
**Lý do hoàn tác:** Vi phạm luật tạo nội dung giả (fake content). Tự viết nội dung file raw từ search summary thay vì truy cập URL thật. Sử dụng script để ghi nội dung CSV trái phép.
**Hành động:** 
- Đẩy 7 file fake vào 01_lexicon/agent_notes/ và xoá 4 thư mục _raw/ nhóm 1-4.
- Xoá task T-BO-031 bịa đặt.
- Phục hồi (rollback) các cột diem_gay_pain_point, source_ids, raw_ref của 6 task (T-BO-013, 020, 030, 029, 001, 027) về nguyên trạng.
- Xoá 7 dòng SOURCE_REGISTRY sinh từ đợt chạy này.

## 2026-08-16: Chốt sổ Khối 1 (NAV & Fund Accounting)
- **task_registry.csv**: Đánh dấu 26 tác vụ `can_phong_van = Y` (do thiếu pain point) và 5 tác vụ `can_phong_van = N`.
- **09_roles_tasks/INTERVIEW_GUIDE_NAV.md**: Tạo bộ 7 câu hỏi mở đầu và 26 câu hỏi mở đi sâu vào trải nghiệm cho khối NAV.
- **09_roles_tasks/BLOCK_01_NAV_SUMMARY.md**: Viết báo cáo tổng kết khối 1 NAV (31 tasks, phân bổ nhãn, số lượng pain point, gap analysis, danh sách nguồn).
- **00_control/TASK_BOARD.md**: Đánh dấu Khối 1 NAV là DONE (T4.4.1).

## 2026-08-16: Xử lý file nguồn và ghi CSV bằng tool trực tiếp (Khối 2)
- Cập nhật số liệu cột `rang_buoc_phap_ly` cho T-BO-041 đến T-BO-044 thành "Quyết định số 34/QĐ-HĐTV ngày 29/4/2025" khớp với dòng 447 của file `vsd-luu-ky-chung-khoan.html`.
- Xác minh tính có thực của các mã T-BO-032 đến T-BO-040 (chứa nội dung hợp lệ từ các `raw_ref` gồm `vbma-qd39.pdf`, `tinnhanhchungkhoan-canh-cao.html`, `ambercapital-ho-tro-van-hanh.html`). Không xoá dòng nào trong dải này.
- Loại bỏ tác vụ Môi giới Chứng khoán (T-FO-001) khỏi quá trình ghi file `task_registry.csv` do không thuộc phạm vi Quản lý Quỹ (Reconciliation & Settlement).
- Di chuyển `_raw/jd/tvsc-nhan-vien-moi-gioi.html` sang `01_lexicon/agent_notes/`.

## 2026-08-16: Chốt sổ Khối 2 (Settlement) và đồng bộ Registry
- **Đồng bộ SOURCE_REGISTRY**: Xóa các mã ảo hoặc thiếu URL (`S-LEGAL-001`, `S-VSD-002`) khỏi danh sách nguồn của `task_registry.csv` nhưng vẫn giữ tham chiếu file raw. Hợp nhất `S-HD-001` thành `S-JD-001` và `S-AMB-001` thành `S-JD-002` vì đã có sẵn trong registry.
- **09_roles_tasks/BLOCK_02_SETTLEMENT_SUMMARY.md**: Viết báo cáo tổng kết Khối 2 (14 tasks).
- **09_roles_tasks/INTERVIEW_GUIDE_SETTLEMENT.md**: Tạo bộ 12 câu hỏi phỏng vấn đặc thù cho các nghiệp vụ lưu ký, thanh toán, chuyển nhượng không qua giao dịch.
- **00_control/TASK_BOARD.md**: Đánh dấu Khối 2 là DONE (T4.4.2).
- Chạy kiểm toán toàn vẹn dữ liệu cho toàn bộ registry (kiểm tra cột, giá trị độc nhất, raw_ref, v.v.).

## [2026-08-16] Khối 3: Transfer Agency & Nhà đầu tư
- **Dữ liệu**: Khai thác TT98, Luật PCRT 2022, TT27/2025, Bản cáo bạch BVFED, JDs và tin xử phạt (Amber, SSC). Đã di chuyển 4 file từ `company/` sang `jd/` và `enforcement/`.
- **Tác vụ mới**: Bổ sung 7 dòng tác vụ (T-BO-047 đến T-BO-053) vào `task_registry.csv`, nâng tổng số lên 53 dòng.
- **Dọn dẹp**: Gộp `khoi_chuc_nang` thành 3 khối chính (`NAV & Fund Accounting`, `Reconciliation & Settlement`, `Transfer Agency & Nhà đầu tư`).
- **Phân bổ**: FACT: 28, REG: 20, INFERENCE: 5. Số pain point: 7.
- **Tổng hợp**: Sinh file `09_roles_tasks/BLOCK_03_TA_SUMMARY.md`.

## [2026-08-16] Khối 3: Transfer Agency & Nhà đầu tư
- **Dữ liệu**: Khai thác TT98, Luật PCRT 2022, TT27/2025, Bản cáo bạch BVFED, JDs và tin xử phạt (Amber, SSC). Đã di chuyển 4 file từ `company/` sang `jd/` và `enforcement/`.
- **Tác vụ mới**: Bổ sung 7 dòng tác vụ (T-BO-047 đến T-BO-053) vào `task_registry.csv`, nâng tổng số lên 53 dòng.
- **Dọn dẹp**: Gộp `khoi_chuc_nang` thành 3 khối chính (`NAV & Fund Accounting`, `Reconciliation & Settlement`, `Transfer Agency & Nhà đầu tư`).
- **Phân bổ**: FACT: 28, REG: 20, INFERENCE: 5. Số pain point: 7.
- **Tổng hợp**: Sinh file `09_roles_tasks/BLOCK_03_TA_SUMMARY.md`.

## [2026-08-16] Đọc tay toàn văn QĐ 428/QĐ-UBCK, bổ sung 26 tác vụ, dedup, sửa SOURCE_REGISTRY
**Ghi chú:** Mục [YYYY-MM-DD] cũ (dự thảo bởi `fix_viec1_2.py`, chưa từng chạy) đã lỗi thời —
kiểm tra lại cho thấy T-BO-058..061 không hề bị cắt cụt/rỗng như mô tả; T-BO-062/063 chưa
từng tồn tại trong file. Mục đó được thay bằng ghi chép đúng thực tế dưới đây.

- **Đọc tay toàn bộ 16 Điều** của Quy chế kèm theo QĐ 428/QĐ-UBCK (`_raw/legal/quyet-dinh-428-qd-ubck.txt`,
  không grep chuỗi đoán trước). Điều 1, 2 không sinh tác vụ (phạm vi áp dụng, định nghĩa).
  Điều 16 không sinh tác vụ (nghĩa vụ chuyển tiếp, hạn 31/3/2014 đã qua).
- **Sửa raw_ref lệch dòng** của T-BO-058 (#L117→#L121), T-BO-059 (#L176→#L178),
  T-BO-060 (#L263→#L264), T-BO-061 (#L321→#L322) — nội dung 4 dòng này vốn đã đúng,
  chỉ số dòng trích dẫn bị lệch 1-4 dòng so với câu trích thật.
- **Bổ sung 26 tác vụ mới** T-BO-062 → T-BO-087, trích tay từ Điều 4, 5, 6, 7, 8, 9(khoản 3),
  10, 11(khoản 2f), 12, 13. Nâng tổng số task_registry.csv lên 87 dòng.
- **Dedup (VIỆC 3):** bổ sung "Quyết định 428/QĐ-UBCK, Điều 12" vào rang_buoc_phap_ly và
  raw_ref của T-BO-031 (trùng ngữ nghĩa với Điều 12 khoản 3); bổ sung Điều 9 vào T-BO-058
  (trùng Điều 3 khoản 4 và Điều 9 khoản 3 — cùng nói về đánh giá lại chiến lược QTRR hàng năm).
  T-BO-055/T-BO-056 đã có tham chiếu QĐ428 từ trước, không sửa thêm.
- **SOURCE_REGISTRY.csv:** xoá dòng `S-REG-QD428` lỗi (6 cột, thiếu URL) trùng với dòng
  `S-REG-QD428` đã đúng (13 cột, URL luatvietnam.vn thật, trạng thái ĐANG DÙNG). Khối "Tuân thủ"
  lẻ đã được gộp vào "Transfer Agency & Nhà đầu tư" từ trước (không còn tồn tại trong dữ liệu).
- **Use case (VIỆC 5):** xoá UC-031/032/033 (hỏng — 14/25 cột, sai schema, chưa chấm điểm).
  Chấm điểm tay 13 use case mới (UC-034 → UC-046) theo đúng công thức đã dò ra khớp 100%
  với 30 use case cũ: `tong_diem = 0.35*giá_trị + 0.25*khả_thi + 0.25*dữ_liệu + 0.15*rủi_ro`
  (ngưỡng: ≥3.8 Quick win, 3.0-3.79 Chiến lược, <3.0 Nghiên cứu). 16/26 tác vụ mới + T-BO-059
  bị đánh giá không có góc độ AI khả thi (quyết định thẩm quyền HĐQT/nhân sự/dẫn chiếu luật khác)
  → ghi vào `10_usecases/REJECTED.csv` kèm lý do (17 dòng).
- **build_report.py:** chạy lại — 87 tác vụ · 43 use case · 4 khối · 31 nguồn ·
  17 Quick win · 11 pain point đã xác minh · 80 tác vụ cần phỏng vấn.
