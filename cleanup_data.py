from pathlib import Path
import sys

directory_to_clean = sys.argv[1]
json_lines = [path for path in Path(directory_to_clean).rglob('*.jsonl')]
paths_to_remove = [path for path in Path(directory_to_clean).rglob('*') if path not in json_lines]
for path in paths_to_remove:
    if path.is_file():
        path.unlink()