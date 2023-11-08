import json
from pathlib import Path
from scripts.save_to_file  import save_to_file


def json_to_md(json_filename, output_filename):
    with open(json_filename, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    md_content = f"\n# {Path(json_filename).stem} Project Content\n\n## This content was extracted with ❤️ by GitRepoScraper\n\n"

    for item in json_data["tree"]:
        md_content += f"### {item['path']}\n\n"
        if "content" in item and item["content"]:
            md_content += (
                f"```{item['path'].split('.')[-1]}\n{item['content']}\n```\n\n"
            )
        else:
            md_content += "No content available.\n\n"

    save_to_file(output_filename, md_content)
