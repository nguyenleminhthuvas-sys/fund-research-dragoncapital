#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dựng index.html từ report_template.html + dữ liệu trong _data/.
Chạy: python3 build_report.py
Chỉ đọc CSV và bơm JSON vào template. Không sinh nội dung nghiệp vụ.
"""
import csv, json, os, datetime, re

BASE = os.path.dirname(os.path.abspath(__file__))
D    = os.path.join(BASE, "_data")
OUT  = os.path.join(BASE, "12_report", "index.html")
TPL  = os.path.join(BASE, "report_template.html")

def read(p):
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f))

tasks    = read(os.path.join(D, "task_registry.csv"))
usecases = read(os.path.join(D, "usecase_registry.csv"))
try:
    sources = read(os.path.join(D, "SOURCE_REGISTRY.csv"))
except FileNotFoundError:
    sources = []

n_task = len(tasks)
n_uc   = len(usecases)
blocks = sorted({t["khoi_chuc_nang"] for t in tasks})
pain   = sum(1 for t in tasks if t.get("diem_gay_pain_point", "").strip())
ask    = sum(1 for t in tasks if t.get("can_phong_van", "").strip().upper() == "Y")
quick  = sum(1 for u in usecases if u.get("ro") == "Quick win")
verif  = sum(1 for u in usecases if u.get("muc_do") == "VERIFIED")
no_dur = sum(1 for t in tasks if not t.get("thoi_luong_uoc_tinh_phut", "").strip())
no_sys = sum(1 for t in tasks if not t.get("he_thong_dung", "").strip())
today  = datetime.date.today().strftime("%d/%m/%Y")

# ── META: sửa nội dung ở đây khi thêm khối mới ────────────────────
META = {
    "blocks_todo": [
        "Corporate Actions",
        "Client Reporting",
        "Performance & Risk Management",
        "Compliance & Regulatory Reporting",
        "Data Management",
    ],
    "deep_dive_n": 10,
    "findings": [
        {"t": f"{n_uc} cơ hội ứng dụng AI trên {n_task} tác vụ vận hành có thật",
         "d": f"Mỗi tác vụ được bóc tách từ văn bản pháp luật, bản cáo bạch, mô tả công việc "
              f"hoặc quyết định xử phạt đã tải về và lưu lại. Không có tác vụ nào suy đoán."},
        {"t": f"{quick} use case thuộc nhóm làm được ngay",
         "d": "Chủ yếu là trích xuất dữ liệu từ chứng từ có cấu trúc cố định và sinh văn bản "
              "theo mẫu lặp lại — công nghệ đã trưởng thành, dữ liệu đầu vào sẵn có."},
        {"t": "Trích xuất chứng từ là nhóm cơ hội lớn nhất",
         "d": "Phần lớn điểm nghẽn nằm ở chỗ dữ liệu đến dưới dạng PDF, bản scan hoặc email "
              "rồi phải gõ tay vào hệ thống. Đây là nơi AI thay được nhiều thao tác nhất."},
        {"t": f"Chỉ {pain}/{n_task} tác vụ có điểm gãy đã xác minh",
         "d": "Tài liệu công khai mô tả nghĩa vụ phải làm, không mô tả chỗ làm khó. "
              f"{ask} tác vụ còn lại cần phỏng vấn người đang làm nghề để xác nhận."},
        {"t": f"{verif}/{n_uc} use case đạt mức đã kiểm chứng đầy đủ",
         "d": f"Thiếu hai dữ kiện: thời lượng thao tác (rỗng {no_dur}/{n_task} tác vụ) và "
              f"hệ thống đang dùng (rỗng {no_sys}/{n_task}). Chỉ phỏng vấn mới lấp được."},
    ],
    "limits": [
        f"<b>{verif}/{n_uc} use case đạt mức VERIFIED.</b> Toàn bộ còn lại ở mức CATALOGUE — "
        f"đủ để định hướng, chưa đủ để lập kế hoạch triển khai chi tiết.",
        f"<b>Nguyên nhân:</b> cột thời lượng thao tác rỗng {no_dur}/{n_task} tác vụ, cột hệ thống "
        f"đang dùng rỗng {no_sys}/{n_task}. Tài liệu công khai không chứa hai thông tin này.",
        f"<b>{pain}/{n_task} tác vụ có điểm gãy đã xác minh</b> từ quyết định xử phạt và tin báo chí. "
        f"{ask} tác vụ còn lại chưa có bằng chứng về khó khăn thực tế.",
        "<b>Chưa có tài liệu nào của Dragon Capital.</b> Nguồn hiện tại là bản cáo bạch Bảo Việt Fund, "
        "mô tả công việc của Bản Việt và HD Capital, quy chế VSDC và thông tư Bộ Tài chính. "
        "Quy trình tương đồng vì cùng chịu Thông tư 98/2020, nhưng không được hiểu là quy trình của Dragon Capital.",
        f"<b>Đã nghiên cứu {len(blocks)}/8 khối chức năng</b> của chuỗi giá trị vận hành quỹ. "
        "Năm khối còn lại chưa khảo sát.",
        "<b>Điểm số do người phân tích chấm thủ công</b> trên từng use case, không dùng quy tắc tự động. "
        "Cơ sở chấm điểm hiển thị trong hồ sơ từng use case.",
        f"<b>Ngày chốt dữ liệu: {today}.</b> Hiệu lực văn bản pháp luật được kiểm tại thời điểm thu thập; "
        "cần kiểm lại nếu dùng sau 6 tháng.",
    ],
    "next_step": "Một cuộc phỏng vấn 45 phút với chuyên viên vận hành quỹ sẽ lấp được cả hai cột "
                 f"đang trống và nâng phần lớn trong {n_uc} use case từ CATALOGUE lên VERIFIED. "
                 "Bộ câu hỏi đã soạn sẵn tại <code>09_roles_tasks/INTERVIEW_SHORTLIST.md</code> — "
                 f"32 câu, bám vào {ask} tác vụ cụ thể đang thiếu dữ kiện.",
}

def load_json(name):
    p = os.path.join(D, name)
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {}

META["roadmap"] = load_json("roadmap.json")
META["architecture"] = load_json("architecture.json")

with open(TPL, encoding="utf-8") as f:
    html = f.read()

repl = {
    "{{TITLE}}":  "Cơ hội ứng dụng AI trong vận hành quỹ đầu tư",
    "{{DEK}}":    f"Khảo sát {len(blocks)} khối chức năng tầng Back Office của công ty quản lý quỹ tại "
                  f"Việt Nam: {n_task} tác vụ vận hành được bóc tách từ nguồn sơ cấp, "
                  f"{n_uc} cơ hội ứng dụng AI được chấm điểm và xếp thứ tự ưu tiên.",
    "{{ORG}}":    "Sunext AI Lab",
    "{{VERSION}}": "v2.0",
    "{{BYLINE}}": f"Chốt dữ liệu {today}  ·  {n_task} tác vụ  ·  {n_uc} use case  ·  "
                  f"{len(sources)} nguồn  ·  {len(blocks)}/8 khối chức năng",
    "{{DD_N}}":   str(META["deep_dive_n"]),
}
for k, v in repl.items():
    html = html.replace(k, v)

def inject(html, marker, data):
    pat = re.compile(r"/\*__" + marker + r"__\*/.*?/\*__END__\*/", re.S)
    return pat.sub(lambda m: "/*__%s__*/%s/*__END__*/" % (marker, json.dumps(data, ensure_ascii=False)), html, count=1)

# Chuẩn hoá cột SOURCE_REGISTRY để khớp tên trường trong template JS
for s in sources:
    s["ten_tai_lieu"]  = s.get("tieu_de", "")
    s["to_chuc"]       = s.get("to_chuc_phat_hanh", "")
    s["ngay_lay"]      = s.get("ngay_truy_cap", "")
    s["note_chat_luong"] = s.get("ghi_chu", "")
    s["status"]        = s.get("trang_thai", "")

html = inject(html, "TASKS", tasks)
html = inject(html, "USECASES", usecases)
html = inject(html, "META", META)
html = inject(html, "SOURCES", sources)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Đã dựng: {OUT}")
print(f"  {n_task} tác vụ · {n_uc} use case · {len(blocks)} khối · {len(sources)} nguồn")
print(f"  Quick win {quick} · pain point {pain} · cần phỏng vấn {ask}")
