# FETCH_LOG.md — GHI LOG URL FETCH

# Giai đoạn A — Thu thập dữ liệu Back Office NAV & Fund Accounting

# Ngày: 14/08/2026

## URL MỞ ĐƯỢC (Saved to _raw/)

| URL                                                                        | Kết quả | File lưu                                                           |
| -------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------- |
| https://www.ssctech.com/solutions/fund-administration                      | 200 OK    | _raw/vendor/ssc-fund-administration-page.html (131KB)               |
| https://clearwateranalytics.com/solutions/investment-accounting-reporting/ | 200 OK    | _raw/vendor/clearwater-investment-accounting-reporting.html (131KB) |
| https://www.ssctech.com/industry/asset-management                          | 200 OK    | _raw/vendor/ssc-asset-management-industry.html (129KB)              |
| https://www.broadridge.com/financial-services/asset-management             | 200 OK    | _raw/vendor/broadridge-asset-management.html (32KB)                 |
| https://www.enfusion.com/solutions                                         | 200 OK    | _raw/vendor/enfusion-solutions-listing.html (152KB)                 |
| https://vn.linkedin.com/jobs/fund-accountant-jobs                          | 200 OK    | _raw/jd/linkedin-fund-accountant-vietnam-listing.html (30KB)        |
| https://fmarket.vn/quy/DCDS                                                | 200 OK    | _raw/company/fmarket-dcds-fund-page.html (110KB)                    |

## URL LỖI

### SimCorp — Toàn bộ URL product đang 404

- https://www.simcorp.com/en/solutions/investment-management-platform/accounting-and-corporate-actions → 404
- https://www.simcorp.com/en/platform/front-to-back/accounting → 404
- https://www.simcorp.com/en/investment-operations/accounting → 404
- https://www.simcorp.com/en/solutions/accounting-and-valuation → 404
- https://www.simcorp.com/en/investment-management-software/accounting → 404
- https://www.simcorp.com/en/solutions/buy-side-front-to-back/accounting → 404
- https://www.simcorp.com/en/solutions/investment-accounting-services → 404
- https://www.simcorp.com/en/platform → 404
- https://www.simcorp.com (homepage) → trả về nhưng không có link accounting nào trong HTML
- **Đánh giá:** Website SimCorp có vẻ đã đổi cấu trúc URL. Cần dùng browser thật hoặc search site:simcorp.com để tìm URL đúng.

### FIS InvestOne — 404

- https://www.fisglobal.com/en/solutions/institutional-asset-management/fund-administration → 404
- https://www.fisglobal.com/en/solutions/capital-markets/fund-administration → 404
- https://www.fisglobal.com/en/solutions/asset-managers → 404
- **Đánh giá:** FIS có thể đã rebrand/restructure. URL product chính xác cần xác minh.

### Clearwater — một số URL 404

- https://clearwateranalytics.com/solutions/accounting/ → 404
- https://clearwateranalytics.com/platform/accounting → 404
- (Đã tìm được URL đúng: /solutions/investment-accounting-reporting/ → saved thành công)

### Enfusion

- https://www.enfusion.com/solutions/fund-administration → 404
- (Đã tìm được: /solutions listing → saved)

### DCVFM — Timeout

- https://dcvfm.com.vn/vi/quy-mo-cua-cong-ty/ban-cao-bach → Connection timeout
- **Đánh giá:** dcvfm.com.vn hiện không phản hồi. Cần thử lại sau hoặc dùng browser.

### VCBF — DNS không resolve

- https://vcbf.com.vn/en/fund/vcbf-bcf → no such host
- https://vbcf.com.vn/download-de/ban-cao-bach/ → no such host
- https://www.vcbf.com.vn → timeout
- **Đánh giá:** Domain vcbf.com.vn có vẻ không hoạt động. Cần xác minh tên miền đúng.

### VietnamWorks — 403 (block bot)

- https://www.vietnamworks.com/en/fund-accountant-jobs → 403 Forbidden

### LinkedIn — Trả về HTML nhưng không có nội dung JD thật

- https://www.linkedin.com/jobs/fund-accountant-jobs-vietnam → HTML shell (JS-rendered, không có JD text)
- https://vn.linkedin.com/jobs/fund-accountant-jobs → tương tự (30KB nhưng là HTML framework, không có job text)
- **Đánh giá:** LinkedIn dùng client-side rendering. File đã save là HTML shell không có nội dung JD. Cần browser thật để đọc JD thật.

### thuvienphapluat.vn — Redirect sai

- https://thuvienphapluat.vn/van-ban/Tai-chinh-nha-nuoc/Thong-tu-98-2020-TT-BTC-hoat-dong-quan-ly-quy-dau-tu-chung-khoan-456699.aspx → redirect sang văn bản số 4179/VBHN-BLĐTBXH (không liên quan)
- **Đánh giá:** Đây là lỗi redirect của thuvienphapluat.vn. Nội dung TT98 điều 20 được thu thập từ search web thay thế.

### Cập nhật 14/08/2026: Dọn dẹp _raw/

- Đã di chuyển `_raw/vendor/simcorp-nav-fund-accounting-features-research-summary.txt` sang `01_lexicon/agent_notes/`. Lý do: Đây là bản tóm tắt do AI viết, không phải tài liệu gốc.
- Đã di chuyển `_raw/legal/TT98_2020_dieu20_NAV.txt` sang `01_lexicon/agent_notes/`. Lý do: Đây là bản tóm tắt do AI viết, không phải tài liệu gốc.
- Đã đổi đuôi toàn bộ các file `.html` còn lại trong `_raw/` thành `.md` để phản ánh đúng nội dung (markdown text trích xuất).

## LẦN FETCH 2 - TÌM BẢN GỐC (THẤT BẠI)

### MỤC TIÊU 1: Toàn văn Thông tư 98/2020/TT-BTC

- https://vanban.chinhphu.vn/?pageid=27160&docid=201060 → Trả về HTML thành công (200 OK) nhưng nội dung là "Nghị quyết số 1001/NQ-UBTVQH14", không phải TT98.
- https://luatvietnam.vn/tai-chinh/thong-tu-98-2020-tt-btc-hoat-dong-va-quan-ly-quy-dau-tu-chung-khoan-195975-d1.html → 200 OK nhưng nội dung là "Công văn 10991/BGTVT-CYT".
- https://vbpl.vn/btc/Pages/vbpq-van-ban-goc.aspx?ItemID=145062 → 403 Forbidden.
- https://ssc.gov.vn/ubck/faces/oracle/webcenter/portalapp/pages/vi/vbpl/vbpqDetail.jspx?_afrLoop=16985843817906936&dDocName=APPSSCGOVVN162054370&_afrWindowMode=0&_adf.ctrl-state=1d6z8k80uy_4 → 404 Not Found.
- https://thuvienphapluat.vn/van-ban/Tai-chinh-nha-nuoc/Van-ban-hop-nhat-04-VBHN-BTC-2026-quan-ly-quy-dau-tu-chung-khoan-621999.aspx → 200 OK nhưng không tìm thấy nội dung "Điều 20" hoặc văn bản TT98 bên trong (chỉ có shell UI).

### MỤC TIÊU 2: Bản cáo bạch quỹ mở (PDF)

- https://fundmanagement-miraeasset.com.vn/vi/document/fund → 404 Not Found
- https://www.baovietfund.com.vn/vi/quy/BVBF/tai-lieu → 404 Not Found
- https://www.baovietfund.com.vn/vi/cong-bo-thong-tin/ban-cao-bach → 404 Not Found
- https://dragoncapital.com.vn/vi/quy/dcds/tai-lieu-quy → 404 Not Found
- https://dragoncapital.com.vn/vi/tai-lieu-bao-cao?fund=DCDS&year=2024&type=prospectus → 404 Not Found
- https://mediacdn.vn/upload/4-2025/0-files/DCDS_ban_cao_bach_2025.pdf → Lỗi DNS: lookup mediacdn.vn: no such host
- https://www.scribd.com/document/DCDS-ban-cao-bach → 404 Not Found
- https://dcvfm.com.vn/vi/quy/dcds → Lỗi Timeout
- https://cafef.vn/quy/DCDS-quy-dau-tu-chung-khoan-nang-dong-dc.chn → 404 Not Found
- https://fmarket.vn/quy/DCDS / https://fmarket.vn/tai-lieu-quy → 200 OK nhưng website là Single Page Application (Angular), thẻ nội dung rỗng/chỉ chứa HTML shell, không trích được link PDF.

## LẦN FETCH 3 — 15/08/2026 (4 URL còn lại)

### URL #4 ✅ THÀNH CÔNG

- **URL:** https://static2.vietstock.vn/vietstock/2023/1/18/20230118_20230118___e1vfvn30___ban_cao_bach_cap_nhat_thang_1_2023.pdf
- **Kết quả:** 200 OK — PDF tải được
- **File lưu:** `_raw/company/vietstock-e1vfvn30-ban-cao-bach-cap-nhat-2023-01.pdf` (15 MB)
- **Nội dung:** Bản cáo bạch cập nhật tháng 1/2023 — E1VFVN30 (ETF theo dõi VN30)
- **Ghi chú:** File có thể là bản cáo bạch của VFM ETF theo dõi VN30, không phải VFMVF1. Cần kiểm tra nội dung.

### URL #5 ✅ THÀNH CÔNG

- **URL:** https://img.baovietfund.com.vn/resource/10122018/1544456984_bancaobachquybvfedsuadoithang11.2018.pdf
- **Kết quả:** 200 OK — PDF tải được
- **File lưu:** `_raw/company/baovietfund-bvfed-ban-cao-bach-2018-11.pdf` (1.8 MB)
- **Nội dung:** Bản cáo bạch quỹ BVFED — Bảo Việt Fund, sửa đổi tháng 11/2018

### URL #6 ❌ SPA — KHÔNG CÓ PDF LINK TRONG HTML

- **URL:** https://www.dragoncapital.com.vn/individual/vi/report
- **Kết quả:** 200 OK nhưng là Salesforce Experience Cloud (LWR framework) — toàn bộ content render bằng JavaScript
- **HTML tĩnh:** Chứa SPA bootstrap scripts, không có link .pdf nào, không có link azureedge.net nào
- **Hành động:** Bỏ qua theo LUẬT FETCH §3.9 điều 5. KHÔNG đoán URL CDN.

### URL #7 ❌ AJAX-RENDERED — KHÔNG CÓ PDF LINK TRONG HTML TĨNH

- **URL:** https://finance.vietstock.vn/VFMVF1/tai-tai-lieu.htm
- **Kết quả:** 200 OK, HTML server-rendered có cấu trúc trang, nhưng danh sách tài liệu load qua AJAX/API riêng
- **HTML tĩnh:** Không có link .pdf nào trong HTML trả về
- **Hành động:** Bỏ qua theo LUẬT FETCH §3.9 điều 5. KHÔNG đoán API endpoint.
- **Ghi chú:** Tên trang ghi "DCDS" trong `<title>` — có thể URL VFMVF1 thực ra điều hướng sang fund DCDS. Cần xác minh.

## VIỆC 2 — XOÁ FILE RỖNG (15/08/2026)

Đã xoá 2 file HTML shell không có nội dung thật:

- ❌ `_raw/jd/linkedin-fund-accountant-vietnam-listing.md` (30KB) — LinkedIn JS-rendered shell, không có JD text
- ❌ `_raw/company/fmarket-dcds-fund-page.md` (107KB) — Fmarket Angular SPA shell, không có link PDF

## VIỆC 3 — THU THẬP JD (15/08/2026)

### JD URL kết quả

| URL                                                                             | Kết quả        | File                                                                | Loại                  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------- | ---------------------- |
| https://www.vndirect.com.vn/tuyen_dung/ke-toan-quy-ipaam/                       | ❌ 403 Forbidden | —                                                                  | —                     |
| https://vietcapital.com.vn/careers/analyst-officer                              | ✅ 200 OK        | `_raw/jd/vietcapital-jd-analyst-officer-fund.md` (18KB)           | Tin tuyển dụng thật |
| https://vietcapital.com.vn/careers/ke-toan-quy                                  | ✅ 200 OK        | `_raw/jd/vietcapital-jd-ke-toan-quy.md` (17KB)                    | Tin tuyển dụng thật |
| https://vietcapital.com.vn/careers/senior-fund-accounting-officer               | ✅ 200 OK        | `_raw/jd/vietcapital-jd-senior-fund-accounting-officer.md` (18KB) | Tin tuyển dụng thật |
| https://www.velvetjobs.com/job-descriptions/fund-accountant                     | ✅ 200 OK        | `_raw/jd/velvetjobs-jd-fund-accountant.md` (18KB)                 | Mẫu JD tổng hợp     |
| https://www.velvetjobs.com/job-descriptions/accountant-fund-accountant          | ✅ 200 OK        | `_raw/jd/velvetjobs-jd-accountant-fund-accountant.md` (18KB)      | Mẫu JD tổng hợp     |
| https://snaphunt.com/resources/job-descriptions/fund-accountant-job-description | ❌ 404 Not Found | —                                                                  | —                     |
| https://www.jobed.ai/fund-accountant                                            | ✅ 200 OK        | `_raw/jd/jobed-ai-jd-fund-accountant.md` (4.3KB)                  | Mẫu JD tổng hợp     |
| https://singapore.recruit.net/search-fund-accountant-jobs                       | ❌ 403 Forbidden | —                                                                  | —                     |
