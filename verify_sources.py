import csv

source_registry = '_data/SOURCE_REGISTRY.csv'
task_registry = '_data/task_registry.csv'
usecase_registry = '_data/usecase_registry.csv'

def get_valid_sources():
    valid = set()
    with open(source_registry, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row:
                valid.add(row[0].strip())
    return valid

valid_sources = get_valid_sources()
missing = set()

def check_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        if 'source_ids' in header:
            source_idx = header.index('source_ids')
        else:
            print(f"source_ids column not found in {filepath}")
            return
            
        for i, row in enumerate(reader):
            if len(row) > source_idx:
                cell = row[source_idx]
                if cell:
                    ids = [x.strip() for x in cell.replace(';', ',').split(',')]
                    for id in ids:
                        if id and id not in valid_sources:
                            missing.add((id, filepath, i+2))

check_csv(task_registry)
check_csv(usecase_registry)

print("Danh sách các source_id lạc (không có trong SOURCE_REGISTRY):")
if not missing:
    print("[] (Rỗng - Tất cả đều tồn tại)")
else:
    for m in missing:
        print(f" - {m[0]} (tại {m[1]} dòng {m[2]})")
