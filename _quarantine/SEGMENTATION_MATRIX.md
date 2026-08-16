# MA TRẬN PHÂN KHÚC NGÀNH QUẢN LÝ QUỸ VIỆT NAM (SEGMENTATION MATRIX)

Tài liệu định vị các tổ chức quản lý quỹ tại Việt Nam theo 6 trục phân khúc. Mọi claim được gắn nhãn theo chuẩn `GLOBAL_RULES.md`.

## 1. MA TRẬN 6 TRỤC (6-AXIS SEGMENTATION)

### 1.1 Trục Lớp tài sản (Asset Class)
- **Cổ phiếu (Equities):** Dragon Capital `[FACT]` (Nguồn: S-T1-005), VinaCapital `[FACT]` (Nguồn: S-T1-101), SSIAM `[FACT]` (Nguồn: S-T1-100), VCBF, IPAAM.
- **Trái phiếu (Fixed Income):** Techcom Capital (TCBF) `[FACT]` (Nguồn: S-T1-102), MBCapital, PVI AM.
- **Thị trường tiền tệ (Money Market):** Quỹ mở tiền tệ (chưa phổ biến) -> **[WHITE-SPACE]** `[INFERENCE]` Do lợi suất từ tiền gửi ngân hàng cá nhân tại Việt Nam đang hấp dẫn và dễ tiếp cận hơn sản phẩm quỹ tiền tệ.
- **Tài sản thay thế (Private Equity / Real Estate):** VinaCapital (VOF) `[FACT]` (Nguồn: S-T1-101), Dragon Capital (clean energy/property - trước đây) `[INFERENCE]` (Quỹ chưa niêm yết rộng rãi cho retail).

### 1.2 Trục Cấu trúc pháp lý (Legal Structure)
- **Quỹ mở (Open-ended Funds):** Dragon Capital (DCDS) `[FACT]` (Nguồn: S-T1-004), VCBF, SSIAM, BVF.
- **ETF (Exchange Traded Funds):** Dragon Capital (E1VFVN30) `[FACT]` (Nguồn: S-T1-004), SSIAM (VNFIN LEAD) `[FACT]` (Nguồn: S-T1-100), VinaCapital (VN100).
- **Quỹ đóng (Closed-ended Funds):** Dragon Capital (VEIL) `[FACT]` (Nguồn: S-T1-005), VinaCapital (VOF) `[FACT]` (Nguồn: S-T1-101).
- **Quỹ thành viên / Ủy thác (Mandates):** PVI AM, VietinBank Capital, BVF.
- **Quỹ hưu trí bổ sung tự nguyện:** -> **[WHITE-SPACE]** `[INFERENCE]` Thiếu các chính sách ưu đãi thuế mạnh tay từ chính phủ (Nguồn: S-T3-003), làm hạn chế dòng tiền vào phân khúc này.

### 1.3 Trục Chiến lược đầu tư (Investment Strategy)
- **Chủ động (Active - Alpha seeking):** Dragon Capital (DCDS) `[FACT]` (Nguồn: S-T1-004), VCBF, MBCapital, BVF.
- **Bị động (Passive / Indexing):** SSIAM, Dragon Capital, VinaCapital `[FACT]` (S-T1-100, S-T1-004).
- **Định lượng (Quantitative / Smart Beta):** -> **[WHITE-SPACE]** `[INFERENCE]` Hệ thống hạ tầng dữ liệu và công cụ phái sinh, bán khống chưa hoàn thiện tại Việt Nam làm giới hạn khả năng phát triển Smart Beta (Nguồn: S-T1-008).

### 1.4 Trục Nhóm khách hàng (Client Segment)
- **Cá nhân đại chúng (Mass Retail):** Techcom Capital, Dragon Capital, VinaCapital `[FACT]` (Nguồn: S-T3-100).
- **Khách hàng HNWI / Family Office:** SSIAM, VCBF `[INFERENCE]` (Phân phối qua chi nhánh VIP của ngân hàng/CTCK mẹ).
- **Định chế tài chính (Institutional - Bảo hiểm, SWF):** PVI AM, BVF, VietinBank Capital `[FACT]` (Nguồn: S-T3-100 - Quản lý ủy thác chủ yếu cho công ty bảo hiểm và ngân hàng mẹ).

### 1.5 Trục Kênh phân phối (Distribution Channel)
- **Kênh Ngân hàng (Bancassurance / Wealth):** Techcom Capital (qua TCBS), VCBF (qua VCB), MBCapital (qua MBBank) `[FACT]` (Nguồn: S-T3-100).
- **Kênh Công ty mẹ (Brokerage / CTCK):** SSIAM, IPAAM (qua VNDirect).
- **Nền tảng số (Fintech / B2B2C):** Dragon Capital (DragonX), VinaCapital, phân phối qua Fmarket `[FACT]` (Nguồn: S-T3-100).
- **Robo-Advisor:** -> **[WHITE-SPACE]** `[INFERENCE]` Khung pháp lý về tư vấn đầu tư tự động hóa chưa rõ ràng và thói quen khách hàng chưa hình thành (Nguồn: S-T1-008).

### 1.6 Trục Quy mô & Mô hình vận hành (Scale & Operating Model)
- **Lớn - Hệ sinh thái đa dạng (AUM lớn, nhiều sp):** Dragon Capital, VinaCapital, SSIAM, Techcom Capital `[DATA]` (Top 10 nắm 95% AUM toàn thị trường - Nguồn: S-T3-003).
- **Vừa - Gắn liền công ty mẹ (Boutique / Tích hợp):** VCBF, BVF, PVI AM, MBCapital, VietinBank Capital.
- **Nhỏ - Độc lập:** Các công ty QLQ mới nổi hoặc chuyên ủy thác nhỏ lẻ (IPAAM).

---

## 2. PHÂN TÍCH KHÁC BIỆT CHUỖI GIÁ TRỊ (VALUE CHAIN DIFFERENCES)

Sự phân mảnh trên ma trận tạo ra các yêu cầu vận hành (Value Chain) hoàn toàn khác biệt. Dưới đây là 8 điểm khác biệt then chốt giữa các phân khúc — *nền tảng để rà soát use case AI (T5):*

1. **ETF vs. Quỹ mở (Middle/Back Office):** `[FACT]` Hoạt động Middle/Back Office của ETF đòi hỏi tính toán Danh mục chứng khoán cơ cấu (PCF - Portfolio Composition File) hàng ngày và xử lý cơ chế Creation/Redemption với các AP (Authorized Participants). Quỹ mở thì không, chỉ xử lý lệnh Subscription/Redemption bằng tiền mặt (Nguồn: S-T1-001).
2. **Quỹ mở vs. Quỹ thành viên / Ủy thác (Compliance & Reporting):** `[FACT]` Quỹ thành viên chỉ báo cáo định giá (NAV) định kỳ (tháng/quý) với khung pháp lý lỏng hơn. Ngược lại, quỹ mở bắt buộc tính NAV thường xuyên (ngày/tuần) và phải tuân thủ nghiêm ngặt các hạn mức đầu tư theo Thông tư 98/2020/TT-BTC `[REG]` (Nguồn: S-T1-001, Điều 15).
3. **Phân phối D2C vs. B2B / Bancassurance (Front Office):** `[FACT]` Khi bán D2C qua App tự xây (như DragonX của Dragon Capital), công ty quản lý quỹ phải gánh vác toàn bộ quy trình eKYC, AML và CSKH. Với kênh B2B/Brokerage, CTCK/Ngân hàng mẹ làm eKYC và chuyển lệnh qua tài khoản tổng hợp (Omnibus) (Nguồn: S-T1-010).
4. **Active vs. Passive Equity (Investment/Research):** `[FACT]` Quỹ chủ động (Active) yêu cầu đội ngũ Research khổng lồ để đọc BCTC, dự báo lợi nhuận (Alpha seeking) (Nguồn: S-T1-004). Quỹ thụ động (Passive) tập trung Value Chain vào hệ thống Rebalancing tự động để giảm thiểu Tracking Error (Nguồn: S-T1-100).
5. **Cổ phiếu vs. Trái phiếu (Trading & Execution):** `[FACT]` Cổ phiếu giao dịch khớp lệnh tập trung trên HOSE/HNX với STP (Straight-Through Processing). Trong khi đó, trái phiếu tại VN giao dịch thỏa thuận (OTC), yêu cầu Dealer đàm phán thủ công qua điện thoại/chat và xác nhận hợp đồng song phương (Nguồn: S-T1-008).
6. **Bán lẻ đại chúng vs. Định chế tài chính (Client Reporting):** `[FACT]` Khách hàng bán lẻ (Mass Retail) cần portal/app xem số dư tức thời và báo cáo hiệu suất được đơn giản hóa. Khách hàng định chế (Institutional) yêu cầu báo cáo Due Diligence, phân tích phân bổ tài sản (Attribution) chuyên sâu (Nguồn: S-T3-003).
7. **Tài sản tư nhân (PE) vs. Tài sản niêm yết (Public) (Sourcing & Valuation):** `[FACT]` Quỹ PE như VinaCapital VOF không có giá thị trường đóng cửa hàng ngày. Value chain của PE đòi hỏi Deal Sourcing thủ công, định giá bằng mô hình DCF/Multiples (thường dùng bên thứ ba) và tham gia quản trị doanh nghiệp (Board Seats) (Nguồn: S-T1-101).
8. **Thị trường tiền tệ / Trái phiếu ngắn hạn vs. Cổ phiếu (Liquidity Management):** `[FACT]` Quỹ tiền tệ/trái phiếu thanh khoản cao (như TCBF) phải xử lý khối lượng lệnh mua/bán (Subscription/Redemption) khổng lồ mỗi ngày. Đội ngũ quản lý rủi ro phải duy trì buffer tiền mặt và Repo liên tục để đảm bảo thanh khoản (T+0, T+1) so với quỹ cổ phiếu có độ trễ thanh toán (T+2) (Nguồn: S-T1-102).

---

## HANDOFF
- **Đã tạo gì:** `SEGMENTATION_MATRIX.md` (Ma trận 6 trục), định vị 10 công ty quản lý quỹ (Dragon Capital, SSIAM, VinaCapital, VCBF, MBCapital, BVF, PVI AM, Techcom Capital, VietinBank Capital, IPAAM).
- **Giả định gì:** Các dữ liệu thị trường (như white-space ở Smart Beta, Robo-Advisor) dựa trên hiện trạng pháp lý theo Nghị định 155 và Luật CK 2019 (S-T1-008, S-T1-002).
- **Thiếu gì:** Cần khảo sát thêm dữ liệu chi tiết nội bộ của nhóm PVI AM, BVF về tỷ trọng chính xác của khách hàng định chế so với bán lẻ nếu muốn phân tách tỷ trọng %.
- **Agent kế tiếp cần lưu ý gì:** Trong Phase 4 & 5 (Value Chain & AI Use Cases), lấy 8 điểm khác biệt chuỗi giá trị trong tài liệu này làm blueprint để sinh use case. Ví dụ: Dùng AI OCR cho lệnh thỏa thuận OTC trái phiếu (Điểm 5) hoặc AI eKYC/Chatbot cho kênh D2C (Điểm 3).
- **Trạng thái:** READY_FOR_AUDIT
