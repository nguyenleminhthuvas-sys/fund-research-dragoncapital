# TASK BOARD

| ID | Agent | Phụ thuộc | Trạng thái | Ghi chú |
|---|---|---|---|---|
| T0.1 | A0 | — | DONE | Khởi tạo workspace, tách file, tạo CSV rỗng, board này |
| T1.1 | A1 | T0.1 | **DONE** | GLOSSARY.md (210 thuật ngữ, 8 nhóm) + CORE_30.md (30 cốt lõi, 15 cơ chế, bài test NAV T+1). SOURCE_REGISTRY 12 nguồn. |
| T2.1 | A2 | T1.1 | **DONE** | GLOBAL_MAP.md: Fix audit findings [AUD-002, AUD-003] done, READY_FOR_AUDIT |
| T2.2 | A3 | T1.1 | **DONE** | VN_MAP.md + 6 legal/*.md + REG_TASK_CANDIDATES.csv (63 dòng ≥ 60). Khủng hoạt lực được kiểm tra 14/08/2026. READY_FOR_AUDIT |
| T2.3 | A7 | T1.1 | **DONE** | VENDOR_TAXONOMY.md + TASK_CANDIDATES.csv (310 dòng, MECE, tỷ lệ chuẩn). SOURCE_REGISTRY 91 nguồn. READY_FOR_AUDIT |
| T2.4 | A8 | T1.1 | **DONE** | DC_ANATOMY.md + entity_map.json (3 lớp) + 6 funds/*.md + PROCESS_FROM_PROSPECTUS.csv (41 dòng ≥40). READY_FOR_AUDIT |
| T3.1 | A4 | T2.1, T2.2 | **DONE** | SEGMENTATION_MATRIX.md: 6 trục, 10 công ty, 8 điểm khác biệt VC. READY_FOR_AUDIT |
| T3.2 | A5 | T2.1, T2.2, T2.4 | **DONE** | UNIT_ECONOMICS.md: 3 kịch bản hòa vốn, 10 cost + 5 revenue buster. READY_FOR_AUDIT |
| T3.3 | A6 | T2.1-T2.4, T3.1 | **DONE** | VALUE_CHAIN.md + 60 processes/*.md + 300 L3 tasks. READY_FOR_AUDIT |
| T4.1 | A9 | T3.3, T2.3, T2.4 | **DONE** | Dựng 18 thẻ role thành công, đủ 12 trường tại /09_roles_tasks/role_cards |
| T4.2 | A9 | T4.1 | **DONE** | Hợp nhất & chuẩn hóa task_registry.csv, dedup thành 355 dòng chuẩn |
| T4.3 | A0 | T4.2 | **DONE** | GATE 1 — Đã pass 100% các chỉ tiêu kiểm định |
| T4.4 | Thư | T4.2 | IN PROGRESS | Phỏng vấn sơ cấp |
| T4.4.1 | Agent | T4.4 | **DONE** | Khối 1: Thu thập pain point & bộ câu hỏi NAV |
| T4.4.2 | Agent | T4.4 | **DONE** | Khối 2: Thu thập pain point & bộ câu hỏi Settlement |
| T5.1 | A10 | T4.3 | TODO | Sinh use case theo ma trận task × năng lực AI |
| T5.2 | A10 | T5.1 | TODO | Dedup & chống loãng |
| T5.3 | A11 | T5.2 | TODO (chờ OQ-002) | Lọc 100 UC xuất sắc từ pool — cần Thư xác nhận bổ sung task này |
| T5.4 | A10 | T5.3 | TODO (chờ OQ-002) | QuoteExtractor: fact-check 2 nguồn cho đúng 100 UC đã lọc |
| T6.1 | A11 | T5.4 | TODO | Chấm điểm 4 trục |
| T6.2 | A11 | T6.1 | TODO | Top 30 & lộ trình |
| T7.1 | A12 | T2.x | TODO | Red Team audit (chạy song song) |
| T7.2 | A13 | T6.2, T7.1 | TODO | Báo cáo tổng hợp |
