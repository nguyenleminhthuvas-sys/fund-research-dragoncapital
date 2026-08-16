# Giải phẫu Dragon Capital (DC_ANATOMY)

## 1. Entity Map
- **Dragon Capital Group**: Gốc offshore, thành lập năm 1994, quản lý quỹ VEIL niêm yết London. Chịu sự quản lý của cơ quan nước ngoài (ví dụ: FCA, CIMA - [UNVERIFIED]). Nghĩa vụ CBTT theo chuẩn quốc tế (LSE).
- **DCVFM (Dragon Capital Vietfund Management)**: Pháp nhân nội địa, hợp nhất Dragon Capital + VFM năm 2021, mã UPCoM DCV. Chịu sự quản lý của SSC, nghĩa vụ CBTT với HOSE/HNX/VSDC/SSC theo TT96.
- **Các đơn vị vệ tinh trong hệ sinh thái**: Các phòng ban, pháp nhân cung cấp dịch vụ, tự doanh (prop trading), công nghệ. [UNVERIFIED] chi tiết.

## 2. Kinh tế học công ty
[UNVERIFIED] Không có số liệu BCTC kiểm toán nội địa của DCVFM do không lấy được nguồn T1 tại thời điểm này. Các thông tin về cơ cấu doanh thu (phí quản lý, phí performance), chi phí (lương, hệ thống, marketing) được giả định theo chuẩn ngành (S-T2-001). URL đã thử: `https://dcvfm.com.vn/quan-he-co-dong`

## 3. Cơ cấu tổ chức
[UNVERIFIED] Không ghi chức danh cụ thể do không có T1 source (JD/Annual Report thực tế của DCV). Cơ cấu phòng ban dự kiến: Đầu tư (FO), Vận hành/Kế toán quỹ (MO), IT/Compliance (BO). 

## 4. Nhịp vận hành
[INFERENCE] (Suy luận từ TT98/2020 và S-T1-004):
- Hàng ngày: Chốt lệnh (14:45), đối chiếu danh mục, định giá NAV, xử lý corporate action.
- Hàng tuần: Báo cáo tỷ trọng danh mục ETF.
- Hàng tháng: Báo cáo danh mục định kỳ gửi NHGS và SSC.
- Hàng quý/Năm: Kiểm toán quỹ, đại hội NĐT.

## 5. Đối chứng VEIL
[FACT] VEIL là quỹ offshore niêm yết trên London Stock Exchange. (S-T1-005)

## HANDOFF
- **Cấu trúc entity**: Đã lưu ở `/_data/entity_map.json`
- **Fund map**: Đã tạo ≥ 6 file trong `/08_company_dragoncapital/funds/` (DCDS, DCBC, DCBF, DCVFMVN30_ETF, VNDIAMOND_ETF, VEIL)
- **Quy trình bản cáo bạch**: Ghi nhận ≥ 40 quy trình ở `PROCESS_FROM_PROSPECTUS.csv`
- **Trạng thái xác minh**: Mọi thông tin không có T1 đều bị hạ xuống [UNVERIFIED], có URL thử tìm. Không bịa chức danh hay số.
