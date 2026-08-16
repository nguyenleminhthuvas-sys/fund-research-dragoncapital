# LUẬT BẤT BIẾN
1. ORCHESTRATOR là bạn (Main Agent). Skill chỉ là module được gọi ở
   phase chỉ định, KHÔNG skill nào được tự nhận vai điều phối.
2. Không bịa URL, không bịa số, không bịa chức danh. Không biết thì
   ghi "Không xác minh được" và đưa vào OPEN_QUESTIONS.md.
3. Số lượng use case do task_registry.csv quyết định, KHÔNG do quota.
   Cấm chẻ nhỏ hoặc đổi tên use case đã có để đạt chỉ tiêu.

## 3. GLOBAL_RULES.md — LUẬT CHUNG CHO MỌI AGENT

### 3.1 Nhãn bằng chứng (bắt buộc ở mọi dòng dữ kiện)

| Nhãn | Nghĩa | Yêu cầu |
|---|---|---|
| `[FACT]` | Sự kiện xác minh được | Bắt buộc có `source_id` |
| `[DATA]` | Số liệu định lượng | Bắt buộc có `source_id` + kỳ dữ liệu + đơn vị |
| `[CASE]` | Case study có thật | Bắt buộc có tên tổ chức + `source_id` |
| `[REG]` | Quy định pháp luật | Bắt buộc có số hiệu văn bản + điều khoản |
| `[INFERENCE]` | Suy luận từ dữ kiện | Bắt buộc ghi rõ suy luận từ dòng nào |
| `[HYPOTHESIS]` | Giả thuyết chưa có bằng chứng | Bắt buộc ghi cách kiểm chứng |
| `[VENDOR CLAIM]` | Tuyên bố từ nhà cung cấp | Không được dùng làm bằng chứng ROI |
| `[UNVERIFIED]` | Không xác minh được | Giữ lại nhưng không đưa vào kết luận |

### 3.2 Phân hạng nguồn

| Tier | Loại | Ví dụ |
|---|---|---|
| **T1** | Nguồn sơ cấp/pháp lý | Bản cáo bạch, điều lệ quỹ, BCTC kiểm toán, BC thường niên, văn bản pháp luật, CBTT trên HOSE/HNX/VSDC/SSC, annual report VEIL trên LSE |
| **T2** | Tổ chức có thẩm quyền | ICI, EFAMA, CFA Institute, BIS, IMF, IOSCO, McKinsey/BCG/Bain/Big4, Cerulli, Broadridge |
| **T3** | Ngành & dữ liệu thị trường | FiinGroup, Vietstock, Fmarket, tài liệu vendor (SimCorp, Aladdin, CRD), JD tuyển dụng |
| **T4** | Báo chí & cộng đồng | CafeF, VnEconomy, blog, forum |

**Luật:** kết luận không được chỉ dựa trên T4. Số liệu về Dragon Capital phải là T1, nếu không có thì gắn `[UNVERIFIED]`.

### 3.3 Chống bịa (anti-hallucination)
1. **Cấm chế URL.** Chỉ ghi URL đã thực sự truy cập được. URL chết → ghi `[DEAD LINK]` + ngày kiểm tra.
2. **Cấm chế số.** Không có số → viết `Không xác minh được`, không ước lượng ngầm.
3. **Cấm chế tên người và chức danh cụ thể tại Dragon Capital.** Chỉ ghi chức danh khi có nguồn T1/T3 (BC thường niên, LinkedIn, JD).
4. **Cấm suy diễn quy trình nội bộ thành `[FACT]`.** Quy trình nội bộ chưa xác minh → luôn là `[INFERENCE]` với nền là chuẩn ngành.
5. **Trích dẫn ≤ 15 từ** cho mọi nguồn. Còn lại phải diễn đạt lại. Không copy nguyên đoạn bản cáo bạch hay báo cáo.
6. **Mọi số liệu phải có kỳ.** "AUM 77.000 tỷ" là vô nghĩa nếu không có "tại thời điểm nào".

### 3.4 Luật ghi Source Registry
Trước khi dùng bất kỳ nguồn nào, agent phải thêm một dòng vào `/_data/SOURCE_REGISTRY.csv` và lấy `source_id`. Không có `source_id` → không được trích.

### 3.5 6 câu hỏi kiểm chứng use case
Mọi use case phải trả lời (điền vào registry):
1. **AI_LAM_GI** — hôm nay ai làm việc này? (chức danh cụ thể, không phải "bộ phận")
2. **TAN_SUAT_THOI_LUONG** — bao lâu một lần, mỗi lần mất bao lâu?
3. **DU_LIEU** — input nằm ở đâu, định dạng gì, ai sở hữu?
4. **HAU_QUA_SAI** — sai thì hậu quả gì? → quyết định mức human-in-the-loop
5. **KPI** — chỉ số nào cải thiện, cải thiện bao nhiêu?
6. **RANG_BUOC_PHAP_LY** — vướng quy định nào?

Đủ 6 → `VERIFIED`. Đủ 3–5 → `CATALOGUE`. Dưới 3 → **loại**, không được đưa vào registry.

### 3.6 Luật ngôn ngữ & độ dài
- Viết tiếng Việt. Thuật ngữ chuyên ngành giữ tiếng Anh, giải thích lần đầu.
- **Nội dung trong ô CSV: tối đa 200 ký tự.** Cần dài hơn → tách sang file .md riêng và ghi đường dẫn vào ô `chi_tiet_ref`.
- Không viết văn giải thích dài trong artifact dữ liệu. Số liệu + nguồn + nhãn.

### 3.7 Khi bế tắc
Không đoán. Ghi vào `OPEN_QUESTIONS.md` theo format:
```
[OQ-###] | Agent | Câu hỏi | Vì sao chặn | Đề xuất cách gỡ (nguồn nào / hỏi ai) | Mức chặn: BLOCKER/HIGH/LOW
```

### 3.8 LUẬT URL — Bắt buộc từ 2026-08-15
*(Bổ sung sau sự cố fetch lần 2 thất bại 100% vì ghép URL)*

1. **Chỉ fetch URL đến từ:**
   - (a) Kết quả search thực sự vừa chạy, hoặc
   - (b) Link nằm trong HTML của trang đã tải thành công.
2. **CẤM tự ghép đường dẫn theo pattern** (ví dụ: thêm `/dieu-20`, `/fund-accounting`, `/ban-cao-bach` mà không thấy link đó trong trang).
3. **CẤM lấy URL từ SOURCE_REGISTRY cũ** để fetch lại — registry cũ có thể chứa URL bịa.
4. **URL trả về 404:** quay lại search với từ khóa khác. KHÔNG thử biến thể đường dẫn (ví dụ: đổi `fund-administration` thành `fund-admin` hay `investment-accounting`).
5. **URL trả về nội dung không khớp tieu_de:** ghi `[DEAD LINK]` + ngày kiểm tra + nội dung thực sự thấy, XÓA khỏi registry. KHÔNG sửa URL bằng cách đoán.
6. **Mọi URL trong SOURCE_REGISTRY phải đã được mở thành công** và title/nội dung trang xác nhận khớp với `tieu_de`.

### 3.9 LUẬT FETCH — Bắt buộc từ 2026-08-15
*(Bổ sung sau sự cố URL #3 hethongphapluat.com — tốn thời gian, không thu được gì)*

1. **Tối đa 5 trang cho mỗi nguồn.** Đủ 5 trang → dừng, ghi FETCH_LOG.
2. **Không đi theo link đệ quy.** Chỉ đi 1 tầng từ trang gốc (không follow link từ trang con).
3. **Timeout 60 giây.** Một URL không phản hồi sau ~60 giây → bỏ, ghi vào FETCH_LOG, đi tiếp.
4. **Không dùng browser subagent** khi đang rate-limit. Ưu tiên `read_url_content`.
5. **SPA/AJAX → không đoán URL.** Nếu trang là SPA và HTML tĩnh không có link PDF → ghi FETCH_LOG, bỏ qua. **KHÔNG tự đoán hoặc ghép URL CDN**.
6. **PDF không đọc được text → ghi FETCH_LOG.** Không tự viết tóm tắt thay thế.
7. **hethongphapluat.com bị cấm.** Trang này tách văn bản thành ~60 URL riêng — không đáng thời gian. Dùng thuvienphapluat hoặc luatminhkhue.

### 3.10 LUẬT KIỂM NGUỒN — Bắt buộc từ 2026-08-16
*(Bổ sung sau đợt kiểm 6 artifact phát hiện GLOBAL_MAP.md, VN_MAP.md, SEGMENTATION_MATRIX.md,
VALUE_CHAIN.md và toàn bộ `processes/` bị sinh bằng template, trích `source_id` không tồn tại
trong SOURCE_REGISTRY.csv hoặc gán nhầm sang nguồn không liên quan — xem `_quarantine/README.md`)*

Diễn đạt lại tốt và tỷ lệ `[INFERENCE]` thấp **KHÔNG chứng minh dữ liệu thật.** Một artifact chỉ
được coi là dùng được khi thỏa cả 3 điều kiện:

1. **Mọi `source_id` trong nó tồn tại trong `SOURCE_REGISTRY.csv`.**
2. **Mỗi `source_id` trỏ tới file có thật trong `_raw/`.**
3. **Nội dung file `_raw/` đó thực sự nói về điều đang được trích.**

Kiểm điều 3 bằng cách **mở file và đọc**, không suy từ tên file. Một `raw_ref` tồn tại không có
nghĩa là nội dung khớp — phải đọc để xác nhận đoạn trích thật sự nằm ở đó.

---

## OVERRIDE SKILL — ĐIỂM ORCHESTRATOR GHI ĐÈ LÊN SKILL

*Phần này là tài liệu pháp lý nội bộ. Mọi agent đọc GLOBAL_RULES phải biết những điều này.*
*Chi tiết kỹ thuật đầy đủ: xem `/00_control/SKILL_INTEGRATION_MAP.md`*

### OS-1: Cấm quota cứng về số lượng use case (ghi đè Skill 1)

Skill 1 (`ai-usecase-researcher.md`) hardcode "ĐÚNG 20 use cases" mỗi subagent và "100-300+ use cases" làm outcome. **Những con số này bị vô hiệu hóa hoàn toàn.**

Quy tắc thay thế: A10 chỉ tạo use case khi tồn tại `task_id` tương ứng trong `task_registry.csv` và câu trả lời cho ≥ 1 trong 7 năng lực AI là "có, kèm lý do cụ thể". Nếu domain có 12 task phù hợp → output 12, không bịa thêm 8.

### OS-2: Domain chia theo khối chức năng, không theo ngành tổng (ghi đè Skill 1)

Skill 1 chia batch theo "domain chuyên biệt ngành" (VD: "chẩn đoán", "dược"). Dự án này chia theo **khối chức năng** (FO/MO/BO/EN) theo mã khối trong `task_registry.csv`. Mỗi subagent A10 = 1 khối chức năng.

### OS-3: task_registry.csv là input bắt buộc khi gọi Skill 1 (ghi đè Skill 1)

Skill 1 tự phân tích ngành từ đầu (Phase 0, Bước 2). **Cấm.** Khi ORCHESTRATOR gọi Skill 1 ở Phase 5, phải truyền vào:
- `industry_context` = output tổng hợp từ A2+A3+A6+A8 artifacts
- `task_list` = danh sách task_id của khối đó từ `task_registry.csv`
Skill 1 chỉ được sinh use case từ danh sách task_id này, không được tự tạo task mới.

### OS-4: Schema output ánh xạ về usecase_registry.csv (ghi đè Skill 1)

Skill 1 dùng 9-field Python dict. Toàn bộ output phải được A10 convert sang 23-cột `usecase_registry.csv` theo bảng ánh xạ trong `SKILL_INTEGRATION_MAP.md` Mục 4 **trước khi** ghi vào registry. HTML badge/source format của Skill 1 chỉ dùng cho output HTML cuối cùng.

### OS-5: Scoring dùng công thức 4 trục của plan (ghi đè Skill 1)

Skill 1 Tier 1/2/3 (thời gian triển khai) không thay thế công thức A11:
`tong_diem = Giá_trị×0.35 + Khả_thi×0.25 + Dữ_liệu×0.25 + Rủi_ro×0.15`
Tier 1/2/3 được giữ lại làm field phụ `tier_trien_khai` trong `PRIORITY.md`.

### OS-6: Deep Dive áp dụng cho 20 UC, không phải 10 (ghi đè Skill 1)

Skill 1 hardcode "Deep Dives — 10 UC quan trọng nhất". Dự án này deep dive **20 UC đầu bảng** theo tổng_diem sau khi A11 xếp hạng.

### OS-7: Fact-check chỉ chạy trên 100 UC được lọc (ghi đè quy trình Skill 1)

Skill 1 Phase 3 (QuoteExtractorAgent) thiết kế chạy trên toàn bộ batch. **Override:** QuoteExtractor chỉ chạy sau khi A11 lọc ra 100 UC xuất sắc nhất. Không fact-check 300 UC thô để tiết kiệm tài nguyên và tập trung độ sâu.

### OS-8: Source path và output path override (ghi đè Skill 1)

- Scratch path: `/Users/mac/.gemini/antigravity/brain/{subagent_id}/` (không phải `/Users/tungchi/...`)
- Output HTML: `12_report/FINAL_REPORT.html` (không phải `{USER_OUTPUT_DIR}/{industry}_ai_report.html`)

### OS-9: Skill 2 — Investment View Signal là optional cho artifact nội bộ (ghi đè Skill 2)

Skill 2 bắt buộc OVERWEIGHT/NEUTRAL/UNDERWEIGHT ở mọi output. Dự án này dùng `--mode buy-side` (internal research). **Override:** Investment View Signal bắt buộc CHỈ tại `12_report/FINAL_REPORT.md` phần Executive Summary. Các artifact nghiên cứu trung gian (A2-A8) được miễn.

### OS-10: Skill 2 — Source hierarchy tích hợp vào tier T1-T4 của GLOBAL_RULES (ghi đè Skill 2)

Skill 2 có thứ bậc nguồn riêng. **Tier T1-T4 của GLOBAL_RULES là tiêu chuẩn duy nhất.** Nguồn Skill 2 gợi ý chỉ là danh sách địa chỉ tìm kiếm, không override tier classification.

---
