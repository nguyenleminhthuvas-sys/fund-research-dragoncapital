import csv
import os

mappings = {
    'S-DOC-BVFED': 'S-BVFED-001',
    'S-REG-TT98': 'S-TT98-001',
    'S-ENF-AMBER': 'S-ENF-006',
    'S-ENF-TCTC': 'S-ENF-006',
    'S-REG-TT99': 'S-REG-003',
    'S-ENF-120KL': 'S-ENF-007'
}

def fix_file(filepath, source_col_idx):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for i, row in enumerate(rows):
        if i == 0:
            continue # skip header
        if len(row) > source_col_idx:
            # The source column can contain multiple comma-separated IDs
            sources = [s.strip() for s in row[source_col_idx].split(',') if s.strip()]
            new_sources = []
            for s in sources:
                if s in mappings:
                    new_sources.append(mappings[s])
                else:
                    new_sources.append(s)
            # Deduplicate while preserving order
            seen = set()
            dedup_sources = [x for x in new_sources if not (x in seen or seen.add(x))]
            row[source_col_idx] = ','.join(dedup_sources)
            
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

print("Fixing task_registry.csv...")
fix_file('_data/task_registry.csv', 19)

print("Fixing usecase_registry.csv...")
fix_file('_data/usecase_registry.csv', 14)

print("Verifying all source_ids in task_registry and usecase_registry exist in SOURCE_REGISTRY.csv...")

with open('_data/SOURCE_REGISTRY.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    valid_sources = set(row[0] for row in reader)

missing = set()

def check_file(filepath, source_col_idx):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        for i, row in enumerate(rows):
            if i == 0: continue
            if len(row) > source_col_idx:
                sources = [s.strip() for s in row[source_col_idx].split(',') if s.strip()]
                for s in sources:
                    if s not in valid_sources:
                        missing.add(s)

check_file('_data/task_registry.csv', 19)
check_file('_data/usecase_registry.csv', 14)

print("Missing source_ids:")
if missing:
    for m in missing:
        print(f"- {m}")
else:
    print("Empty (None missing!)")
