from pathlib import Path
import json


def save_to_file(filepath, data):
    base_directory = Path(__file__).parent.parent
    full_path = base_directory / filepath

    full_path.parent.mkdir(parents=True, exist_ok=True)

    with full_path.open("w", encoding="utf-8") as file:
        if isinstance(data, (dict, list)):
            json.dump(data, file, ensure_ascii=False, indent=4)
        else:
            file.write(data)
    print(f"\n📜 The {Path(filepath).stem} file has been saved to {full_path.resolve()} 🪄")
