# SKILL INTEGRATION MAP
**Ngày tạo:** 2026-08-14
**Tác giả:** A0 ORCHESTRATOR
**Mục đích:** Xác định rõ mỗi skill được gọi khi nào, ở đâu, override điều gì
**Trạng thái:** v1.0 — dùng suốt dự án, cập nhật khi phát sinh xung đột mới

---

## 1. BẢNG SKILL × PHASE

| Phase plan | Task | Skill được gọi | Vai trò cụ thể | Ghi chú |
|---|---|---|---|---|
| Phase 1 — Nền tảng | T1.1 Glossary | **Skill 2** (Industry Deepdive) | Phase 1 Mental Model (Industry Intelligence Triad) + M2 Data Hierarchy để xác định thứ bậc nguồn ngành quản lý quỹ | Chỉ lấy framework tư duy, KHÔNG chạy full 29-dimension report |
| Phase 2 — 4 luồng song song | T2.1 Global Analyst | **Skill 2** (Industry Deepdive) | Phase 2 Research Engine (hard cap 5 vòng search) + Phase 3 Analysis (TAM Triangulation, Contradictions Protocol) | Mode: `--mode buy-side`, Depth: FULL |
| Phase 2 | T2.2 VN Analyst | **Skill 2** (Industry Deepdive) | Phase 2-3 tập trung pháp lý VN (SSC, luật CK 54/2019, TT98/99/96/2020) + Phase 4 Deliverable | Mode: `--mode buy-side`, không cần SSC disclaimer (internal) |
| Phase 2 | T2.3 Vendor Miner | **KHÔNG dùng skill** | A7 khai thác module vendor + JD bằng web search trực tiếp | Skill 2 không có framework cho vendor taxonomy |
| Phase 2 | T2.4 Company Analyst | **Skill 2** (Industry Deepdive) | Phase 2 Research cho Dragon Capital — tập trung T1 sources: bản cáo bạch, BCTC, CBTT | Mode: `--mode buy-side` |
| Phase 3 — Tổng hợp | T3.1 Segmentation | **Skill 2** (Industry Deepdive) | Dimension 25-26 (Peer Benchmarking) + Phần V (Porter/competitive landscape) | Dùng T8 template |
| Phase 3 | T3.2 Economics | **Skill 2** (Industry Deepdive) | Phần IV (Economics + Financial Analysis) — "trái tim" 18–20% | Dimension 9-13 (unit economics, P&L) |
| Phase 3 | T3.3 Value Chain | **Skill 2** (Industry Deepdive) | Dimension 4 (Value Chain) + framework tổng hợp đa nguồn | Không output báo cáo, output processes/*.md |
| Phase 4 — Role & Task | T4.1-T4.2 Role & Task | **KHÔNG dùng skill** | A9 tự hợp nhất CSV từ 4 nguồn thượng nguồn, không cần skill framework | Pure data engineering task |
| Phase 5 — Sinh Use Case | T5.1 Use Case Gen | **Skill 1** (AI Use Case Researcher) | Phase 2 Multi-Agent Generation: subagent mỗi khối chức năng, mỗi batch ~20 UC | **OVERRIDE** quota 20 UC/batch — xem Mục 3 |
| Phase 5 | T5.2 Dedup | **KHÔNG dùng skill** | A10 tự dedup theo logic ngữ nghĩa — skill 1 không có dedup protocol | |
| Phase 6 — Chấm điểm | T6.1 Scoring | **Skill 1** (AI Use Case Researcher) | Phần Prioritization Matrix: 7 tiêu chí chấm điểm, Top 30 | **OVERRIDE** schema chấm điểm — xem Mục 3 |
| Phase 6 | T6.2 Top 30 + Roadmap | **Skill 1** (AI Use Case Researcher) | HTML structure: Tier 1/2/3 roadmap + Deep Dives 20 UC | |
| Phase 7 — Audit | T7.1 Red Team | **KHÔNG dùng skill** | A12 tự audit — skill không có red team protocol | |
| Phase 7 | T7.2 Final Report | **Skill 1** (AI Use Case Researcher) | Phase 4: HTML Report Structure + main.py template | Điều chỉnh output path → `12_report/` |
| **FACT-CHECK** | Bước mới (xem MỤC TIÊU ĐÃ ĐIỀU CHỈNH) | **Skill 1** (AI Use Case Researcher) | Phase 3: QuoteExtractorAgent — fact-check 2 nguồn cho ĐÚNG 100 UC | Chỉ chạy trên 100 UC lọc, không phải toàn bộ |
| **DEEP DIVE** | Bước mới | **Skill 3** (Use Case Deep Dive) | **KHÔNG CÓ NỘI DUNG** — skill 3 hiện là file rỗng | ⚠️ BLOCKER — xem Mục 5 |

---

## 2. SKILL NÀO CHỒNG CHỨC NĂNG — ORCHESTRATOR CHỌN CÁI NÀO

### 2.1 Chồng giữa Skill 1 và Skill 2: phần "phân tích ngành"

**Hiện tượng:** Skill 1 (Phase 0, Bước 2) có "Phân tích cấu trúc ngành: sub-segments, bộ phận, quy trình core, điểm đau, xu hướng công nghệ". Skill 2 (toàn bộ) cũng phân tích ngành nhưng ở độ sâu institutional-grade (29 dimensions, dual-horizon, unit economics).

**Quyết định:** **Dùng Skill 2 cho phân tích ngành (Phase 1-3), Skill 1 KHÔNG được tự phân tích ngành.**
- Lý do: Skill 2 yêu cầu nguồn T1/T2 + nhãn kép + Contradictions Protocol — đúng chuẩn GLOBAL_RULES của dự án này. Phần "phân tích ngành" trong Skill 1 chỉ là context loading cho use case generation, không phải independent deliverable.
- Cách thực thi: Khi gọi Skill 1 ở Phase 5, truyền output của A2/A3/A6 vào field `industry_context` — không để Skill 1 tự phân tích ngành từ đầu.

### 2.2 Chồng giữa Skill 1 và Skill 2: phần source hierarchy

**Hiện tượng:** Skill 1 ưu tiên nguồn theo ngành (Tài chính: BIS > IMF > MAS > Basel > McKinsey > Deloitte). Skill 2 ưu tiên theo thứ bậc VN-first (GSO/SBV/MOF/BCTC → Bộ ngành → Hiệp hội → World Bank/IMF → FiinPro → báo chí). GLOBAL_RULES dự án có T1-T4 tier riêng.

**Quyết định:** **GLOBAL_RULES tier T1-T4 của dự án là tiêu chuẩn duy nhất.** Hai skill chỉ là gợi ý nguồn, không override tier hệ thống.
- Ánh xạ: T1=Skill2 nguồn 1 (BCTC/pháp lý) | T2=Skill2 nguồn 2-4 + Skill1 BIS/IMF/McKinsey | T3=Skill2 nguồn 5-6 + FiinGroup/Fmarket | T4=Skill2 nguồn 7 (báo chí) = Cấm làm bằng chứng số liệu.

### 2.3 Chồng giữa Skill 1 và Skill 2: chấm điểm use case

**Hiện tượng:** Skill 1 chấm theo 3 Tier thời gian (Quick Win 0-6M / Strategic 6-18M / Moonshot 18-36M). Skill 2 không có framework chấm điểm UC. PLAN có công thức 4 trục với trọng số (Giá trị×0.35 + Khả thi×0.25 + Dữ liệu×0.25 + Rủi ro×0.15) + 3 rổ (quick_win/chien_luoc/nghien_cuu).

**Quyết định:** **Dùng công thức 4 trục của PLAN (T6.1).** Skill 1 Tier 1/2/3 map vào rổ của plan như sau:
- Tier 1 (0-6M) ≈ `quick_win` (tổng ≥ 3.8, khả thi ≥ 4, dữ liệu ≥ 4)
- Tier 2 (6-18M) ≈ `chien_luoc` (giá trị ≥ 4, nhưng khả thi hoặc dữ liệu ≤ 3)
- Tier 3 (18-36M) ≈ `nghien_cuu` (còn lại)

---

## 3. QUOTA CỨNG CẦN OVERRIDE

### 3.1 Skill 1 — "ĐÚNG 20 use cases" mỗi subagent (dòng 100, 117)

**Vấn đề:** Skill 1 hardcode "ĐÚNG 20 dictionary" trong prompt template subagent. Tuy nhiên LUẬT BẤT BIẾN số 3: *"Số lượng use case do task_registry.csv quyết định, không do quota."*

**Override:**
```
THAY: "Viết ... với ĐÚNG 20 dictionary về mảng {domain_name}"
BẰNG: "Viết ... với TỐI ĐA 20 dictionary về mảng {domain_name}.
       Chỉ tạo use case khi tác vụ trong task_registry.csv thực sự
       phù hợp với domain này. Nếu domain có 12 tác vụ phù hợp
       thì output 12, không bịa thêm 8 để đủ 20."
```

**Dòng cần override trong Skill 1:**
- Dòng 59: `- Chia use case thành batch 20 UCs/batch` → thay bằng `batch ≤ 20 UCs`
- Dòng 100: `ĐÚNG 20 use cases chi tiết` → thay bằng `≤ 20 use cases thực sự có task tương ứng`
- Dòng 117: `với ĐÚNG 20 dictionary` → thay bằng `với tối đa 20 dictionary (ưu tiên chất lượng)`
- Dòng 306: `Tổng UCs đúng với kế hoạch?` → thay bằng `Tổng UCs bằng số task hợp lệ × tỷ lệ 1.2-1.5?`

### 3.2 Skill 1 — "100-300+ use cases" ở header description (dòng 6)

**Vấn đề:** Skill 1 tự claim "tạo 100-300+ use cases" như một outcome cố định. Đây là quota gián tiếp.

**Override:** ORCHESTRATOR nhắc nhở mỗi khi gọi Skill 1: target 300 ứng viên KHÔNG phải sàn cứng. Nếu task_registry có 250 task × 1.2 = 300 UC tối đa. Nếu 200 task × 1.2 = 240 UC. Accept.

### 3.3 Skill 1 — Deep Dives "10 UC quan trọng nhất" (dòng 213)

**Vấn đề:** Skill 1 hardcode deep dive cho 10 UC. Mục tiêu dự án đã điều chỉnh là **20 UC đầu bảng**.

**Override:**
```
THAY: "Deep Dives — Phân tích sâu 10 UC quan trọng nhất"
BẰNG: "Deep Dives — Phân tích sâu 20 UC đầu bảng theo tổng_diem"
```

### 3.4 Skill 1 — Prioritization Matrix "Top 30 UCs" (dòng 212)

**Vấn đề:** Skill 1 cố định "Top 30 UCs được chấm điểm (7 tiêu chí)". Dự án này chấm TOÀN BỘ registry, sau đó lọc xuống 100 UC xuất sắc nhất, rồi deep dive 20.

**Override:** Prioritization Matrix chạy trên TOÀN BỘ registry (không chỉ top 30 để chấm). Output PRIORITY.md của A11 ghi tất cả điểm, sau đó lọc 100 tốt nhất để fact-check, 20 tốt nhất để deep dive.

---

## 4. BẢNG ÁNH XẠ SCHEMA: SKILL 1 → usecase_registry.csv

Skill 1 dùng 9 fields Python dict. usecase_registry.csv có 23 cột. Bảng ánh xạ:

| Field Skill 1 | Cột usecase_registry.csv | Ghi chú xử lý |
|---|---|---|
| `department` | `khoi_chuc_nang` | Map sang mã khối (FO/MO/BO/EN + tên khối con) |
| `use_case_name` | `ten_use_case` | Giữ nguyên, chuẩn hóa: Động từ + Tân ngữ + Ngữ cảnh |
| `ai_type` | `nang_luc_ai(1-7)` | Convert: NLP→3/4, CV→6, Predictive ML→5, GenAI→4, Agent→7. Ghi số 1-7 theo thang plan |
| `problem` | `van_de_kinh_doanh` | Rút ngắn ≤200 ký tự; nội dung dài hơn → file `.md` riêng, ghi `chi_tiet_ref` |
| `current_process` | `quy_trinh_hien_tai_theo_buoc` | Giữ nguyên step-by-step, ≤200 ký tự/ô |
| `ai_intervention` | `ai_lam_gi_o_buoc_nao` | Chỉ đích danh bước số mấy theo `current_process` |
| `kpi` | `kpi_cai_thien` | Giữ nguyên |
| `roi` | `uoc_tinh_roi` | Giữ nguyên; gắn `[INFERENCE]` nếu không có nguồn T1/T2 |
| `source` | `source_ids` | PHẢI convert sang `source_id` format (S-T1-001...) trong SOURCE_REGISTRY.csv TRƯỚC khi ghi. URL trong source của Skill 1 → đăng ký → lấy source_id |
| *(không có)* | `uc_id` | ORCHESTRATOR tự gán: `UC-{KHOI}-###` |
| *(không có)* | `task_id_lien_ket` | A10 PHẢI gắn về task_id trong task_registry — đây là trường validate quan trọng nhất |
| *(không có)* | `muc_tu_dong` | A10 tự điền: assist/copilot/autonomous dựa trên `hau_qua_sai` |
| *(không có)* | `human_in_the_loop` | A10 tự điền theo logic plan Mục 3.5 câu hỏi 4 |
| *(không có)* | `diem_gia_tri/kha_thi/du_lieu/rui_ro` | A11 điền ở Phase 6 |
| *(không có)* | `muc_do (VERIFIED/CATALOGUE)` | A10 điền dựa trên đủ 6/3-5 câu hỏi kiểm chứng |
| `source` badge HTML | *(không map vào CSV)* | HTML badge → giữ trong file `.md` deep dive, không nhét vào CSV |

**Cột KHÔNG CÓ trong Skill 1, A10 phải tự điền từ task_registry:**
- `tang` (FO/MO/BO/EN)
- `rang_buoc_phap_ly`
- `du_lieu_can_co`
- `ro` (quick_win/chien_luoc/nghien_cuu) — do A11 điền ở Phase 6

---

## 5. XUNG ĐỘT PHÁT HIỆN — PLAN CHƯA NÓI TỚI

### XĐ-1: Skill 3 (Use Case Deep Dive) — FILE RỖNG

**Mức độ: BLOCKER cho mục tiêu "Deep dive 20 UC"**

Skill 3 (`skill-3-usecase-deepdive.md`) hiện là file rỗng 0 byte. Plan dự án và mục tiêu điều chỉnh đều cần deep dive 20 UC. Hiện tại không có framework chuẩn để thực hiện.

**Đã ghi vào OPEN_QUESTIONS.md:** [OQ-001]

**Đề xuất xử lý (chờ Thư xác nhận):**
- Option A: Tạo Skill 3 từ đầu dựa trên format của Skill 1 Phase 3 (QuoteExtractor) + Skill 2 Phase 4 Deliverable, chuyên biệt cho use case.
- Option B: Dùng tổ hợp Skill 1 Phase 4 (HTML: Deep Dives section) + Skill 2 T9 (Investment Committee Memo) làm framework tạm cho 20 UC.
- ORCHESTRATOR đề xuất Option B vì triển khai được ngay, không cần thêm skill mới.

### XĐ-2: Fact-check 100 UC — quy trình chưa được định nghĩa đầy đủ trong plan

**Mức độ: HIGH**

Mục tiêu điều chỉnh yêu cầu "Fact-check 2 nguồn cho ĐÚNG 100 use case". PLAN gốc (T7.1) có Red Team audit lấy mẫu 25 source, 40 dòng — không phải fact-check có hệ thống cho 100 UC. Skill 1 Phase 3 (QuoteExtractorAgent) có protocol nhưng thiết kế cho fact-check toàn bộ batch, không phải filter 100 UC trước.

**Cần bổ sung task mới:** T5.3 — Filter 100 UC (sau T5.2 Dedup) → T5.4 QuoteExtractor cho 100 UC này → rồi mới sang T6.1 Scoring toàn bộ registry.

### XĐ-3: HTML output path xung đột

**Mức độ: LOW**

Skill 1 hardcode output path theo pattern `{USER_OUTPUT_DIR}/{industry}_ai_report.html`. Dự án này output phải vào `12_report/FINAL_REPORT.html` (theo A13 task T7.2). Cần override khi gọi Skill 1 Phase 4.

### XĐ-4: Subagent scratch path hardcode tên user khác

**Mức độ: MEDIUM**

Skill 1 dùng path `/Users/tungchi/.gemini/antigravity/brain/` (người dùng khác). Cần override thành path của workspace hiện tại tại thời điểm gọi Skill 1.

### XĐ-5: Skill 2 "Investment View Signal" không phù hợp với output nội bộ

**Mức độ: LOW**

Skill 2 bắt buộc mỗi báo cáo mở đầu bằng OVERWEIGHT/NEUTRAL/UNDERWEIGHT. Đây là yêu cầu sell-side. Dự án này dùng `--mode buy-side` (internal), nên điều kiện này được nới: Investment View Signal là optional cho các artifact nghiên cứu nội bộ (A2, A3, A6), bắt buộc chỉ cho báo cáo T7.2 Final Report phần Executive Summary.

### XĐ-6: Skill 1 scaling rule không phù hợp với domain ngành quỹ

**Mức độ: MEDIUM**

Skill 1 Scaling Rules: "IF UCs > 200 → 10-15 subagents, chia batch theo domain". Domain của Skill 1 là domain chuyên biệt ngành (e.g., "chẩn đoán", "dược"). Dự án này chia theo **khối chức năng** (FO/MO/BO/EN × 12-15 khối). Số subagent cần điều chỉnh: 1 subagent per khối chức năng = tối đa 15 subagents.

---

## 6. TÓM TẮT OVERRIDE THEO PHASE

| Phase | Override chính |
|---|---|
| Phase 5 (Skill 1 gọi) | Xóa quota "ĐÚNG 20 UC"; domain = khối chức năng (không phải ngành tổng); truyền `task_registry.csv` làm input bắt buộc |
| Phase 5 fact-check | Chỉ chạy QuoteExtractor trên 100 UC được lọc (không phải toàn bộ) |
| Phase 6 (Skill 1 scoring) | Dùng công thức 4 trục của plan, không dùng Tier 1/2/3 độc lập; chấm toàn bộ registry |
| Phase 7 HTML output | Override output path → `12_report/FINAL_REPORT.html`; Deep Dives = 20 (không phải 10) |
| Mọi phase dùng Skill 2 | Mode = buy-side; Investment View Signal = optional (nội bộ) |
| Mọi phase | SOURCE_REGISTRY.csv là gating: không có source_id → không được trích |

---

*SKILL_INTEGRATION_MAP.md — Tài liệu sống, cập nhật khi phát sinh xung đột mới*
*A0 ORCHESTRATOR là bên duy nhất chỉnh sửa file này*
