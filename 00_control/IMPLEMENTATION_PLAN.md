# IMPLEMENTATION PLAN — FUND INDUSTRY & DRAGON CAPITAL AI USE-CASE RESEARCH

**Phiên bản:** v2.0 (sửa 2026-08-15: gỡ chỉ tiêu số lượng)
**Chế độ chạy:** Google Antigravity — Multi-Agent, artifact-based handoff
**Ngôn ngữ làm việc:** Tiếng Việt (thuật ngữ chuyên ngành giữ nguyên tiếng Anh)
**Chủ dự án:** Thư
**Thời lượng:** 10 tuần (có thể nén còn 5 tuần nếu chạy song song tối đa)

> ⛔ **CẢNH BÁO — CHỈ TIÊU SỐ LƯỢNG ĐÃ BỊ GỠ (hiệu lực từ 2026-08-15)**
>
> Bản v1 của kế hoạch này đặt ngưỡng số lượng làm điều kiện qua gate.
> Điều đó đã gây ra lần chạy hỏng ngày 14/08/2026: 355 tác vụ sinh bằng
> random.choice, 86 nguồn độn, 60 văn bản pháp luật không tồn tại.
>
> **Từ nay:** số lượng là **KẾT QUẢ ĐƯỢC BÁO CÁO**, không phải mục tiêu.
> Con số nhỏ nhưng có thật luôn được chấp nhận.
> Đạt chỉ tiêu bằng dữ liệu suy đoán là **lỗi nghiêm trọng nhất** dự án này.
>
> Mọi dòng "≥ N dòng / ≥ N nguồn" trong file này đã được đổi thành
> "Báo cáo con số thật đạt được". Tiêu chí **chất lượng và truy vết** giữ nguyên.

---

## 0. CÁCH NẠP FILE NÀY VÀO ANTIGRAVITY

1. Tạo workspace mới tên `fund-research`.
2. Copy toàn bộ file này vào `/00_control/IMPLEMENTATION_PLAN.md`.
3. Tách 3 khối sau thành file riêng (agent đọc trước mỗi task):
   - Mục 3 → `/00_control/GLOBAL_RULES.md`
   - Mục 4 → `/00_control/SCHEMAS.md`
   - Mục 5 → `/00_control/AGENT_ROSTER.md`
4. Khởi động bằng prompt cho ORCHESTRATOR ở Mục 10.
5. Mọi agent **bắt buộc** đọc `GLOBAL_RULES.md` + `SCHEMAS.md` trước khi ghi bất kỳ artifact nào.

---

## 1. MỤC TIÊU & ĐỊNH NGHĨA "DONE"

### 1.1 Mục tiêu cuối

Tạo ra một danh mục **300–400 AI use case** cho ngành quản lý quỹ tại Việt Nam, neo vào Dragon Capital (DCVFM), trong đó:

- **80–120 use case ở mức VERIFIED** — trả lời đủ 6/6 câu hỏi kiểm chứng (Mục 3.5)
- **200–280 use case ở mức CATALOGUE** — trả lời tối thiểu 3/6

### 1.2 Deliverable bắt buộc (12 artifact)

| #   | Artifact                                          | File                                        | Owner |
| --- | ------------------------------------------------- | ------------------------------------------- | ----- |
| D1  | Glossary 200 thuật ngữ                          | `/01_lexicon/GLOSSARY.md`                 | A1    |
| D2  | Bản đồ ngành toàn cầu + sơ đồ dòng vốn | `/02_industry_global/GLOBAL_MAP.md`       | A2    |
| D3  | Bản đồ ngành VN + khung pháp lý             | `/03_industry_vn/VN_MAP.md`               | A3    |
| D4  | Ma trận segmentation 6 trục                     | `/04_segmentation/SEGMENTATION_MATRIX.md` | A4    |
| D5  | P&L mẫu + unit economics công ty QLQ            | `/05_business_model/UNIT_ECONOMICS.md`    | A5    |
| D6  | Value chain 3 tầng, đến cấp 3                 | `/06_value_chain/VALUE_CHAIN.md`          | A6    |
| D7  | Task taxonomy rút từ vendor                     | `/07_vendor_taxonomy/VENDOR_TAXONOMY.md`  | A7    |
| D8  | Giải phẫu Dragon Capital                        | `/08_company_dragoncapital/DC_ANATOMY.md` | A8    |
| D9  | 18 thẻ role + 250–300 tác vụ nguyên tử      | `/_data/task_registry.csv`                | A9    |
| D10 | Danh mục use case                                | `/_data/usecase_registry.csv`             | A10   |
| D11 | Bảng chấm điểm + Top 30 ưu tiên             | `/11_scoring/PRIORITY.md`                 | A11   |
| D12 | Báo cáo tổng hợp                              | `/12_report/FINAL_REPORT.md`              | A13   |

### 1.3 Điều kiện DONE của toàn dự án

- [ ] `task_registry.csv`: Báo cáo con số thật đạt được (không trùng lặp sau dedup)
- [ ] `usecase_registry.csv`: Báo cáo con số thật đạt được — phân tách VERIFIED / CATALOGUE
- [ ] `SOURCE_REGISTRY.csv`: Báo cáo con số thật đạt được — phân tách theo Tier
- [ ] Mọi dòng use case đều truy vết được về ≥ 1 `task_id` và ≥ 1 `source_id` *(tiêu chí chất lượng — giữ nguyên)*
- [ ] Agent A12 (Red Team) đã audit và đóng toàn bộ finding mức HIGH
- [ ] Tỷ lệ dòng gắn `[INFERENCE]` được báo cáo trung thực (không có ngưỡng bắt buộc)

---

## 2. CẤU TRÚC THƯ MỤC

```
fund-research/
├── 00_control/
│   ├── IMPLEMENTATION_PLAN.md      # file này
│   ├── GLOBAL_RULES.md             # Mục 3
│   ├── SCHEMAS.md                  # Mục 4
│   ├── AGENT_ROSTER.md             # Mục 5
│   ├── TASK_BOARD.md               # trạng thái từng task, ORCHESTRATOR cập nhật
│   ├── OPEN_QUESTIONS.md           # câu hỏi cần Thư trả lời / cần phỏng vấn
│   ├── ASSUMPTIONS.md              # mọi giả định đang dùng
│   └── CHANGELOG.md
├── 01_lexicon/
├── 02_industry_global/
├── 03_industry_vn/
│   └── legal/                      # trích yếu từng văn bản pháp luật
├── 04_segmentation/
├── 05_business_model/
├── 06_value_chain/
│   └── processes/                  # 1 file .md cho mỗi quy trình cấp 2
├── 07_vendor_taxonomy/
├── 08_company_dragoncapital/
│   ├── entities/
│   ├── funds/                      # 1 file cho mỗi quỹ
│   └── docs/                       # bản cáo bạch, BCTC đã tải
├── 09_roles_tasks/
│   └── role_cards/                 # 1 file .md cho mỗi role
├── 10_usecases/
│   └── by_function/                # use case chia theo khối chức năng
├── 11_scoring/
├── 12_report/
└── _data/
    ├── SOURCE_REGISTRY.csv
    ├── task_registry.csv
    ├── usecase_registry.csv
    ├── role_cards.json
    └── entity_map.json
```

**Quy tắc ghi file:** agent chỉ được ghi vào thư mục mình sở hữu + `_data/` của mình. Muốn sửa artifact của agent khác → ghi request vào `OPEN_QUESTIONS.md`, ORCHESTRATOR xử lý.

---

## 3. GLOBAL_RULES.md — LUẬT CHUNG CHO MỌI AGENT

### 3.1 Nhãn bằng chứng (bắt buộc ở mọi dòng dữ kiện)

| Nhãn              | Nghĩa                              | Yêu cầu                                               |
| ------------------ | ----------------------------------- | ------------------------------------------------------- |
| `[FACT]`         | Sự kiện xác minh được         | Bắt buộc có`source_id`                             |
| `[DATA]`         | Số liệu định lượng            | Bắt buộc có`source_id` + kỳ dữ liệu + đơn vị |
| `[CASE]`         | Case study có thật                | Bắt buộc có tên tổ chức +`source_id`            |
| `[REG]`          | Quy định pháp luật              | Bắt buộc có số hiệu văn bản + điều khoản      |
| `[INFERENCE]`    | Suy luận từ dữ kiện             | Bắt buộc ghi rõ suy luận từ dòng nào             |
| `[HYPOTHESIS]`   | Giả thuyết chưa có bằng chứng | Bắt buộc ghi cách kiểm chứng                       |
| `[VENDOR CLAIM]` | Tuyên bố từ nhà cung cấp       | Không được dùng làm bằng chứng ROI              |
| `[UNVERIFIED]`   | Không xác minh được            | Giữ lại nhưng không đưa vào kết luận           |

### 3.2 Phân hạng nguồn

| Tier         | Loại                            | Ví dụ                                                                                                                                                  |
| ------------ | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **T1** | Nguồn sơ cấp/pháp lý        | Bản cáo bạch, điều lệ quỹ, BCTC kiểm toán, BC thường niên, văn bản pháp luật, CBTT trên HOSE/HNX/VSDC/SSC, annual report VEIL trên LSE |
| **T2** | Tổ chức có thẩm quyền       | ICI, EFAMA, CFA Institute, BIS, IMF, IOSCO, McKinsey/BCG/Bain/Big4, Cerulli, Broadridge                                                                  |
| **T3** | Ngành & dữ liệu thị trường | FiinGroup, Vietstock, Fmarket, tài liệu vendor (SimCorp, Aladdin, CRD), JD tuyển dụng                                                                |
| **T4** | Báo chí & cộng đồng         | CafeF, VnEconomy, blog, forum                                                                                                                            |

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

---

## 4. SCHEMAS.md — CHUẨN DỮ LIỆU HANDOFF

### 4.1 `SOURCE_REGISTRY.csv`

```
source_id, tier, loai_nguon, tieu_de, to_chuc_phat_hanh, url, ngay_xuat_ban,
ngay_truy_cap, ngon_ngu, do_tin_cay(1-5), pham_vi_dung, ghi_chu
```

`source_id` format: `S-T1-001`, `S-T3-047`.

### 4.2 `task_registry.csv` — artifact quan trọng nhất của dự án

```
task_id, tang, khoi_chuc_nang, quy_trinh_cap2, tac_vu_cap3, mo_ta_ngan,
input, nguon_input, output, nguoi_nhan_output, role_chinh, role_phu,
tan_suat, thoi_luong_uoc_tinh_phut, he_thong_dung, buoc_thu_cong,
diem_gay_pain_point, rang_buoc_phap_ly, do_tin_cay(FACT/INFERENCE),
source_ids, chi_tiet_ref
```

`task_id` format: `{TANG}-{KHOI}-{QT}-{TV}` → ví dụ `FO-RES-03-02`, `BO-NAV-01-04`.

Mã tầng: `FO` (front), `MO` (middle), `BO` (back), `EN` (enabling).
Mã khối gợi ý: `PROD, IR, RES, IDEA, PC, TRD, MON` (FO) · `RSK, CMP, PERF, VAL, OPSO` (MO) · `STL, REC, NAV, FA, TA, CA, CUS, TAX` (BO) · `DATA, IT, LEG, HR, FIN, MKT` (EN).

### 4.3 `usecase_registry.csv` — 18 cột

```
uc_id, task_id_lien_ket, tang, khoi_chuc_nang, ten_use_case,
van_de_kinh_doanh, quy_trinh_hien_tai_theo_buoc, ai_lam_gi_o_buoc_nao,
nang_luc_ai(1-7), muc_tu_dong(assist/copilot/autonomous), human_in_the_loop,
kpi_cai_thien, uoc_tinh_roi, du_lieu_can_co, rang_buoc_phap_ly,
diem_gia_tri(1-5), diem_kha_thi(1-5), diem_du_lieu(1-5), diem_rui_ro(1-5),
tong_diem, ro(quick_win/chien_luoc/nghien_cuu), muc_do(VERIFIED/CATALOGUE),
source_ids
```

`uc_id` format: `UC-{KHOI}-###`.

### 4.4 `role_cards.json`

```json
{
  "role_id": "FO-PM-EQ",
  "chuc_danh": "Portfolio Manager – Equity",
  "khoi": "Front Office",
  "bao_cao_cho": "CIO",
  "nhip_lam_viec": {"daily": [], "weekly": [], "monthly": [], "quarterly": [], "ad_hoc": []},
  "tac_vu": ["task_id", "..."],
  "he_thong_dung": [],
  "tac_vu_ton_thoi_gian_nhat": "",
  "loi_thuong_gap": [],
  "kpi_bi_cham": [],
  "do_tin_cay": "FACT|INFERENCE",
  "source_ids": []
}
```

### 4.5 `entity_map.json`

```json
{
  "entity_id": "",
  "ten_phap_nhan": "",
  "ma_ck": "",
  "vai_tro_trong_group": "",
  "nghiep_vu_duoc_cap_phep": [],
  "san_pham_quan_ly": [],
  "co_quan_quan_ly": [],
  "nghia_vu_cbtt": [],
  "source_ids": []
}
```

---

## 5. AGENT_ROSTER.md — 13 AGENT + 1 ORCHESTRATOR

| ID            | Tên agent           | Vai trò                                                          | Sở hữu thư mục                         | Công cụ cần        |
| ------------- | -------------------- | ----------------------------------------------------------------- | ------------------------------------------ | --------------------- |
| **A0**  | ORCHESTRATOR         | Điều phối, cập nhật TASK_BOARD, giải xung đột, gate check | `00_control/`                            | —                    |
| **A1**  | LEXICON              | Xây từ vựng & mô hình tư duy ngành                         | `01_lexicon/`                            | Web                   |
| **A2**  | GLOBAL_ANALYST       | Bản đồ ngành toàn cầu, dòng vốn, xu hướng               | `02_industry_global/`                    | Web, PDF              |
| **A3**  | VN_ANALYST           | Thị trường VN + khung pháp lý                                | `03_industry_vn/`                        | Web, PDF              |
| **A4**  | SEGMENTER            | Ma trận phân khúc 6 trục                                      | `04_segmentation/`                       | Web                   |
| **A5**  | ECONOMIST            | Business model & unit economics                                   | `05_business_model/`                     | Web, PDF, tính toán |
| **A6**  | VALUECHAIN_ARCHITECT | Value chain 3 tầng đến cấp 3                                  | `06_value_chain/`                        | Web, PDF              |
| **A7**  | VENDOR_MINER         | Rút task taxonomy từ tài liệu vendor & JD                     | `07_vendor_taxonomy/`                    | Web, browser          |
| **A8**  | COMPANY_ANALYST      | Giải phẫu Dragon Capital                                        | `08_company_dragoncapital/`              | Web, browser, PDF     |
| **A9**  | ROLE_TASK_ENGINEER   | Thẻ role + tác vụ nguyên tử                                  | `09_roles_tasks/`, `task_registry.csv` | —                    |
| **A10** | USECASE_GENERATOR    | Sinh use case từ ma trận task × năng lực AI                  | `10_usecases/`, `usecase_registry.csv` | —                    |
| **A11** | SCORER               | Chấm điểm, xếp rổ, chọn Top 30                              | `11_scoring/`                            | Tính toán           |
| **A12** | RED_TEAM             | Audit độc lập: bịa, trùng, thiếu nguồn, logic sai          | ghi vào`AUDIT_LOG.md`                   | Web                   |
| **A13** | WRITER               | Viết báo cáo cuối                                             | `12_report/`                             | —                    |

### 5.1 Nguyên tắc phối hợp

- **A12 không bao giờ chạy cùng lượt với agent nó audit.** Audit chạy sau khi artifact được đánh dấu `READY_FOR_AUDIT`.
- **A9 và A10 là nút cổ chai** — mọi agent thượng nguồn phải xong trước.
- Agent không được sửa artifact của agent khác. Chỉ đề xuất qua `OPEN_QUESTIONS.md`.
- Mỗi agent kết thúc task bằng việc ghi block `## HANDOFF` cuối artifact: đã tạo gì, giả định gì, còn thiếu gì, agent kế tiếp cần lưu ý gì.

---

## 6. SƠ ĐỒ PHỤ THUỘC (DAG)

```
                    ┌── A1 LEXICON ──┐
                    │                │
        ┌───────────┼────────────────┼───────────┐
        │           │                │           │
   A2 GLOBAL    A3 VN_MARKET    A7 VENDOR    A8 COMPANY_DC
        │           │                │           │
        └─────┬─────┘                │           │
              │                      │           │
        A4 SEGMENT                   │           │
              │                      │           │
        A5 ECONOMICS                 │           │
              │                      │           │
              └──────► A6 VALUECHAIN ◄───────────┘
                              │
                       A9 ROLE_TASK  ◄── [PHỎNG VẤN SƠ CẤP]
                              │
                       A10 USECASE_GEN
                              │
                        A11 SCORER
                              │
                       A12 RED_TEAM (audit toàn tuyến)
                              │
                        A13 WRITER
```

**Chạy song song được:** {A2, A3, A7, A8} sau khi A1 xong. Đây là 4 luồng nặng nhất → nén được 3 tuần.

---

## 7. TASK BOARD — TỪNG TASK CHI TIẾT

Format mỗi task: `ID | Agent | Phụ thuộc | Input | Các bước | Output | Tiêu chí nghiệm thu`

---

### PHASE 0 — SETUP (Ngày 1)

#### T0.1 | A0 | — | Khởi tạo workspace

**Các bước:**

1. Tạo toàn bộ cây thư mục ở Mục 2.
2. Tách `GLOBAL_RULES.md`, `SCHEMAS.md`, `AGENT_ROSTER.md` ra file riêng.
3. Tạo 5 file CSV/JSON rỗng với đúng dòng header ở Mục 4.
4. Tạo `TASK_BOARD.md` với toàn bộ task ở Mục 7, trạng thái `TODO`.
5. Tạo `ASSUMPTIONS.md`, `OPEN_QUESTIONS.md`, `CHANGELOG.md`, `AUDIT_LOG.md`.

**Nghiệm thu:** cây thư mục đủ, header CSV đúng chính tả từng cột, TASK_BOARD liệt kê đủ số task.

---

### PHASE 1 — NỀN TẢNG (Tuần 1)

#### T1.1 | A1 | T0.1 | Xây glossary 200 thuật ngữ

**Input:** CFA curriculum outline (Portfolio Management), ICI Fact Book, glossary công khai của SimCorp / Northern Trust / BNY / Investment Company Institute.

**Các bước:**

1. Gom thuật ngữ theo 8 nhóm: *Cấu trúc quỹ · Đầu tư & danh mục · Giao dịch & thực thi · Vận hành & thanh toán · Định giá & NAV · Rủi ro & tuân thủ · Đo lường hiệu quả · Phân phối & khách hàng*.
2. Mỗi thuật ngữ ghi: tiếng Anh | tiếng Việt | định nghĩa ≤ 40 từ | ai dùng thuật ngữ này | vì sao nó quan trọng.
3. Đánh dấu 30 thuật ngữ "cốt lõi" — nếu không hiểu 30 từ này thì không đọc được bản cáo bạch.
4. Với 15 thuật ngữ vận hành phức tạp nhất (NAV strike, dealing cut-off, reconciliation, corporate action, PCF, creation/redemption basket, trade break, T+n settlement, fair value pricing, swing pricing, side pocket, subscription in-kind, soft dollar, best execution, dilution levy), viết thêm đoạn "cơ chế hoạt động" ≤ 120 từ.

**Output:** `/01_lexicon/GLOSSARY.md` + `/01_lexicon/CORE_30.md`

**Nghiệm thu:**

- Báo cáo số mục thật đạt được; 100% mục có `source_id` *(tiêu chí chất lượng — giữ nguyên)*
- Có đủ 15 đoạn "cơ chế hoạt động"
- Test tự kiểm: agent phải viết được đoạn 150 từ trả lời *"Vì sao NAV chốt T+1 chứ không real-time, và điều đó tạo ra pain point vận hành gì?"* — đặt ở cuối `CORE_30.md`

---

### PHASE 2 — 4 LUỒNG SONG SONG (Tuần 2–4)

#### T2.1 | A2 | T1.1 | Bản đồ ngành toàn cầu

**Các bước:**

1. **Dòng vốn:** vẽ sơ đồ Asset Owner (hộ gia đình, quỹ hưu trí, bảo hiểm, SWF, endowment) → Distributor/Advisor → Asset Manager → Custodian/Broker → Thị trường. Ghi rõ ai trả phí cho ai, ở khâu nào.
2. **Quy mô & cấu trúc:** AUM toàn cầu, tỷ trọng active/passive, tỷ trọng theo asset class, tốc độ tăng trưởng 10 năm. Nguồn: ICI Fact Book, BCG Global Asset Management report, EFAMA.
3. **Kinh tế học ngành:** xu hướng fee compression (số liệu TER trung bình 10 năm), dịch chuyển sang passive, dịch chuyển sang private markets, hợp nhất ngành.
4. **Top 15 nhà quản lý toàn cầu:** AUM, mô hình, nguồn doanh thu chính, chiến lược công nghệ. Lấy từ annual report của BlackRock, Vanguard, Fidelity, Amundi, Schroders.
5. **Timeline 5 giai đoạn phát triển ngành** — từ mutual fund cổ điển → institutional → passive/ETF → alternatives → data & platform. Ghi rõ mỗi giai đoạn thay đổi cái gì trong value chain.

**Output:** `/02_industry_global/GLOBAL_MAP.md`

**Nghiệm thu:** Báo cáo số `[DATA]` thật đạt được (có kỳ và nguồn); sơ đồ dòng vốn ghi rõ 6 loại phí; timeline có mốc năm cụ thể.

---

#### T2.2 | A3 | T1.1 | Bản đồ ngành Việt Nam + khung pháp lý

**Các bước:**

1. **Landscape:** danh sách toàn bộ công ty QLQ được cấp phép (nguồn SSC), AUM, số quỹ, loại quỹ. Xếp hạng thị phần.
2. **Cấu trúc thị trường:** số lượng và quy mô quỹ mở / ETF / quỹ thành viên / quỹ đóng / quỹ hưu trí bổ sung tự nguyện; số tài khoản NĐT; kênh phân phối (trực tiếp, CTCK, ngân hàng, Fmarket).
3. **Khung pháp lý — đọc và trích yếu từng văn bản**, mỗi văn bản một file trong `/03_industry_vn/legal/`:
   - Luật Chứng khoán 54/2019/QH14
   - Nghị định 155/2020/NĐ-CP
   - Thông tư 98/2020/TT-BTC — hoạt động và quản lý quỹ đầu tư chứng khoán
   - Thông tư 99/2020/TT-BTC — hoạt động của công ty quản lý quỹ
   - Thông tư 96/2020/TT-BTC — công bố thông tin
   - Quy định về phòng chống rửa tiền áp dụng cho công ty QLQ
   - **Bắt buộc kiểm tra hiệu lực và văn bản sửa đổi/thay thế mới nhất tại thời điểm chạy** — ghi ngày kiểm tra
4. **Trích xuất nghĩa vụ → tác vụ:** đây là bước tạo giá trị lớn nhất. Quét từng văn bản, mỗi cụm *"phải báo cáo / phải lưu trữ / phải kiểm tra / phải định giá / phải công bố / phải giám sát"* → tạo một dòng ứng viên tác vụ với format:
   ```
   [REG] Văn bản | Điều khoản | Nghĩa vụ | Tần suất | Ai làm | → task ứng viên
   ```

   Ghi vào `/03_industry_vn/legal/REG_TASK_CANDIDATES.csv`.
5. **So sánh VN vs chuẩn quốc tế:** VN thiếu gì (fund admin độc lập, prime broker, securities lending, chuẩn GIPS…) → đây là white-space.

**Output:** `/03_industry_vn/VN_MAP.md`, `/03_industry_vn/legal/*.md`, `REG_TASK_CANDIDATES.csv`

**Nghiệm thu:**

- Báo cáo số văn bản pháp lý thật được trích yếu; mỗi văn bản ghi rõ ngày kiểm tra hiệu lực *(tiêu chí chất lượng — giữ nguyên)*
- `REG_TASK_CANDIDATES.csv`: Báo cáo con số thật đạt được
- Có bảng so sánh VN vs quốc tế — báo cáo số hạng mục thật so sánh được

---

#### T2.3 | A7 | T1.1 | Rút task taxonomy từ vendor & JD *(luồng cho sản lượng cao nhất)*

**Các bước:**

1. **Khai thác tài liệu vendor.** Với mỗi hệ thống dưới đây, lấy danh mục module/chức năng từ trang sản phẩm, datasheet, user guide public, tài liệu API:
   - Front-to-back: SimCorp Dimension, BlackRock Aladdin, Charles River IMS, Enfusion, SS&C Eze
   - Fund accounting & NAV: SS&C, Clearwater, FIS InvestOne
   - Compliance & reporting: Confluence, Bloomberg AIM compliance module
   - Data & research: FactSet, Bloomberg, Refinitiv Workspace, S&P Capital IQ
   - Transfer agency & phân phối: Calastone, MFEX/Euroclear, Fmarket (VN)
2. **Chuẩn hóa:** mỗi module → ánh xạ về tầng (FO/MO/BO/EN) và khối chức năng. Gộp trùng giữa các vendor.
3. **Khai thác Job Description.** Thu ≥ 60 JD:
   - VN: DCVFM, VinaCapital, SSIAM, VCBF, MBCapital, BVF, Techcom Capital, VCBF, PVI AM
   - Quốc tế cùng chức danh: PM, Analyst, Fund Accountant, Compliance Officer, Performance Analyst, TA Operations
   - Mỗi JD → bóc thành danh sách tác vụ dạng động từ + tân ngữ ("đối chiếu giao dịch với ngân hàng giám sát", "tính NAV cuối ngày")
4. **Khai thác DDQ/RFP template.** Lấy mẫu DDQ của institutional investor (AIMA, ILPA, các mẫu operational due diligence public). Mỗi câu hỏi → suy ra một quy trình bắt buộc phải tồn tại.
5. Hợp nhất 3 nguồn thành cây taxonomy 3 cấp: **Khối → Quy trình → Tác vụ**, đánh dấu tác vụ nào xuất hiện ở ≥ 2 nguồn (độ tin cậy cao).

**Output:** `/07_vendor_taxonomy/VENDOR_TAXONOMY.md` + `/07_vendor_taxonomy/TASK_CANDIDATES.csv`

**Nghiệm thu:**

- Báo cáo số hệ thống thật được khai thác
- Báo cáo số JD thật được bóc tách
- `TASK_CANDIDATES.csv`: Báo cáo con số thật đạt được (chưa dedup)
- Mỗi dòng ghi rõ xuất hiện ở mấy nguồn *(tiêu chí chất lượng — giữ nguyên)*

---

#### T2.4 | A8 | T1.1 | Giải phẫu Dragon Capital

**Các bước:**

1. **Entity map.** Tách rõ ba lớp, ghi vào `entity_map.json`:
   - Dragon Capital Group (gốc offshore, 1994) — quản lý VEIL niêm yết London
   - DCVFM / Dragon Capital Vietfund Management (pháp nhân nội địa, hợp nhất Dragon Capital + VFM năm 2021, mã UPCoM `DCV`)
   - Các đơn vị vệ tinh trong hệ sinh thái
     Với mỗi pháp nhân: nghiệp vụ được cấp phép, cơ quan quản lý, nghĩa vụ CBTT.
2. **Fund map.** Mỗi quỹ một file trong `/08_company_dragoncapital/funds/`:
   - Quỹ mở: DCDS, DCBC, DCBF, DCIP, VFMVSF (kiểm tra danh sách hiện hành)
   - ETF: DCVFMVN30, DCVFM VNDIAMOND, DCVFM VNMIDCAP
   - VEIL (offshore, LSE)
   - Trường thông tin: loại quỹ, ngày thành lập, chiến lược, benchmark, biểu phí, ngân hàng giám sát, đại lý chuyển nhượng, quy mô, tần suất giao dịch, cut-off time
3. **Khai thác bản cáo bạch — nguồn giàu nhất.** Với mỗi quỹ, tải bản cáo bạch + điều lệ và bóc ra:
   - Quy trình đăng ký mua / bán / chuyển đổi CCQ theo từng bước, kèm thời điểm cut-off
   - Phương pháp xác định NAV, nguồn giá, xử lý chứng khoán khó định giá
   - Vai trò và ranh giới trách nhiệm: công ty QLQ / ngân hàng giám sát / đại lý chuyển nhượng / kiểm toán
   - Hạn mức đầu tư và cơ chế xử lý khi vi phạm
   - Nghĩa vụ báo cáo định kỳ và tần suất
     → Mỗi cụm trên là một quy trình có thật, ghi vào `/08_company_dragoncapital/PROCESS_FROM_PROSPECTUS.csv`
4. **Kinh tế học công ty.** Từ BCTC + BC thường niên của `DCV` và BCTC quỹ đã kiểm toán: cơ cấu doanh thu, cơ cấu chi phí, headcount nếu có, xu hướng 3–5 năm.
5. **Cơ cấu tổ chức.** Từ BC thường niên + BC quản trị + LinkedIn: các khối chuyên môn, chức danh cấp quản lý. **Không suy đoán chức danh không có nguồn.**
6. **Nhịp vận hành.** Từ lịch công bố NAV, báo cáo định kỳ, báo cáo danh mục hàng tháng → dựng lịch nghiệp vụ ngày/tuần/tháng/quý.
7. **Đối chứng VEIL.** Annual report của VEIL trên LSE viết bằng tiếng Anh theo chuẩn quốc tế → dùng để suy ra chuẩn vận hành nội bộ của group.

**Output:** `/08_company_dragoncapital/DC_ANATOMY.md`, `entity_map.json`, `funds/*.md`, `PROCESS_FROM_PROSPECTUS.csv`

**Nghiệm thu:**

- Entity map tách đúng các lớp pháp nhân (báo cáo số lớp tìm được)
- Báo cáo số quỹ có file riêng đầy đủ trường
- `PROCESS_FROM_PROSPECTUS.csv`: Báo cáo con số thật đạt được
- Mọi dòng dữ kiện về Dragon Capital phải gắn nguồn T1 hoặc gắn `[UNVERIFIED]` *(tiêu chí chất lượng — giữ nguyên)*
- Mọi chức danh cụ thể đều có `source_id` *(tiêu chí chất lượng — giữ nguyên)*

---

### PHASE 3 — TỔNG HỢP (Tuần 4–5)

#### T3.1 | A4 | T2.1, T2.2 | Ma trận segmentation 6 trục

**Các bước:**

1. Dựng ma trận theo 6 trục: asset class · cấu trúc pháp lý · chiến lược · nhóm khách hàng · kênh phân phối · quy mô & mô hình vận hành.
2. Định vị Dragon Capital + 9 đối thủ VN vào ô tương ứng.
3. Đánh dấu ô trống (white-space) và ghi giả thuyết vì sao trống — do quy định, do cầu, hay do năng lực.
4. **Quan trọng cho use case:** với mỗi phân khúc, ghi rõ *value chain của phân khúc đó khác nhau ở đâu*. Ví dụ ETF cần PCF hàng ngày và cơ chế creation/redemption với AP — quỹ mở thì không. Đây là nguồn sinh use case chuyên biệt.

**Output:** `/04_segmentation/SEGMENTATION_MATRIX.md`

**Nghiệm thu:** đủ 6 trục; báo cáo số công ty định vị được; báo cáo số điểm khác biệt value chain tìm được.

---

#### T3.2 | A5 | T2.1, T2.2, T2.4 | Business model & unit economics

**Các bước:**

1. Dựng **P&L mẫu** của công ty quản lý quỹ, có công thức:
   - Doanh thu: management fee (% AUM) + performance fee + phí phát hành/mua lại + phí quản lý danh mục ủy thác + phí tư vấn
   - Chi phí: nhân sự · ngân hàng giám sát & đại lý chuyển nhượng & kiểm toán · dữ liệu và terminal · công nghệ · marketing & kênh phân phối · tuân thủ · vận hành chung
2. Tính **điểm hòa vốn theo AUM** với 3 kịch bản cost base (boutique / mid / full-stack). Ghi rõ toàn bộ giả định vào `ASSUMPTIONS.md`.
3. Tính **độ nhạy**: AUM giảm 10/20/30% → lợi nhuận biến động bao nhiêu (operating leverage).
4. Đối chiếu mô hình với số liệu thật từ BCTC `DCV` và 2–3 công ty QLQ niêm yết khác.
5. **Kết luận bắt buộc:** liệt kê 10 hạng mục chi phí lớn nhất và 5 nguồn doanh thu đang bị ép → đây chính là bản đồ "use case nào có tiền".

**Output:** `/05_business_model/UNIT_ECONOMICS.md` + file tính toán

**Nghiệm thu:** P&L có công thức chạy được; báo cáo số kịch bản thật dựng được; giả định ghi đầy đủ; có bảng chi phí lớn nhất xếp hạng.

---

#### T3.3 | A6 | T2.1–T2.4, T3.1 | Value chain 3 tầng đến cấp 3

**Các bước:**

1. Hợp nhất đầu vào từ A2 (chuẩn quốc tế), A7 (module vendor), A8 (quy trình từ bản cáo bạch), A3 (nghĩa vụ pháp lý).
2. Dựng cây 3 cấp:
   - **Cấp 1 — Khối chức năng** (12–15 khối, dùng mã ở Mục 4.2)
   - **Cấp 2 — Quy trình** (4–6 quy trình mỗi khối)
   - **Cấp 3 — Tác vụ** (3–5 tác vụ mỗi quy trình)
3. Mỗi quy trình cấp 2 viết một file riêng trong `/06_value_chain/processes/` gồm: mục đích · trigger · các bước · input/output · vai trò tham gia · hệ thống · tần suất · điểm gãy điển hình · ràng buộc pháp lý.
4. Đánh dấu quy trình nào **khác biệt theo phân khúc** (ETF vs quỹ mở vs mandate).
5. Kiểm đếm: nếu tổng số tác vụ cấp 3 < 250 → chưa đủ sâu, quay lại đào tiếp khối nào mỏng nhất.

**Output:** `/06_value_chain/VALUE_CHAIN.md` + `processes/*.md`

**Nghiệm thu:**

- Báo cáo số khối / quy trình cấp 2 / tác vụ cấp 3 thật đạt được
- Mỗi quy trình cấp 2 có file riêng đủ 9 trường *(tiêu chí chất lượng — giữ nguyên)*
- Mọi tác vụ truy vết được về ≥ 1 nguồn *(tiêu chí chất lượng — giữ nguyên)*

---

### PHASE 4 — XUỐNG ĐÁY: ROLE & TÁC VỤ (Tuần 6–7)

#### T4.1 | A9 | T3.3, T2.3, T2.4 | Dựng 18 thẻ role

**Danh sách role bắt buộc:**

| Khối    | Role                                                                                                                                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Front    | CIO · Head of Research · Sector Analyst · Portfolio Manager (Equity) · Portfolio Manager (Fixed Income) · ETF Portfolio Manager · Trader/Dealer · Quant Analyst · ESG Analyst |
| Middle   | Head of Risk · Compliance Officer · Performance & Attribution Analyst · Valuation Officer                                                                                          |
| Back     | Fund Accountant · Settlement/Operations Officer · Transfer Agency Officer                                                                                                           |
| Enabling | Product Manager · IR & Client Servicing · Sales & Distribution · Data/IT Manager                                                                                                   |

**Các bước:**

1. Với mỗi role, điền đủ 12 trường của `role_cards.json` (Mục 4.4).
2. **Nhịp làm việc là trường quan trọng nhất** — tách rõ việc hằng ngày / tuần / tháng / quý / ad-hoc. Ví dụ Fund Accountant: NAV hằng ngày, đối chiếu hằng ngày, báo cáo NĐT hằng tháng, phối hợp kiểm toán hằng năm.
3. Gắn mỗi role với danh sách `task_id` trong `task_registry.csv`.
4. Đánh dấu `do_tin_cay`: role nào dựng từ nguồn thật (JD, BC thường niên) = `FACT`; role nào suy từ chuẩn ngành = `INFERENCE`.

**Output:** `/09_roles_tasks/role_cards/*.md` + `/_data/role_cards.json`

**Nghiệm thu:** Báo cáo số thẻ role thật dựng được; mỗi thẻ có ít nhất 5 tác vụ; ghi rõ role nào có nguồn JD thật (`FACT`) vs suy luận từ chuẩn ngành (`INFERENCE`).

---

#### T4.2 | A9 | T4.1 | Hợp nhất & chuẩn hóa `task_registry.csv` *(task quan trọng nhất dự án)*

**Các bước:**

1. Gom 4 nguồn ứng viên tác vụ (dùng con số thật từ mỗi nguồn):
   - `/07_vendor_taxonomy/TASK_CANDIDATES.csv` (báo cáo số dòng thật)
   - `/03_industry_vn/legal/REG_TASK_CANDIDATES.csv` (báo cáo số dòng thật)
   - `/08_company_dragoncapital/PROCESS_FROM_PROSPECTUS.csv` (báo cáo số dòng thật)
   - Tác vụ cấp 3 từ `VALUE_CHAIN.md`
2. **Dedup theo ngữ nghĩa, không theo chuỗi ký tự.** Hai dòng mô tả cùng một việc bằng từ khác nhau phải gộp. Giữ lại bản diễn đạt rõ nhất, cộng dồn `source_ids`.
3. Chuẩn hóa cách viết tác vụ: **động từ + tân ngữ + điều kiện**. Ví dụ "Đối chiếu số dư chứng khoán với ngân hàng giám sát cuối ngày giao dịch".
4. Điền đủ 21 cột của schema 4.2. Cột không biết → ghi `KXĐ` (không xác định), **không bịa**.
5. Ước lượng `thoi_luong_uoc_tinh_phut` bằng benchmark ngành, gắn `[INFERENCE]` và ghi cơ sở ước lượng.
6. Điền `diem_gay_pain_point` — trường này quyết định chất lượng use case. Nguồn: tài liệu vendor (họ bán giải pháp cho pain point nào), JD (kỹ năng nào được nhấn mạnh), diễn đàn nghề nghiệp, báo cáo tư vấn.
7. Gắn cờ `can_phong_van = TRUE` cho các dòng chỉ có `[INFERENCE]` ở cả `thoi_luong` và `diem_gay`.

**Output:** `/_data/task_registry.csv`

**Nghiệm thu:**

- Báo cáo con số thật sau dedup; báo cáo phân bố theo khối FO/MO/BO/EN
- 100% dòng có `task_id` đúng format và ≥ 1 `source_id` *(tiêu chí chất lượng — giữ nguyên)*
- Báo cáo tỷ lệ dòng có `KXĐ` ở cột `role_chinh`
- Báo cáo tỷ lệ điền `diem_gay_pain_point`

---

#### T4.3 | A0 | T4.2 | **GATE 1 — Kiểm tra độ sâu trước khi sinh use case**

ORCHESTRATOR chạy checklist, **không đạt thì không được sang Phase 5**:

- [ ] `task_registry.csv`: ORCHESTRATOR báo cáo số dòng thật; nếu có khối chức năng quá mỏng → ghi rõ và giải thích lý do (nguồn chưa đủ, hay thực sự ngành mỏng ở đó)
- [ ] Báo cáo số tác vụ đến từ nguồn T1 của Dragon Capital
- [ ] `SOURCE_REGISTRY.csv`: Báo cáo con số thật theo Tier
- [ ] A12 đã audit `task_registry.csv` và đóng hết finding HIGH *(tiêu chí chất lượng — giữ nguyên)*
- [ ] `OPEN_QUESTIONS.md` không còn mục `BLOCKER` *(tiêu chí chất lượng — giữ nguyên)*

**Nếu fail:** ORCHESTRATOR ghi rõ khối nào thiếu và giao lại task đào sâu cho agent tương ứng.

---

#### T4.4 | Thư (người thật) | T4.2 | Phỏng vấn sơ cấp — *hiệu chỉnh, không thể thay bằng agent*

**Chuẩn bị (agent A9 làm):** từ `task_registry.csv`, sinh bộ câu hỏi phỏng vấn theo từng nhóm role, tập trung vào các dòng gắn cờ `can_phong_van = TRUE`.

**Cấu trúc bộ câu hỏi (agent tạo file `/09_roles_tasks/INTERVIEW_GUIDE.md`):**

1. Mô tả một ngày làm việc điển hình theo trình tự thời gian
2. Việc nào ngốn nhiều thời gian nhất mà bạn thấy đáng lẽ không nên tốn thế?
3. Tháng vừa rồi có sự cố nào phải xử lý gấp? Nguyên nhân gốc là gì?
4. Dữ liệu bạn cần thường nằm ở đâu? Có phải copy tay giữa hệ thống không?
5. Báo cáo nào bạn phải làm mà cảm giác lặp đi lặp lại?
6. Nếu có một trợ lý làm hộ một việc, bạn giao việc gì đầu tiên?
7. Việc nào **tuyệt đối không được** để máy làm? Vì sao?

**Mục tiêu:** 8–12 cuộc — tối thiểu 2 front, 2 middle, 2 back, 1 IT/data, 1 phân phối. Không nhất thiết tại Dragon Capital; VinaCapital, SSIAM, VCBF, MBCapital cho ~80% cùng thông tin và dễ tiếp cận hơn. Kênh: alumni UEH, LinkedIn, hội thảo ngành.

**Sau phỏng vấn:** A9 cập nhật `task_registry.csv` — nâng dòng từ `[INFERENCE]` lên `[FACT]`, sửa ước lượng thời lượng, bổ sung pain point thật.

**Nghiệm thu:** Báo cáo số biên bản thật thực hiện được; báo cáo số dòng task được nâng từ `[INFERENCE]` lên `[FACT]`.

> **Lưu ý thẳng thắn:** nếu bỏ T4.4, độ sâu dự án trần ở khoảng 60% và phần `diem_gay_pain_point` phần lớn sẽ là suy luận. Danh mục use case vẫn dùng được để định hướng, nhưng không nên trình bày như đã xác minh.

---

### PHASE 5 — SINH USE CASE (Tuần 8–9)

#### T5.1 | A10 | T4.3 | Sinh use case theo ma trận task × năng lực AI

**Ma trận 7 năng lực AI:**

| # | Năng lực                    | Dấu hiệu tác vụ phù hợp                                            |
| - | ----------------------------- | ------------------------------------------------------------------------ |
| 1 | Trích xuất & phân loại    | Input là văn bản/PDF không cấu trúc, output là trường dữ liệu |
| 2 | Tóm tắt & tổng hợp        | Input dài, output là bản rút gọn cho người khác đọc            |
| 3 | Tìm kiếm & hỏi đáp (RAG) | Người làm phải "đi tìm" thông tin trong kho tài liệu            |
| 4 | Sinh nội dung                | Output là văn bản theo mẫu lặp lại                                 |
| 5 | Dự báo & định lượng     | Có dữ liệu lịch sử, output là con số dự phóng                   |
| 6 | Phát hiện bất thường     | Có quy tắc/ngưỡng, việc là "soi xem có gì sai"                   |
| 7 | Tác tử/điều phối         | Chuỗi nhiều bước, nhiều hệ thống, quy tắc rõ ràng              |

**Các bước:**

1. Duyệt **tuần tự từng dòng** `task_registry.csv`. Với mỗi task, hỏi 7 câu tương ứng 7 năng lực: *"Năng lực này có giải quyết được phần nào của tác vụ không?"*
2. Chỉ tạo use case khi trả lời **có, kèm lý do cụ thể**. Nếu không → ghi vào `/10_usecases/REJECTED.csv` với lý do (đây là artifact có giá trị, chứng minh đã duyệt hết).
3. Mỗi use case điền đủ 23 cột schema 4.3, đặc biệt:
   - `quy_trinh_hien_tai_theo_buoc`: đánh số bước, ≤ 200 ký tự, chi tiết dài để file .md riêng
   - `ai_lam_gi_o_buoc_nao`: chỉ đích danh bước số mấy
   - `muc_tu_dong`: assist / copilot / autonomous
   - `human_in_the_loop`: quyết định dựa trên `hau_qua_sai` — hậu quả tài chính hoặc pháp lý nghiêm trọng thì bắt buộc có người duyệt
4. **Áp bộ lọc 6 câu hỏi (Mục 3.5).** Đủ 6 → `VERIFIED`. Đủ 3–5 → `CATALOGUE`. Dưới 3 → chuyển sang `REJECTED.csv`.
5. Tỷ lệ kỳ vọng: **1 task sinh trung bình 1,2–1,5 use case hợp lệ.**

**Output:** `/_data/usecase_registry.csv`, `/10_usecases/by_function/*.md`, `/10_usecases/REJECTED.csv`

**Nghiệm thu:**

- Báo cáo con số thật: tổng dòng registry / phân tách VERIFIED vs CATALOGUE
- 100% dòng có `task_id_lien_ket` hợp lệ *(tiêu chí chất lượng — giữ nguyên)*
- `REJECTED.csv`: Báo cáo số dòng thật; nếu tỷ lệ từ chối < 15% → ghi lý do
- Không use case nào chỉ mô tả năng lực AI chung chung mà không neo vào bước cụ thể *(tiêu chí chất lượng — giữ nguyên)*

---

#### T5.2 | A10 | T5.1 | Dedup & chống loãng

**Các bước:**

1. Phát hiện use case trùng ngữ nghĩa giữa các khối (ví dụ "tóm tắt tài liệu" xuất hiện ở 8 nơi). Quy tắc: **giữ riêng nếu input, người dùng, hoặc ràng buộc pháp lý khác nhau; gộp nếu chỉ khác tên gọi.**
2. Phát hiện use case "biến thể rỗng" — cùng một việc chỉ đổi tên đối tượng. Gộp lại thành một use case có trường `pham_vi_ap_dung`.
3. Kiểm tra phân bố: không khối nào chiếm > 20% tổng use case.
4. Ghi báo cáo dedup: đã gộp bao nhiêu, còn lại bao nhiêu.

**Nghiệm thu:** tỷ lệ trùng ngữ nghĩa < 5% khi A12 lấy mẫu 40 dòng kiểm tra.

---

### PHASE 6 — CHẤM ĐIỂM & ƯU TIÊN (Tuần 9)

#### T6.1 | A11 | T5.2 | Chấm điểm 4 trục

**Thang điểm 1–5 cho mỗi trục, ghi rõ tiêu chí:**

| Trục                                                    | 1 điểm                                                           | 5 điểm                                                             |
| -------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------- |
| **Giá trị**                                      | Tiết kiệm < 1 giờ/tháng, không ảnh hưởng doanh thu/rủi ro | Tiết kiệm > 40 giờ/tháng hoặc chặn được rủi ro trọng yếu |
| **Khả thi kỹ thuật**                            | Cần năng lực chưa có sẵn trên thị trường                 | Dùng công nghệ phổ biến, đã có case tương tự              |
| **Sẵn sàng dữ liệu**                           | Dữ liệu không tồn tại hoặc nằm trên giấy                  | Dữ liệu có sẵn dạng số, có API, chất lượng tốt            |
| **Rủi ro pháp lý** (điểm cao = rủi ro thấp) | Chạm quy định bắt buộc người thực hiện                    | Không ràng buộc, thuần nội bộ                                  |

**Công thức:** `tong_diem = Giá trị × 0,35 + Khả thi × 0,25 + Dữ liệu × 0,25 + Rủi ro × 0,15`

**Xếp rổ (kế hoạch gốc — KHÔNG khớp dữ liệu thực tế, xem ghi chú dưới):**

- **Quick win**: tổng ≥ 3,8 và khả thi ≥ 4 và dữ liệu ≥ 4
- **Chiến lược**: giá trị ≥ 4 nhưng khả thi hoặc dữ liệu ≤ 3
- **Nghiên cứu**: còn lại

> **Ghi chú audit 17/08/2026:** Đối chiếu 43/43 dòng `usecase_registry.csv` cho thấy quy tắc
> xếp rổ **thực tế đã áp dụng** đơn giản hơn quy tắc trên — chỉ dựa vào `tong_diem`, không xét
> riêng từng trục khả thi/dữ liệu/giá trị:
> `Quick win: tong_diem ≥ 3,8` · `Chiến lược: 3,0 ≤ tong_diem < 3,8` · `Nghiên cứu: tong_diem < 3,0`.
> Khớp chính xác 43/43 dòng (0 sai lệch), trong khi quy tắc theo từng trục ở trên cho ra
> 17/43 sai lệch nếu áp lại — tức bảng trên đã KHÔNG phải là quy tắc dùng để tạo dữ liệu hiện
> hành. Không có ghi chép nào giải thích khi nào/tại sao quy tắc bị đơn giản hoá. Công thức
> tính điểm `tong_diem` (GLOBAL_RULES.md OS-5, trọng số 0,35/0,25/0,25/0,15) thì khớp đúng
> 43/43 dòng — không có sai lệch ở bước tính điểm, chỉ sai lệch ở bước xếp rổ sau đó.
> Xem `00_control/AUDIT_LOG.md` mục 17/08/2026.

**Output:** cập nhật `usecase_registry.csv` + `/11_scoring/PRIORITY.md`

**Nghiệm thu:** 100% dòng có đủ 4 điểm; có biểu đồ phân bố theo rổ và theo khối.

---

#### T6.2 | A11 | T6.1 | Top 30 & lộ trình

**Các bước:**

1. Chọn Top 30 theo tổng điểm, đảm bảo phủ ≥ 8 khối chức năng (tránh dồn hết vào một khối).
2. Với mỗi use case Top 30, viết một trang: bối cảnh · quy trình hiện tại · thiết kế giải pháp · dữ liệu cần · KPI · rủi ro · ước tính công sức.
3. Xếp thành lộ trình 3 đợt: 0–3 tháng (quick win) · 3–9 tháng · 9–18 tháng.
4. Ước tính ROI cho Top 10, ghi rõ toàn bộ giả định vào `ASSUMPTIONS.md`.

**Nghiệm thu:** 30 trang chi tiết; lộ trình 3 đợt; ROI Top 10 có công thức truy vết được.

---

### PHASE 7 — AUDIT & BÁO CÁO (Tuần 10)

#### T7.1 | A12 | Chạy song song từ Phase 2 | Red Team audit

**A12 chạy audit sau mỗi milestone, ghi vào `AUDIT_LOG.md`.**

**Checklist audit:**

1. **Bịa nguồn** — lấy mẫu ngẫu nhiên 25 `source_id`, kiểm tra URL còn sống và nội dung đúng như trích dẫn
2. **Bịa số** — mọi `[DATA]` có kỳ và đơn vị chưa
3. **Nhãn sai** — có dòng nào gắn `[FACT]` mà thực chất là suy luận
4. **Bịa chức danh** — mọi chức danh cụ thể tại Dragon Capital có nguồn chưa
5. **Use case rỗng** — lấy mẫu 40 dòng, kiểm tra có trả lời được 6 câu không
6. **Trùng lặp** — lấy mẫu 40 dòng, đếm trùng ngữ nghĩa
7. **Lệch phân bố** — có khối nào bị bỏ quên không
8. **Trích quá 15 từ** — quét toàn bộ artifact tìm đoạn copy nguyên văn
9. **Logic gãy** — kết luận có được đỡ bởi dữ kiện phía trên không
10. **Tỷ lệ INFERENCE** — có vượt 35% không

**Format finding:**

```
[AUD-###] | Mức: HIGH/MED/LOW | Artifact | Dòng/mục | Vấn đề | Đề xuất sửa | Agent chịu trách nhiệm | Trạng thái
```

**Nghiệm thu:** đủ 10 hạng mục; mọi finding HIGH đã đóng.

---

#### T7.2 | A13 | T6.2, T7.1 | Báo cáo tổng hợp

**Cấu trúc 12 phần:**

1. Executive Summary (2 trang — đọc xong biết 80% kết luận)
2. Ngành quản lý quỹ toàn cầu: dòng vốn, quy mô, xu hướng
3. Ngành quản lý quỹ Việt Nam: landscape, pháp lý, khoảng cách so với quốc tế
4. Phân khúc ngành — ma trận 6 trục
5. Business model & unit economics
6. Value chain 3 tầng
7. Giải phẫu Dragon Capital: pháp nhân, sản phẩm, tổ chức, nhịp vận hành
8. Bản đồ role & tác vụ
9. Danh mục AI use case — phương pháp và tổng quan phân bố
10. Top 30 use case ưu tiên + lộ trình 3 đợt
11. Khoảng trống dữ liệu, giả định, giới hạn nghiên cứu
12. Phụ lục: glossary, source registry, task registry, use case registry đầy đủ

**Quy tắc viết:** mỗi phần mở bằng 3–5 bullet kết luận, rồi mới đến bằng chứng. Không viết dài dòng. Mọi bảng đều phải có nguồn.

**Nghiệm thu:** phần 11 liệt kê trung thực các giới hạn; Executive Summary đứng độc lập được.

---

## 8. GATE CHECK — 5 CHỐT CHẶN

| Gate         | Sau task | ORCHESTRATOR kiểm                                                                                      | Fail thì làm gì                                                              |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **G1** | T1.1     | Glossary đã qua bài test NAV T+1; mọi mục có`source_id`                                         | Đào lại lexicon, không cho chạy Phase 2                                    |
| **G2** | T2.x     | 4 luồng đều đạt nghiệm thu chất lượng; báo cáo số nguồn thật theo Tier                    | Giao lại luồng yếu nhất                                                     |
| **G3** | T4.2     | Chi tiết ở T4.3                                                                                       | Quay lại T3.3 đào khối mỏng                                                |
| **G4** | T5.2     | Báo cáo tổng use case / VERIFIED / CATALOGUE; tỷ lệ trùng ngữ nghĩa < 5%; không use case rỗng | Nếu số lượng thấp:**đào thêm task** — cấm nhân bản biến thể |
| **G5** | T7.1     | Hết finding HIGH                                                                                       | Sửa rồi audit lại                                                            |

> **Luật chống loãng ở G4:** nếu chưa đủ 300 use case, cách sửa **duy nhất được phép** là quay lại làm dày `task_registry.csv`. Nghiêm cấm tạo thêm use case bằng cách chẻ nhỏ hoặc đổi tên use case đã có. Thà báo cáo 260 use case thật còn hơn 400 use case có 140 dòng rỗng.

---

## 9. LỊCH CHẠY

| Tuần | Task                                  | Agent hoạt động         |
| ----- | ------------------------------------- | -------------------------- |
| 0     | T0.1                                  | A0                         |
| 1     | T1.1                                  | A1                         |
| 2–4  | T2.1, T2.2, T2.3, T2.4*(song song)* | A2, A3, A7, A8 + A12 audit |
| 4–5  | T3.1, T3.2, T3.3                      | A4, A5, A6                 |
| 6–7  | T4.1, T4.2, T4.3                      | A9, A0                     |
| 7–8  | T4.4 phỏng vấn                      | Thư + A9                  |
| 8–9  | T5.1, T5.2                            | A10                        |
| 9     | T6.1, T6.2                            | A11                        |
| 10    | T7.1, T7.2                            | A12, A13                   |

**Bản nén 5 tuần:** gộp Phase 1 vào tuần 1 cùng Phase 2; bỏ T4.4 (chấp nhận trần độ sâu 60%); rút Phase 3 còn 3 ngày.

---

## 10. PROMPT KHỞI ĐỘNG CHO ORCHESTRATOR

```
Bạn là ORCHESTRATOR (A0) của dự án nghiên cứu ngành quản lý quỹ và Dragon Capital.

BỐI CẢNH
Mục tiêu: tạo danh mục 300-400 AI use case cho ngành quản lý quỹ VN,
neo vào Dragon Capital (DCVFM), với 80-120 use case ở mức VERIFIED.
Toàn bộ kế hoạch nằm ở /00_control/IMPLEMENTATION_PLAN.md.

NHIỆM VỤ NGAY
1. Đọc IMPLEMENTATION_PLAN.md.
2. Thực hiện T0.1: dựng cây thư mục Mục 2, tách GLOBAL_RULES.md /
   SCHEMAS.md / AGENT_ROSTER.md, tạo 5 file dữ liệu với header đúng Mục 4,
   tạo TASK_BOARD.md liệt kê mọi task với trạng thái TODO.
3. Giao T1.1 cho A1 LEXICON.
4. Khi T1.1 qua Gate G1, khởi động song song A2, A3, A7, A8.

LUẬT CỦA BẠN
- Không tự làm nghiên cứu. Bạn điều phối, kiểm gate, giải xung đột.
- Sau mỗi task hoàn thành: cập nhật TASK_BOARD.md và CHANGELOG.md.
- Trước khi cho qua gate: chạy đúng checklist, không nới tiêu chí.
  Fail thì giao lại, không đi tiếp.
- Mọi agent phải đọc GLOBAL_RULES.md trước khi ghi artifact.
- Nếu một agent báo BLOCKER, ghi vào OPEN_QUESTIONS.md và báo cho
  chủ dự án, không tự suy đoán để đi tiếp.

BẮT ĐẦU BẰNG T0.1.
```

### 10.1 Prompt mẫu cho agent nghiên cứu (dùng chung, thay phần in hoa)

```
Bạn là {AGENT_ID} - {TÊN AGENT} trong dự án nghiên cứu ngành quản lý quỹ.

TRƯỚC KHI LÀM GÌ: đọc /00_control/GLOBAL_RULES.md và /00_control/SCHEMAS.md.

TASK CỦA BẠN: {TASK_ID}
Input: {ĐƯỜNG DẪN ARTIFACT THƯỢNG NGUỒN}
Các bước: {COPY TỪ TASK CARD}
Output: {ĐƯỜNG DẪN}
Tiêu chí nghiệm thu: {COPY TỪ TASK CARD}

BẮT BUỘC
- Mọi dòng dữ kiện gắn nhãn bằng chứng ([FACT]/[DATA]/[REG]/[INFERENCE]/...).
- Mọi nguồn đăng ký vào SOURCE_REGISTRY.csv trước khi trích, lấy source_id.
- Không chế URL, không chế số, không chế chức danh.
- Trích dẫn tối đa 15 từ, còn lại diễn đạt lại bằng lời của bạn.
- Không biết thì ghi "Không xác minh được", không suy đoán.
- Bế tắc thì ghi vào OPEN_QUESTIONS.md, không tự gỡ bằng giả định.

KẾT THÚC
Ghi block ## HANDOFF cuối artifact: đã tạo gì | giả định đang dùng |
còn thiếu gì | agent kế tiếp cần lưu ý gì.
Rồi đánh dấu task READY_FOR_AUDIT trong TASK_BOARD.md.
```

### 10.2 Prompt cho A12 RED_TEAM

```
Bạn là A12 RED_TEAM. Vai trò của bạn là tìm lỗi, không phải khen.

Audit artifact: {ĐƯỜNG DẪN}
Chạy đủ 10 hạng mục checklist ở T7.1.

NGUYÊN TẮC
- Giả định artifact có lỗi cho đến khi chứng minh ngược lại.
- Kiểm tra thật: mở URL, đối chiếu số, không tin nhãn agent tự gắn.
- Với mỗi finding, ghi rõ dòng nào, sai gì, sửa thế nào.
- Không được kết luận "đạt yêu cầu" nếu chưa lấy mẫu tối thiểu quy định.
- Nếu phát hiện > 3 finding HIGH trong một artifact, đề xuất
  ORCHESTRATOR trả lại toàn bộ artifact thay vì vá từng dòng.

Ghi kết quả vào AUDIT_LOG.md theo format [AUD-###].
```

---

## 11. RỦI RO & CÁCH XỬ LÝ

| Rủi ro                                       | Dấu hiệu sớm                                    | Xử lý                                                                                         |
| --------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Agent bịa quy trình nội bộ Dragon Capital | Dòng`[FACT]` về DC không có `source_id` T1 | A12 quét trường`do_tin_cay` mỗi tuần; hạ nhãn hàng loạt                              |
| Chạy đua số lượng, use case rỗng        | `REJECTED.csv` quá ít so với registry         | Ép tỷ lệ loại ≥ 20% ở G4                                                                  |
| Task registry lệch về front office          | FO > 40% tổng số dòng                           | Back office thực chất nhiều tác vụ lặp nhất — giao A7 đào lại BO                     |
| Không tiếp cận được bản cáo bạch     | A8 báo BLOCKER                                    | Dùng bản cáo bạch của quỹ tương đương ở công ty khác + đánh dấu`[INFERENCE]` |
| Quy định pháp luật đã thay đổi        | Văn bản trích dẫn hết hiệu lực              | Bắt buộc ghi`ngay_kiem_tra_hieu_luc` ở mọi file trong `legal/`                          |
| Không phỏng vấn được                    | Tuần 7 chưa có cuộc nào                       | Hạ mục tiêu xuống 4 cuộc; ghi rõ giới hạn ở phần 11 báo cáo                         |
| Trùng lặp giữa các agent song song        | Hai artifact mô tả cùng nội dung               | A0 rà chéo ở G2                                                                              |

---

## 12. GHI CHÚ CUỐI

**Ba thứ quyết định chất lượng dự án này, theo thứ tự:**

1. Độ sâu của `task_registry.csv` — mọi thứ downstream đều bắt nguồn từ đây
2. Chất lượng cột `diem_gay_pain_point` — không có pain point thật thì use case chỉ là mô tả công nghệ
3. Kỷ luật ở Gate G4 — chỗ dễ tự lừa mình nhất

**Con số 300–400 là kết quả mong đợi, không phải chỉ tiêu bắt buộc.** Nếu chạy nghiêm túc mà ra 260 use case thật, đó là kết quả tốt hơn 400 use case có 140 dòng rỗng — vì người trong ngành nhận ra dòng rỗng trong 5 phút, và uy tín của cả báo cáo mất theo.
