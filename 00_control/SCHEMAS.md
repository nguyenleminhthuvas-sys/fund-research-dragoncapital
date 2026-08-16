## 4. SCHEMAS.md — CHUẨN DỮ LIỆU HANDOFF

### 4.1 `SOURCE_REGISTRY.csv`
```
source_id, tier, loai_nguon, tieu_de, to_chuc_phat_hanh, url, ngay_xuat_ban,
ngay_truy_cap, ngon_ngu, do_tin_cay(1-5), pham_vi_dung, ghi_chu
```
`source_id` format: `S-T1-001`, `S-T3-047`.

### 4.2 `task_registry.csv` — artifact quan trọng nhất của dự án
```
task_id, tang, khoi_chuc_nang, quy_trinh_cap2, tac_vu_cap3, mo_ta_ngan,
input, nguon_input, output, nguoi_nhan_output, role_chinh, role_phu,
tan_suat, thoi_luong_uoc_tinh_phut, he_thong_dung, buoc_thu_cong,
diem_gay_pain_point, rang_buoc_phap_ly, do_tin_cay(FACT/INFERENCE),
source_ids, chi_tiet_ref, raw_ref
```
Định dạng raw_ref: _raw/<thư mục>/<tên file>#L<số dòng> hoặc #p<số trang> cho PDF.
`task_id` format: `{TANG}-{KHOI}-{QT}-{TV}` → ví dụ `FO-RES-03-02`, `BO-NAV-01-04`.

Mã tầng: `FO` (front), `MO` (middle), `BO` (back), `EN` (enabling).
Mã khối gợi ý: `PROD, IR, RES, IDEA, PC, TRD, MON` (FO) · `RSK, CMP, PERF, VAL, OPSO` (MO) · `STL, REC, NAV, FA, TA, CA, CUS, TAX` (BO) · `DATA, IT, LEG, HR, FIN, MKT` (EN).

### 4.3 `usecase_registry.csv` — 18 cột
```
uc_id, task_id_lien_ket, tang, khoi_chuc_nang, ten_use_case,
van_de_kinh_doanh, quy_trinh_hien_tai_theo_buoc, ai_lam_gi_o_buoc_nao,
nang_luc_ai(1-7), muc_tu_dong(assist/copilot/autonomous), human_in_the_loop,
kpi_cai_thien, uoc_tinh_roi, du_lieu_can_co, rang_buoc_phap_ly,
diem_gia_tri(1-5), diem_kha_thi(1-5), diem_du_lieu(1-5), diem_rui_ro(1-5),
tong_diem, ro(quick_win/chien_luoc/nghien_cuu), muc_do(VERIFIED/CATALOGUE),
source_ids, raw_ref
```
Định dạng raw_ref: _raw/<thư mục>/<tên file>#L<số dòng> hoặc #p<số trang> cho PDF.
`uc_id` format: `UC-{KHOI}-###`.

### 4.4 `role_cards.json`
```json
{
  "role_id": "FO-PM-EQ",
  "chuc_danh": "Portfolio Manager – Equity",
  "khoi": "Front Office",
  "bao_cao_cho": "CIO",
  "nhip_lam_viec": {"daily": [], "weekly": [], "monthly": [], "quarterly": [], "ad_hoc": []},
  "tac_vu": ["task_id", "..."],
  "he_thong_dung": [],
  "tac_vu_ton_thoi_gian_nhat": "",
  "loi_thuong_gap": [],
  "kpi_bi_cham": [],
  "do_tin_cay": "FACT|INFERENCE",
  "source_ids": []
}
```

### 4.5 `entity_map.json`
```json
{
  "entity_id": "",
  "ten_phap_nhan": "",
  "ma_ck": "",
  "vai_tro_trong_group": "",
  "nghiep_vu_duoc_cap_phep": [],
  "san_pham_quan_ly": [],
  "co_quan_quan_ly": [],
  "nghia_vu_cbtt": [],
  "source_ids": []
}
```

---
