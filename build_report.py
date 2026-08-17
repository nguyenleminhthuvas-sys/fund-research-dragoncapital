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
DD   = os.path.join(BASE, "12_deep_dives")
# Hai file output phải luôn giống hệt nhau — build ghi ra cả hai để không còn
# lệch bản giữa index.html (dùng để serve) và FINAL_REPORT.html (bản giao nộp).
OUTS = [os.path.join(BASE, "12_report", "index.html"),
        os.path.join(BASE, "12_report", "FINAL_REPORT.html")]
TPL  = os.path.join(BASE, "report_template.html")

# 8 khối chức năng chuẩn của chuỗi giá trị vận hành quỹ (xem 00_control/SCHEMAS.md).
# blocks_todo được suy ra động = ALL_BLOCKS trừ các khối đã có trong task_registry.csv,
# KHÔNG hard-code nữa — trước đây "Performance & Risk Management" bị liệt kê nhầm vào
# cả "đã nghiên cứu" lẫn "chưa nghiên cứu" cùng lúc vì danh sách todo hard-code không
# được cập nhật khi khối Risk được bổ sung.
ALL_BLOCKS = [
    "NAV & Fund Accounting",
    "Reconciliation & Settlement",
    "Transfer Agency & Nhà đầu tư",
    "Performance & Risk Management",
    "Corporate Actions",
    "Client Reporting",
    "Compliance & Regulatory Reporting",
    "Data Management",
]

def read(p):
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f))

tasks    = read(os.path.join(D, "task_registry.csv"))
usecases = read(os.path.join(D, "usecase_registry.csv"))
try:
    sources = read(os.path.join(D, "SOURCE_REGISTRY.csv"))
except FileNotFoundError:
    sources = []

# 8 tác vụ có trong 09_roles_tasks/INTERVIEW_SHORTLIST.md — cập nhật danh sách này nếu
# shortlist đổi. Dùng để tính đúng số UC mà bộ câu hỏi phỏng vấn 45 phút thực sự phủ được,
# thay vì tuyên bố chung chung "phần lớn use case" (bản cũ overclaim: shortlist chỉ nhắm
# khối NAV nên chỉ verify được một phần nhỏ trong tổng số UC).
INTERVIEW_SHORTLIST_TASKS = {
    "T-BO-001", "T-BO-002", "T-BO-004", "T-BO-006",
    "T-BO-007", "T-BO-008", "T-BO-018", "T-BO-030",
}

n_task = len(tasks)
n_uc   = len(usecases)
blocks = sorted({t["khoi_chuc_nang"] for t in tasks})
pain   = sum(1 for t in tasks if t.get("diem_gay_pain_point", "").strip())
ask    = sum(1 for t in tasks if t.get("can_phong_van", "").strip().upper() == "Y")
quick  = sum(1 for u in usecases if u.get("ro") == "Quick win")
verif  = sum(1 for u in usecases if u.get("muc_do") == "VERIFIED")
no_dur = sum(1 for t in tasks if not t.get("thoi_luong_uoc_tinh_phut", "").strip())
no_sys = sum(1 for t in tasks if not t.get("he_thong_dung", "").strip())
shortlist_uc = sorted({u["uc_id"] for u in usecases if u.get("task_id") in INTERVIEW_SHORTLIST_TASKS})
today  = datetime.date.today().strftime("%d/%m/%Y")

# Deep dive .md có sẵn trong 12_deep_dives/ (dùng để Phần 08 biết UC nào đã có
# hồ sơ chi tiết và UC nào trong top điểm số hiện tại còn thiếu, thay vì âm thầm
# bỏ qua toàn bộ thư mục này như bản build trước).
deep_dive_files = sorted(
    m.group(1) for f in os.listdir(DD) if f.endswith(".md")
    for m in [re.match(r"(UC-\d+)\.md$", f)] if m
) if os.path.isdir(DD) else []

blocks_todo = [b for b in ALL_BLOCKS if b not in blocks]

# ── META: sửa nội dung ở đây khi thêm khối mới ────────────────────
META = {
    "blocks_todo": blocks_todo,
    "deep_dive_n": 10,
    "deep_dive_files": deep_dive_files,
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
        f"{len(blocks_todo)} khối còn lại chưa khảo sát: {', '.join(blocks_todo)}.",
        "<b>Điểm số do người phân tích chấm thủ công</b> trên từng use case, không dùng quy tắc tự động. "
        "Cơ sở chấm điểm hiển thị trong hồ sơ từng use case.",
        f"<b>Ngày chốt dữ liệu: {today}.</b> Hiệu lực văn bản pháp luật được kiểm tại thời điểm thu thập; "
        "cần kiểm lại nếu dùng sau 6 tháng.",
    ],
    "next_step": "Một cuộc phỏng vấn 45 phút với chuyên viên vận hành quỹ khối NAV sẽ lấp được cả hai cột "
                 f"đang trống cho 8 tác vụ cốt lõi, đủ nâng <b>{len(shortlist_uc)}/{n_uc} use case</b> "
                 f"({', '.join(shortlist_uc)}) từ CATALOGUE lên VERIFIED — không phải phần lớn {n_uc} UC. "
                 "Bộ câu hỏi đã soạn sẵn tại <code>09_roles_tasks/INTERVIEW_SHORTLIST.md</code> — "
                 f"32 câu, bám vào {ask} tác vụ cụ thể đang thiếu dữ kiện, nhưng shortlist hiện chỉ phủ khối "
                 "NAV &amp; Fund Accounting. Cần thêm bộ câu hỏi tương tự cho Settlement / Transfer Agency / "
                 "Risk để verify được phần còn lại.",
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
    "{{VERSION}}": "v2.2",
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

for out in OUTS:
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

print(f"Đã dựng: {', '.join(OUTS)}")
print(f"  {n_task} tác vụ · {n_uc} use case · {len(blocks)} khối · {len(sources)} nguồn")
print(f"  Quick win {quick} · pain point {pain} · cần phỏng vấn {ask}")
print(f"  blocks_todo: {META['blocks_todo']}")
print(f"  deep_dive_files: {deep_dive_files}")
