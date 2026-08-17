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
| T5.1 | A10 | T4.3 | **DONE** | Sinh use case theo ma trận task × năng lực AI — 43 UC trong `usecase_registry.csv`. *(Trạng thái đồng bộ lại 17/08/2026 — artifact đã tồn tại từ trước nhưng board chưa cập nhật.)* |
| T5.2 | A10 | T5.1 | **DONE** | Dedup & chống loãng — 43 UC không trùng lặp id/tên. |
| T5.3 | A11 | T5.2 | **DONE, PHẠM VI THU HẸP** | Lọc UC từ pool — **chỉ 43/100 UC theo mục tiêu gốc**, KHÔNG đạt target OQ-002. Chưa có ghi chép chính thức về quyết định thu hẹp — xem `00_control/OPEN_QUESTIONS.md` OQ-002 (vẫn HIGH/OPEN) và `00_control/ASSUMPTIONS.md` AS-004. |
| T5.4 | A10 | T5.3 | **DONE, MỘT PHẦN** | Fact-check nguồn cho 43 UC đã lọc — mỗi UC có `source_ids`, nhưng 0/43 đạt mức VERIFIED (tất cả CATALOGUE) vì thiếu thời lượng thao tác + hệ thống dùng, xem `META.limits` trong `FINAL_REPORT.html`. |
| T6.1 | A11 | T5.4 | **DONE** | Chấm điểm 4 trục (giá trị/khả thi/dữ liệu/rủi ro) — có trong `usecase_registry.csv` cột `diem_*`/`tong_diem`, chấm thủ công không dùng quy tắc tự động. |
| T6.2 | A11 | T6.1 | **DONE** | Top use case & lộ trình 3 đợt — `_data/roadmap.json`, hiển thị Phần 06 báo cáo. |
| T7.1 | A12 | T2.x | **DONE (17/08/2026)** | Red Team 10-hạng-mục đã chạy trên dữ liệu cuối (43 UC/87 task). 2 finding thực chất — trích quá 15 từ (đã sửa 11 dòng) và quy tắc xếp rổ `ro` không khớp tài liệu kế hoạch gốc (đã cập nhật tài liệu cho khớp thực tế). Không phát hiện bịa nguồn/bịa số/bịa chức danh. Chi tiết: `00_control/AUDIT_LOG.md` mục "AUDIT PHASE 3". |
| T7.2 | A13 | T6.2, T7.1 | **DONE, VỚI GHI CHÚ** | Báo cáo tổng hợp — `12_report/FINAL_REPORT.html` / `index.html` (bản v2.1, 17/08/2026). Đã audit + sửa lỗi kỹ thuật (xem CHANGELOG 17/08/2026) nhưng T7.1 chưa đóng và OQ-002 chưa RESOLVED — báo cáo tự nhận là giai đoạn "Catalogue", chưa phải bản triển khai chi tiết (xem banner đầu trang). |
| T8.0 | Claude | T7.2 | **DONE (17/08/2026)** | Lập kế hoạch chi tiết cho 4 khối chưa nghiên cứu (Corporate Actions, Client Reporting, Compliance & Regulatory Reporting, Data Management) — xem `00_control/PHASE2_PLAN.md`. Chưa chạy, chờ Thư xác nhận OQ-003. |
| T8.1 | — | T8.0, OQ-003 | TODO (chờ xác nhận) | Giai đoạn A — Gom & verify nguồn cho 4 khối (ưu tiên Compliance & Regulatory Reporting trước theo đề xuất trong PHASE2_PLAN.md Mục 5) |
| T8.2 | — | T8.1 | TODO | Giai đoạn B — Bóc tách tác vụ, nối vào `task_registry.csv`, kiểm tra ranh giới với 87 task hiện có (PHASE2_PLAN.md Mục 2) |
| T8.3 | — | T8.2 | TODO | GATE 2 — kiểm tra độ sâu từng khối mới trước khi sinh use case |
| T8.4 | — | T8.3 | TODO | Giai đoạn C — Sinh & chấm điểm use case, nối vào `usecase_registry.csv` |
| T8.5 | — | T8.4 | TODO | Giai đoạn D — Red Team 10 hạng mục trên phần mới + tích hợp báo cáo v3.0 |
| T8.6 | — | T8.5 | TODO (không bắt buộc) | Giai đoạn E — Phỏng vấn xác nhận, nâng use case khối mới lên VERIFIED |
