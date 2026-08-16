# MÔ HÌNH KINH TẾ HỌC ĐƠN VỊ & P&L (UNIT ECONOMICS)

> Đây là mô hình minh hoạ, mọi con số là giả định ghi tại ASSUMPTIONS.md, không phải số đo thực tế của bất kỳ công ty nào.

> **ACCESS DECLARATION**
> Tài liệu này mô phỏng Business Model của công ty quản lý quỹ, đối chiếu với số liệu thực tế (DCVFM 2023) để nhận diện các vùng chi phí cần tối ưu hóa bằng công nghệ/AI.

## 1. Công thức P&L (Profit & Loss) mẫu của AMC

Một công ty quản lý quỹ (Asset Management Company - AMC) hoạt động dựa trên phương trình lợi nhuận cơ bản sau:

**LỢI NHUẬN (PROFIT) = TỔNG DOANH THU (TOTAL REVENUE) - TỔNG CHI PHÍ (TOTAL COSTS)**

### Các Nguồn Doanh Thu (Revenue Sources):
**[INFERENCE] Phương trình Doanh Thu:**
`Tổng Doanh Thu = (AUM × % Management Fee) + Performance Fee + (New Inflows × % Subscription Fee) + (Redemptions × % Redemption Fee) + (Mandate AUM × % Mandate Fee) + Advisory Fees`
- **Management Fee (Phí quản lý):** Thu nhập cốt lõi, ổn định, tính theo % NAV hàng ngày/tháng.
- **Performance Fee (Phí thưởng hiệu quả):** Không ổn định, dựa trên mức vượt hurdle rate/benchmark.
- **Phí phát hành/mua lại:** Thu trên dòng tiền ra/vào quỹ mở.
- **Phí quản lý danh mục ủy thác (Mandate):** Phí cho các tài khoản riêng biệt.
- **Phí tư vấn:** Các dịch vụ tư vấn tài chính doanh nghiệp hoặc cấu trúc vốn.

### Các Hạng Mục Chi Phí (Cost Items):
**[INFERENCE] Phương trình Chi Phí:**
`Tổng Chi Phí = Fixed Costs (Nhân sự + IT + Văn phòng) + Variable Costs (Phí Giám sát + Phân phối + Thuế)`
- **Nhân sự (FO/MO/BO):** Chi phí lớn nhất (Lương, thưởng, phúc lợi).
- **Ngân hàng giám sát & Đại lý chuyển nhượng (Transfer Agent) & Kiểm toán:** Phí trả cho bên thứ 3 để đảm bảo tính minh bạch.
- **Dữ liệu & Terminal:** Bloomberg, Reuters, hệ thống dữ liệu vĩ mô.
- **Công nghệ (IT):** Hệ thống Core Fund (Charles River, Aladdin, Fiin), Cloud, Security.
- **Marketing & Kênh phân phối:** Hoa hồng trả cho Distributor, quảng cáo số.
- **Tuân thủ & Pháp lý:** Chi phí duy trì chuẩn mực regulatory.
- **Vận hành chung:** Thuê văn phòng, hành chính.

---

## 2. Điểm Hòa Vốn (Break-even AUM) qua 3 Kịch Bản Chi Phí

Dựa vào bộ giả định tại `/05_business_model/ASSUMPTIONS.md` (với Blended Fee Rate = 1.2% AUM/năm):

| Kịch Bản (Scenario) | Tổng Fixed Cost | Điểm Hòa Vốn (AUM) | Đặc Điểm Mô Hình |
|---|---|---|---|
| **1. Boutique AMC** | ~25 tỷ VND | **~2,083 tỷ VND** | Tập trung ngách (Niche), nhân sự siêu tinh gọn, outsource tối đa MO/BO. |
| **2. Mid-sized AMC** | ~80 tỷ VND | **~6,666 tỷ VND** | Phân phối qua kênh số, phát triển quỹ mở đại chúng, áp dụng hệ thống chuẩn. |
| **3. Full-stack AMC** | ~250 tỷ VND | **~20,833 tỷ VND** | Hệ sinh thái đầy đủ chức năng, chi phí IT & Compliance khổng lồ, ví dụ Top 5 thị trường. |

**[INFERENCE] Kết luận Điểm hòa vốn:** AUM là sinh mệnh. Dưới mốc 2,000 tỷ VND, các quỹ sẽ phải bù lỗ hoạt động liên tục hoặc chỉ dựa vào Performance Fee (rất rủi ro).

---

## 3. Độ Nhạy Lợi Nhuận (Operating Leverage)

Đòn bẩy hoạt động (Operating Leverage) của AMC rất cao do cấu trúc chi phí chủ yếu là cố định. Lấy ví dụ **Mid-sized AMC** (AUM cơ sở = 10,000 tỷ VND, Fixed Cost = 80 tỷ, Base Revenue = 120 tỷ, Base Profit = 40 tỷ):

| Kịch bản thị trường | AUM giả định | Doanh thu (1.2%) | Chi phí | Lợi nhuận | Biến động Lợi nhuận so với Base |
|---|---|---|---|---|---|
| **Base Case** | 10,000 tỷ | 120 tỷ | 80 tỷ | 40 tỷ | 0% |
| **AUM giảm 10%** | 9,000 tỷ | 108 tỷ | 80 tỷ | 28 tỷ | **Giảm 30%** |
| **AUM giảm 20%** | 8,000 tỷ | 96 tỷ | 80 tỷ | 16 tỷ | **Giảm 60%** |
| **AUM giảm 30%** | 7,000 tỷ | 84 tỷ | 80 tỷ | 4 tỷ | **Giảm 90%** |

**[INFERENCE] Nhận xét:** Do đặc thù "Fixed Cost nặng", một mức giảm 10% của AUM (do thị trường chứng khoán rớt điểm hoặc bị rút vốn) có thể thổi bay 30% lợi nhuận. Điều này ép các AMC phải biến cấu trúc Fixed Cost thành Variable Cost thông qua công nghệ và AI.

---

## 4. Đối Chiếu Thực Tế: BCTC DCVFM (2023)

- **[UNVERIFIED]** Doanh thu năm 2023 của Dragon Capital Việt Nam (DCVFM) đạt 1.017,17 tỷ đồng, giảm 8% so với 2022. Lợi nhuận trước thuế đạt 371,08 tỷ đồng, giảm 33% so với 2022 [kỳ: 2023, đơn vị: Tỷ VND — source_id S-T4-001 không tồn tại trong SOURCE_REGISTRY.csv, chưa có raw file kiểm chứng].
- **[INFERENCE] Kiểm chứng đòn bẩy hoạt động:** Khi doanh thu giảm 8% (90,67 tỷ đồng) do AUM/thị trường đi xuống, lợi nhuận trước thuế của DCVFM lại giảm tới 33% (182,92 tỷ đồng). Điều này hoàn toàn khớp với bài test độ nhạy (Sensitivity) ở phần 3: **Operating Leverage ở các quỹ là cực kỳ sắc bén**. Lợi nhuận rớt nhanh gấp nhiều lần so với mức rớt của doanh thu.
- **[INFERENCE] Vị thế Full-stack:** Với mức lợi nhuận 371 tỷ đồng, DCVFM vượt xa điểm hòa vốn của kịch bản Full-stack (~250 tỷ chi phí), khẳng định lợi thế quy mô tuyệt đối của Top 1 thị trường.

---

## 5. Kết Luận: "Bản đồ use case nào có tiền"

Để tối ưu hóa biên lợi nhuận trong chu kỳ Fee Compression (áp lực giảm phí), ngành quản lý quỹ cần nhìn vào "Bản đồ có tiền" sau đây:

### 10 Hạng Mục Chi Phí Lớn Nhất Cần Cắt Giảm/Tối Ưu:
1. **Quỹ lương chuyên gia (FO - PM/Analyst):** Khả năng dùng AI Copilot để tăng năng suất 1 Analyst cover từ 15 mã lên 30 mã.
2. **Chi phí hệ thống phần mềm (Core Fund/Charles River/Aladdin):** Quá đắt đỏ.
3. **Phí Terminal (Bloomberg/Refinitiv):** Cần thay thế một phần bằng Data Scraping + LLM nội bộ.
4. **Chi phí tuân thủ pháp lý (Compliance):** Rà soát hàng nghìn trang văn bản thủ công. (Use case: AI Legal Checker).
5. **Marketing & Acquisition (CAC):** Chạy quảng cáo mở tài khoản đắt đỏ (Use case: Hyper-personalized AI marketing).
6. **Chi phí nhân sự Middle Office (Kiểm soát rủi ro, đối soát giao dịch):** Lương cao, công việc lặp lại.
7. **Chi phí nhân sự Back Office (Kế toán quỹ, báo cáo):** Lên báo cáo NAV thủ công hàng ngày.
8. **Phí ngân hàng giám sát & Lưu ký:** Khó mặc cả do rào cản quy định, nhưng có thể tự động hóa khâu đối soát để giảm phụ phí.
9. **Chi phí Customer Service (CS):** Trả lời thắc mắc của hàng ngàn nhà đầu tư retail. (Use case: AI Agent tư vấn 24/7).
10. **Chi phí chuyển đổi số (Transformation):** Cần nguồn lực nội bộ để không bị phụ thuộc hoàn toàn vào Vendor nước ngoài đắt đỏ.

### 5 Nguồn Doanh Thu Đang Bị Ép (Nhu Cầu Tạo Giá Trị Mới):
1. **Phí quản lý (Management Fee) của quỹ mở chủ động:** Bị ép xuống bởi xu hướng Passive/ETF. (Nhu cầu: Giảm chi phí để hạ TER hoặc dùng AI tìm ra Alpha rõ rệt).
2. **Phí hoa hồng phân phối (Retrocession):** Kênh ngân hàng đòi hỏi chia sẻ doanh thu ngày càng lớn. (Nhu cầu: Kênh D2C - Direct to Consumer riêng).
3. **Phí phát hành (Front-end load):** Khách hàng ngày càng nhạy cảm với phí mở tài khoản/đầu tư ban đầu.
4. **Phí quản lý danh mục ủy thác:** Khách hàng định chế đòi hỏi sự minh bạch và report real-time.
5. **Nguồn thu từ Private Equity:** Chịu áp lực về thanh khoản và chi phí Due Diligence thủ công rất cao.

## HANDOFF
- **Đã tạo gì:** 
  - `/05_business_model/ASSUMPTIONS.md`: Toàn bộ giả định mô hình.
  - `/05_business_model/UNIT_ECONOMICS.md`: P&L mẫu, 3 kịch bản hòa vốn, Sensitivity Analysis (giảm 10/20/30% AUM), đối chiếu thực tế với DCVFM 2023, Bản đồ 10 chi phí & 5 nguồn thu bị ép.
- **Trạng thái:** READY_FOR_AUDIT
