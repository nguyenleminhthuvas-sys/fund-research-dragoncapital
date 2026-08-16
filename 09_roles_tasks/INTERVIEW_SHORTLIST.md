# BỘ CÂU HỎI PHỎNG VẤN RÚT GỌN (45 PHÚT) - KHỐI BACK OFFICE

Bản rút gọn này tập trung vào 8 tác vụ cốt lõi nhất, thỏa mãn tiêu chí:

- Tần suất diễn ra hàng ngày (daily).
- Có ràng buộc pháp lý chặt chẽ (Thông tư 98/2020/TT-BTC, VSDC).
- Trọng tâm vào nghiệp vụ tính toán NAV & Fund Accounting.

Mục tiêu chính là thu thập thông tin để điền vào 3 cột còn thiếu trong registry: `thoi_luong_uoc_tinh_phut`, `he_thong_dung`, và `buoc_thu_cong`.

---

## I. CÂU HỎI MỞ ĐẦU (Warming up)

1. Một ngày làm việc điển hình của anh/chị diễn ra như thế nào từ lúc mở máy đến lúc về?
2. Trong các công việc hàng ngày, việc gì đang tiêu tốn nhiều thời gian của anh/chị nhất?
3. Sự cố gần nhất mà bộ phận gặp phải là gì? Anh/chị đã xử lý nó như thế nào?
4. Dữ liệu chính để anh/chị làm việc đang nằm ở đâu? (Excel, hệ thống cũ, email, portal của bên thứ 3?)
5. Có báo cáo nào anh/chị phải làm lặp đi lặp lại hàng ngày/hàng tuần mà thấy rất nhàm chán không?

---

## II. 8 TÁC VỤ ƯU TIÊN CAO NHẤT

### 1. T-BO-001: Lấy giá đóng cửa cổ phiếu trước ngày định giá

*Lý do ưu tiên: Làm hàng ngày, quy định bởi TT98/2020, ảnh hưởng trực tiếp đến NAV toàn quỹ.*

- Bước này anh/chị làm mất khoảng bao lâu, và bao lâu làm một lần? *(Ánh xạ: thoi_luong_uoc_tinh_phut & tan_suat)*
- Anh/chị thao tác trên phần mềm nào ở bước này? *(Ánh xạ: he_thong_dung)*
- Trong bước này có đoạn nào phải làm thủ công không, đoạn nào? *(Ánh xạ: buoc_thu_cong)*

### 2. T-BO-002: Định giá trái phiếu không giao dịch bằng đường cong lợi suất VBMA

*Lý do ưu tiên: Làm hàng ngày, quy định pháp lý khắt khe, dễ xảy ra sai sót dữ liệu ngoại lai.*

- Bước này anh/chị làm mất khoảng bao lâu, và bao lâu làm một lần? *(Ánh xạ: thoi_luong_uoc_tinh_phut & tan_suat)*
- Anh/chị thao tác trên phần mềm nào ở bước này? *(Ánh xạ: he_thong_dung)*
- Trong bước này có đoạn nào phải làm thủ công không, đoạn nào? *(Ánh xạ: buoc_thu_cong)*

### 3. T-BO-004: Tính toán tổng tài sản và NAV / lô CCQ

*Lý do ưu tiên: Core operation hàng ngày, chốt NAV cuối cùng, tuân thủ TT98/2020.*

- Bước này anh/chị làm mất khoảng bao lâu, và bao lâu làm một lần? *(Ánh xạ: thoi_luong_uoc_tinh_phut & tan_suat)*
- Anh/chị thao tác trên phần mềm nào ở bước này? *(Ánh xạ: he_thong_dung)*
- Trong bước này có đoạn nào phải làm thủ công không, đoạn nào? *(Ánh xạ: buoc_thu_cong)*

### 4. T-BO-006: Công bố NAV lên trang web và các phương tiện thông tin

*Lý do ưu tiên: Ràng buộc phải công bố trong vòng 3 ngày, làm hàng ngày, là điểm chạm với KH.*

- Bước này anh/chị làm mất khoảng bao lâu, và bao lâu làm một lần? *(Ánh xạ: thoi_luong_uoc_tinh_phut & tan_suat)*
- Anh/chị thao tác trên phần mềm nào ở bước này? *(Ánh xạ: he_thong_dung)*
- Trong bước này có đoạn nào phải làm thủ công không, đoạn nào? *(Ánh xạ: buoc_thu_cong)*

### 5. T-BO-007: Xác nhận phiếu lệnh giao dịch (Mua/Bán)

*Lý do ưu tiên: Làm hàng ngày mỗi phiên giao dịch CCQ, rủi ro pháp lý cao nếu lệnh sai sót.*

- Bước này anh/chị làm mất khoảng bao lâu, và bao lâu làm một lần? *(Ánh xạ: thoi_luong_uoc_tinh_phut & tan_suat)*
- Anh/chị thao tác trên phần mềm nào ở bước này? *(Ánh xạ: he_thong_dung)*
- Trong bước này có đoạn nào phải làm thủ công không, đoạn nào? *(Ánh xạ: buoc_thu_cong)*

### 6. T-BO-008: Tính toán số lượng CCQ phân bổ cho lệnh mua

*Lý do ưu tiên: Yêu cầu chính xác cao, khớp tiền quỹ và số dư chứng chỉ của nhà đầu tư.*

- Bước này anh/chị làm mất khoảng bao lâu, và bao lâu làm một lần? *(Ánh xạ: thoi_luong_uoc_tinh_phut & tan_suat)*
- Anh/chị thao tác trên phần mềm nào ở bước này? *(Ánh xạ: he_thong_dung)*
- Trong bước này có đoạn nào phải làm thủ công không, đoạn nào? *(Ánh xạ: buoc_thu_cong)*

### 7. T-BO-018: Kiểm soát thời gian đóng sổ lệnh đại lý phân phối

*Lý do ưu tiên: Ràng buộc nghiêm ngặt với giờ giao dịch của Sở GDCK, thường xảy ra lọt lệnh.*

- Bước này anh/chị làm mất khoảng bao lâu, và bao lâu làm một lần? *(Ánh xạ: thoi_luong_uoc_tinh_phut & tan_suat)*
- Anh/chị thao tác trên phần mềm nào ở bước này? *(Ánh xạ: he_thong_dung)*
- Trong bước này có đoạn nào phải làm thủ công không, đoạn nào? *(Ánh xạ: buoc_thu_cong)*

### 8. T-BO-030: Đối chiếu số dư tiền và chứng khoán nội bộ với Ngân hàng lưu ký

*Lý do ưu tiên: Tần suất đối chiếu hàng ngày, thao tác qua nhiều hệ thống gây mất thời gian.*

- Bước này anh/chị làm mất khoảng bao lâu, và bao lâu làm một lần? *(Ánh xạ: thoi_luong_uoc_tinh_phut & tan_suat)*
- Anh/chị thao tác trên phần mềm nào ở bước này? *(Ánh xạ: he_thong_dung)*
- Trong bước này có đoạn nào phải làm thủ công không, đoạn nào? *(Ánh xạ: buoc_thu_cong)*

---

## III. CÂU HỎI KẾT THÚC (Wrap-up)

6. Theo anh/chị, việc gì trong toàn bộ quy trình vừa kể trên tuyệt đối không được để máy làm mà bắt buộc phải do con người tự kiểm duyệt?
7. Nếu ngay ngày mai có một công cụ Trợ lý AI, anh/chị sẽ giao việc gì cho nó đầu tiên?
8. Trong khối Back Office (NAV/Settlement), theo anh/chị, em nên phỏng vấn thêm ai để nắm rõ hơn về những tắc nghẽn hệ thống?
