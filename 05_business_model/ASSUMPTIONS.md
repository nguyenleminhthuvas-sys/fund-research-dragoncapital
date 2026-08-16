# Các Giả Định Kinh Tế & Vận Hành (ASSUMPTIONS)

> Nội dung chưa được kiểm chứng nguồn. Dùng để tham khảo nội bộ, không trích vào báo cáo.

> **ACCESS DECLARATION**
> Tài liệu này mô tả các giả định làm cơ sở cho mô hình Unit Economics của một công ty quản lý quỹ tại Việt Nam.

## 1. Giả Định Nguồn Thu (Revenue Drivers)

- **[INFERENCE] Tỷ lệ Phí Quản lý (Management Fee):** Dựa trên mức trung bình thị trường (S-T2-001):
  - Quỹ mở Cổ phiếu: ~1.5% AUM/năm.
  - Quỹ mở Trái phiếu: ~1.0% AUM/năm.
  - Quỹ ETF: ~0.6% AUM/năm.
  - Quản lý danh mục ủy thác (Institutional/HNWI): ~0.5% AUM/năm.
  - **Giả định Blended Fee Rate:** Khoảng **1.2% AUM/năm** cho một AMC có danh mục đa dạng (50% Equity, 30% Fixed Income, 20% ETF).

- **[INFERENCE] Tỷ lệ Phí Phát hành/Mua lại (Subscription/Redemption Fee):** 
  - Thường dao động từ 0% - 1.5% tùy thời gian nắm giữ. Giả định mức phí bình quân **1.0%** áp dụng trên dòng tiền mới (New Money).
  - Giả định dòng tiền mới hàng năm = 20% AUM đầu kỳ.

- **[INFERENCE] Phí Hiệu quả (Performance Fee):** 
  - Phổ biến ở quỹ đóng, quỹ thành viên hoặc ủy thác cá nhân (thường 10-20% phần vượt hurdle rate). Khó dự phóng cố định, nên trong mô hình Break-even cơ bản, Performance Fee thường được xem là "upside" (thu nhập gia tăng) chứ không phải nguồn thu bù đắp chi phí cố định (fixed costs).

## 2. Giả Định Cấu Trúc Chi Phí (Cost Base Scenarios)

Dựa trên cấu trúc hoạt động của công ty quản lý quỹ nội địa, chi phí được phân thành 3 quy mô (Scenarios):

### Kịch bản 1: Boutique AMC (Chuyên biệt, < 5,000 tỷ VND)
Tập trung quản lý 1-2 quỹ chuyên biệt hoặc vài tài khoản ủy thác lớn.
- Nhân sự (FO/MO/BO - khoảng 20 người): 15 tỷ VND/năm.
- Dịch vụ ngoài (Giám sát, lưu ký, kiểm toán): 3 tỷ VND.
- IT & Terminal (Dữ liệu cơ bản như Bloomberg, hệ thống kế toán nội bộ): 2 tỷ VND.
- Marketing & Kênh phân phối: 0 tỷ (Dựa vào network cá nhân).
- Văn phòng/Vận hành chung: 5 tỷ VND.
- **[INFERENCE] Tổng Fixed Costs:** ~25 tỷ VND/năm.

### Kịch bản 2: Mid-sized AMC (Đa nền tảng, 10,000 - 30,000 tỷ VND)
Đa dạng hóa sản phẩm (quỹ mở, quỹ hưu trí, ủy thác).
- Nhân sự (khoảng 50 người): 40 tỷ VND/năm.
- Dịch vụ ngoài (Giám sát, lưu ký, kiểm toán): 8 tỷ VND.
- IT & Terminal (Hệ thống Core Fund Management chuẩn, CRM): 10 tỷ VND.
- Marketing & Kênh phân phối (Hoa hồng cho CTCK, nền tảng phân phối, quảng cáo): 12 tỷ VND.
- Văn phòng/Vận hành/Tuân thủ: 10 tỷ VND.
- **[INFERENCE] Tổng Fixed Costs:** ~80 tỷ VND/năm.

### Kịch bản 3: Full-stack AMC (Top Tier - e.g. DCVFM, > 50,000 tỷ VND)
Hệ sinh thái toàn diện, có năng lực tự doanh, quản lý chục quỹ và đa dạng kênh phân phối.
- Nhân sự (khoảng 100+ người): 120 tỷ VND/năm.
- Dịch vụ ngoài (Giám sát, lưu ký quốc tế/nội địa, dịch vụ tư vấn Big4): 20 tỷ VND.
- IT & Terminal (Hệ thống quốc tế hàng đầu như Charles River/Aladdin, bảo mật cao): 40 tỷ VND.
- Marketing & Kênh phân phối (Hệ thống đại lý rộng khắp, branding): 40 tỷ VND.
- Văn phòng/Vận hành/Tuân thủ: 30 tỷ VND.
- **[INFERENCE] Tổng Fixed Costs:** ~250 tỷ VND/năm.

## 3. Độ nhạy (Sensitivity / Operating Leverage)
- **[INFERENCE] Operating Leverage cao:** Trong mô hình Asset Management, chi phí hầu hết là cố định (nhân sự, IT, văn phòng chiếm ~70%-80%). Doanh thu phụ thuộc 90% vào AUM. Do đó, khi AUM tăng qua điểm hòa vốn, biên lợi nhuận ròng (Net Margin) sẽ mở rộng rất nhanh. Ngược lại, AUM giảm sẽ ăn mòn lợi nhuận nhanh chóng.

## 4. Bối cảnh số liệu tham chiếu (Reference)
- **[UNVERIFIED] DCVFM (2023):** Doanh thu đạt 1.017,17 tỷ đồng, lợi nhuận trước thuế 371,08 tỷ đồng [kỳ: 2023, đơn vị: Tỷ VND — source_id S-T4-001 không tồn tại trong SOURCE_REGISTRY.csv, chưa có raw file kiểm chứng].
- **[INFERENCE] Biên lợi nhuận trước thuế (Pre-tax Margin) của DCVFM:** ~36.5% trong năm 2023. Đây là mức biên lợi nhuận của một Full-stack AMC đã vượt xa điểm hòa vốn nhờ quy mô AUM khổng lồ (hàng chục nghìn tỷ đồng).

## HANDOFF
- Trạng thái: READY_FOR_AUDIT
