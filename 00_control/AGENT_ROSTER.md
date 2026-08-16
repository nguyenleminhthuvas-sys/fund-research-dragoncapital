## 5. AGENT_ROSTER.md — 13 AGENT + 1 ORCHESTRATOR

| ID | Tên agent | Vai trò | Sở hữu thư mục | Công cụ cần |
|---|---|---|---|---|
| **A0** | ORCHESTRATOR | Điều phối, cập nhật TASK_BOARD, giải xung đột, gate check | `00_control/` | — |
| **A1** | LEXICON | Xây từ vựng & mô hình tư duy ngành | `01_lexicon/` | Web |
| **A2** | GLOBAL_ANALYST | Bản đồ ngành toàn cầu, dòng vốn, xu hướng | `02_industry_global/` | Web, PDF |
| **A3** | VN_ANALYST | Thị trường VN + khung pháp lý | `03_industry_vn/` | Web, PDF |
| **A4** | SEGMENTER | Ma trận phân khúc 6 trục | `04_segmentation/` | Web |
| **A5** | ECONOMIST | Business model & unit economics | `05_business_model/` | Web, PDF, tính toán |
| **A6** | VALUECHAIN_ARCHITECT | Value chain 3 tầng đến cấp 3 | `06_value_chain/` | Web, PDF |
| **A7** | VENDOR_MINER | Rút task taxonomy từ tài liệu vendor & JD | `07_vendor_taxonomy/` | Web, browser |
| **A8** | COMPANY_ANALYST | Giải phẫu Dragon Capital | `08_company_dragoncapital/` | Web, browser, PDF |
| **A9** | ROLE_TASK_ENGINEER | Thẻ role + tác vụ nguyên tử | `09_roles_tasks/`, `task_registry.csv` | — |
| **A10** | USECASE_GENERATOR | Sinh use case từ ma trận task × năng lực AI | `10_usecases/`, `usecase_registry.csv` | — |
| **A11** | SCORER | Chấm điểm, xếp rổ, chọn Top 30 | `11_scoring/` | Tính toán |
| **A12** | RED_TEAM | Audit độc lập: bịa, trùng, thiếu nguồn, logic sai | ghi vào `AUDIT_LOG.md` | Web |
| **A13** | WRITER | Viết báo cáo cuối | `12_report/` | — |

### 5.1 Nguyên tắc phối hợp
- **A12 không bao giờ chạy cùng lượt với agent nó audit.** Audit chạy sau khi artifact được đánh dấu `READY_FOR_AUDIT`.
- **A9 và A10 là nút cổ chai** — mọi agent thượng nguồn phải xong trước.
- Agent không được sửa artifact của agent khác. Chỉ đề xuất qua `OPEN_QUESTIONS.md`.
- Mỗi agent kết thúc task bằng việc ghi block `## HANDOFF` cuối artifact: đã tạo gì, giả định gì, còn thiếu gì, agent kế tiếp cần lưu ý gì.

---
