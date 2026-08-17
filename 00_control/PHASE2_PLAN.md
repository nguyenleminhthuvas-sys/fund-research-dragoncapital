# PHASE 2 PLAN — 4 KHỐI CHỨC NĂNG CÒN LẠI

**Ngày lập:** 17/08/2026 · **Áp dụng cho:** Corporate Actions · Client Reporting · Compliance & Regulatory Reporting · Data Management
**Kế thừa luật chơi từ:** `IMPLEMENTATION_PLAN.md` Mục 3 (GLOBAL_RULES) và Mục 4 (SCHEMAS) — không đổi, chỉ scope lại phạm vi cho 4 khối mới.

---

## 0. Vì sao cần plan riêng, không chạy y hệt Phase 2–7 cũ

Phase 1–3 gốc (glossary, bản đồ ngành, segmentation, business model) là nền tảng **dùng chung cho toàn ngành**, không cần làm lại. Việc còn thiếu chỉ nằm ở tầng sâu nhất: **task_registry.csv** và **usecase_registry.csv** chưa có dữ liệu cho 4 khối này. Plan này vì vậy chỉ còn tương đương Phase 2.3/2.4 + Phase 4–7 gốc, thu hẹp vào 4 khối, và bỏ các bước đã có kết quả dùng lại được (glossary, segmentation...).

---

## 1. Cảnh báo bắt buộc đọc trước khi bắt đầu

### 1.1 Nguồn "trông như xong" nhưng chưa dùng được
`03_industry_vn/legal/TT_96_2020.md`, `LCS_54_2019.md`, `ND_155_2020.md`, `AML_QLQ.md` đều mang banner **"Nội dung chưa được kiểm chứng nguồn... không trích vào báo cáo"** — mọi điều khoản bên trong gắn `[UNVERIFIED]`. Đây là tóm tắt nội bộ, **không phải nguồn sơ cấp**. Trước khi trích bất kỳ điều khoản nào (kể cả đúng nội dung), phải tải lại nguyên văn từ nguồn chính thức (thuvienphapluat.vn hoặc tương đương) và đăng ký `source_id` mới — đúng quy trình đã áp dụng thành công cho TT98/2020 (`S-TT98-001`, 930.729 ký tự đã verify) và QĐ428 (`_raw/legal/quyet-dinh-428-qd-ubck.txt` có số dòng cụ thể).

Các điều khoản đáng chú ý cần verify lại (chỉ là gợi ý vị trí tìm, không phải trích dẫn dùng được):
- Luật CK 54/2019 — Điều 97 (báo cáo UBCKNN), Điều 75 (tách biệt tài sản)
- TT96/2020 — Điều 9, 16-20 (công bố thông tin định kỳ/bất thường), Điều 23, 25 (công bố NAV/iNAV/PCF)
- ND155/2020 — Điều 226 (kiểm soát nội bộ), Điều 230 (lịch báo cáo định kỳ), Điều 240 (vốn khả dụng)

### 1.2 Khung chủ đề tham khảo — KHÔNG dùng nội dung
`_quarantine/VALUE_CHAIN.md` từng vạch ra các mục trùng khớp 4 khối này (FO.2.4 Theo dõi Cổ tức/Quyền, BO.2.5 Phân bổ Cổ tức/Quỹ, BO.3.x Dịch vụ NĐT & Báo cáo, MO.2.x Kiểm soát Tuân thủ, EN.1.x Công nghệ & Dữ liệu). Toàn bộ nội dung đã bị cách ly vì là văn bản mẫu sinh máy, trích nguồn giả. Chỉ dùng tên chủ đề làm checklist tìm nguồn thật từ đầu, **cấm đọc/trích nội dung bên trong**.

---

## 2. Kế hoạch theo từng khối

### 2.1 Corporate Actions

**Phạm vi:** Xử lý sự kiện quyền của **chứng khoán trong danh mục quỹ đang nắm giữ** (cổ tức tiền mặt/cổ phiếu, quyền mua, tách/gộp, chuyển đổi trái phiếu, hủy niêm yết, quyền biểu quyết ĐHCĐ của tổ chức phát hành).

**Ranh giới với khối đã có:** KHÁC với T-BO-011 "Phân phối lợi nhuận" (đó là quỹ chia lãi CHO nhà đầu tư của quỹ). Corporate Actions là quỹ NHẬN quyền lợi TỪ cổ phiếu/trái phiếu mà quỹ đang sở hữu, rồi phản ánh đúng vào NAV.

**Nguồn cần tìm mới:**
- Quy chế HOSE/HNX về ngày GDKHQ, ngày đăng ký cuối cùng (chưa có trong `_raw/`)
- Quy chế VSDC về đăng ký/thực hiện quyền — kiểm tra lại `_raw/legal/vsd-luu-ky-chung-khoan.html` và `vsd-bu-tru-thanh-toan.html` đã có, xem có điều khoản nào về corporate action chưa khai thác
- Luật CK 54/2019 phần quyền cổ đông (cần verify nguyên văn — mục 1.1)
- Bản cáo bạch BVFED (đã có) — đọc lại phần xử lý cổ tức nhận được trong danh mục, nếu có

**Rủi ro:** đây là khối ít tài liệu tiếng Việt công khai nhất trong 4 khối — nhiều khả năng phải dựa nhiều vào JD quốc tế (`[INFERENCE]`) hơn 3 khối kia.

---

### 2.2 Client Reporting

**Phạm vi:** Sao kê định kỳ cho từng khách hàng ủy thác, báo cáo hiệu quả theo yêu cầu, xử lý khiếu nại, tổ chức ĐHNĐT (quỹ đóng/ETF), cập nhật thông tin trên kênh trực tiếp với khách hàng (portal, email).

**Ranh giới với khối đã có:** KHÁC với T-BO-020 (báo cáo pháp lý cho UBCKNN) và T-BO-022 (cập nhật báo cáo NĐT định kỳ — đã dùng case Amber Capital làm pain point). Client Reporting là **kênh trực tiếp/tương tác 2 chiều với khách hàng**, không phải nghĩa vụ công bố hàng loạt.

**Nguồn cần tìm mới:**
- JD "IR & Client Servicing" / "Investor Relations Officer" (chưa có JD nào loại này trong `_raw/jd/`)
- Quy định giải quyết khiếu nại nhà đầu tư trong Luật CK/ND155 (cần verify)
- Case xử phạt liên quan chậm/thiếu báo cáo khách hàng khác Amber Capital (tránh dùng lại case đã dùng cho T-BO-022)

**Rủi ro:** dễ trùng ngữ nghĩa với khối NAV nếu không tách rõ ranh giới ngay từ khi viết task — ưu tiên kiểm tra chéo với `task_registry.csv` hiện có trước khi thêm dòng mới.

---

### 2.3 Compliance & Regulatory Reporting

**Phạm vi:** (a) Giám sát tuân thủ hạn mức đầu tư **trước khi đặt lệnh** (pre-trade compliance check), (b) báo cáo sở hữu cổ đông lớn/người có liên quan, (c) quản lý xung đột lợi ích, (d) lịch nộp báo cáo định kỳ đầy đủ lên UBCKNN (mở rộng ngoài báo cáo kế toán).

**Ranh giới với khối đã có:** KHÁC với UC-028 (Risk block — cảnh báo **sau khi** vi phạm hạn mức đã xảy ra). Compliance block tập trung **ngăn trước khi lệnh khớp**, góc nhìn kiểm soát tiền kiểm chứ không phải hậu kiểm. KHÁC với T-BO-049/050/051 (đã có AML/KYC ở khối Transfer Agency) — không đào lại AML, chỉ làm phần sở hữu lớn/xung đột lợi ích/lịch báo cáo còn thiếu.

**Nguồn cần tìm mới:**
- Luật CK 54/2019, TT96/2020, ND155/2020 (verify nguyên văn — mục 1.1, đây là khối có sẵn nhiều gợi ý điều khoản nhất)
- Case xử phạt về báo cáo sở hữu cổ đông lớn / xung đột lợi ích (chưa có case nào loại này trong `_raw/enforcement/`)
- Tài liệu vendor compliance module (Confluence, Bloomberg AIM — đã gợi ý trong plan gốc T2.3, chưa khai thác)

**Đây là khối có nền pháp lý sẵn rõ nhất trong 4 khối** — ưu tiên làm trước vì tỷ lệ REG/FACT dự kiến cao, ít phải suy luận.

---

### 2.4 Data Management

**Phạm vi:** Quản trị dữ liệu tham chiếu (danh mục CK, tổ chức phát hành), làm sạch dữ liệu giá lịch sử, quản lý quyền truy cập hệ thống, sao lưu/bảo mật, quản trị master data.

**Cảnh báo riêng — rủi ro trùng lặp cao nhất trong 4 khối:** "dữ liệu" chảy qua mọi tác vụ khác (NAV đã dùng dữ liệu giá, AML đã dùng dữ liệu KYC...). Chỉ được tính là task riêng của khối này khi **bản thân việc quản lý dữ liệu là công việc chính** (vd: đối chiếu danh mục CK tham chiếu, cấp/thu quyền truy cập hệ thống, sao lưu định kỳ) — không lặp lại task đã có ở khối khác chỉ vì chúng "có dùng dữ liệu".

**Nguồn cần tìm mới:**
- JD "Data/IT Manager" quốc tế (chưa có trong `_raw/jd/`)
- Trang vendor đã có (Broadridge, Clearwater, SS&C, Enfusion) — đọc lại phần data governance, hiện mới khai thác phần fund accounting
- Quy định an toàn thông tin/an ninh mạng áp dụng cho tổ chức tài chính (nếu có, mức độ liên quan tới vận hành quỹ có thể thấp)

**Khuyến nghị:** đây là khối ít gắn liền với vận hành quỹ nhất (mang tính IT chung), khả năng cao sinh ra ít use case đặc thù ngành hơn 3 khối kia. Đề xuất làm **sau cùng** hoặc **thu hẹp phạm vi mạnh** nếu thời gian hạn chế, ưu tiên 3 khối còn lại trước.

---

## 3. Lịch trình theo giai đoạn (làm song song 4 khối được, trừ khi ghi chú riêng)

| Giai đoạn | Nội dung | Đầu ra | Điều kiện qua gate |
|---|---|---|---|
| **A — Gom & verify nguồn** | Tải + verify nguyên văn 3 văn bản luật (mục 1.1); tìm JD mới (IR/Client Servicing, Data/IT Manager); tìm case xử phạt mới nếu có; đăng ký toàn bộ vào `SOURCE_REGISTRY.csv` | Nguồn mới trong `_raw/` + dòng mới trong `SOURCE_REGISTRY.csv` | Mỗi khối ≥ 3 nguồn T1/T2 xác minh được |
| **B — Bóc tách tác vụ** | Với mỗi nguồn, bóc task theo mẫu "động từ + tân ngữ + điều kiện"; kiểm tra ranh giới với 87 task hiện có (mục 2) trước khi thêm dòng mới | Dòng mới nối vào `task_registry.csv` | 100% dòng mới có `source_id`; báo cáo tỷ lệ REG/FACT/INFERENCE |
| **GATE** | Kiểm tra độ sâu — nếu khối nào < 5 task thật → dừng, ghi rõ lý do (nguồn mỏng hay ngành thực sự mỏng ở đó), không tự sinh use case | — | Giống T4.3 gốc |
| **C — Sinh & chấm điểm use case** | Áp ma trận 7 năng lực AI cho từng task mới; áp bộ lọc 6 câu hỏi (Mục 3.5 GLOBAL_RULES); chấm điểm 4 trục đúng công thức đã audit (0,35/0,25/0,25/0,15) | Dòng mới nối vào `usecase_registry.csv` | Dòng nào < 3/6 câu hỏi → vào `REJECTED.csv`, không đưa vào registry |
| **D — Red Team + tích hợp** | Chạy lại đúng 10 hạng mục Red Team (như đã làm cho 43 UC hiện tại) trên riêng phần mới trước khi gộp; viết deep-dive cho use case điểm cao nhất mỗi khối mới; build lại `build_report.py` (blocks_todo sẽ tự rút từ 4 xuống 0) | `AUDIT_LOG.md` mục mới; báo cáo v3.0 | 0 finding HIGH chưa đóng |
| **E — Phỏng vấn xác nhận (khuyến nghị, không bắt buộc)** | Giống T4.4 gốc — bổ sung câu hỏi cho khối mới vào `INTERVIEW_SHORTLIST.md`, đặc biệt Compliance (khối có nền REG cao, dễ verify FACT qua phỏng vấn ngắn) | Nâng một phần use case từ CATALOGUE lên VERIFIED | Không bắt buộc để ra bản CATALOGUE, nhưng bắt buộc nếu muốn công bố mức VERIFIED |

---

## 4. Cập nhật cần làm ở các control-doc khác (khi bắt đầu chạy thật, chưa làm ở bước lập plan này)

- `TASK_BOARD.md`: thêm dòng T8.1–T8.5 (Gom nguồn → Bóc task → Gate → Sinh UC → Audit) tương ứng bảng Mục 3
- `OPEN_QUESTIONS.md`: mở OQ-003 hỏi Thư có đồng ý ưu tiên thứ tự Compliance → Corporate Actions/Client Reporting → Data Management (theo mục 2.4) hay muốn thứ tự khác
- `ASSUMPTIONS.md`: thêm AS-005 ghi rõ ranh giới đã định nghĩa ở Mục 2 trên, để không ai vô tình đào trùng khi thực hiện

## 5. Trước khi bắt đầu chạy thật — cần Thư xác nhận

1. **Thứ tự ưu tiên** 4 khối — đề xuất Compliance & Regulatory Reporting trước (nền pháp lý rõ nhất), Data Management sau cùng hoặc thu hẹp phạm vi.
2. **Có làm Giai đoạn E (phỏng vấn) không** — nếu không, 4 khối mới sẽ dừng ở CATALOGUE giống 43 UC hiện tại, không VERIFIED được.
3. **Phạm vi Data Management** — giữ đủ 4 khối như kế hoạch gốc, hay bỏ/thu hẹp khối này vì rủi ro trùng lặp + ít giá trị đặc thù ngành (khuyến nghị của tôi: thu hẹp).
