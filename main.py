import argparse
from scripts import json_to_md, repo_scraper, save_to_file, start_loading_animation
from utils import (
    allowed_file_extensions,
    excluded_folders,
    allowed_filenames,
)

try:
    loading_spinner = start_loading_animation("🔮 Inscribing data to the arcane JSON scroll and casting spells to convert JSON to MD... 🌟📜🔮🧙‍♂️")
    parser = argparse.ArgumentParser(description="Repository Scraper Tool")
    parser.add_argument("--owner", type=str, help="Owner of the repository", required=True)
    parser.add_argument("--repo", type=str, help="Name of the repository", required=True)
    parser.add_argument("--branch", type=str, help="Branch to scrape", default="main")
    parser.add_argument(
        "--generate-readme", action="store_true", help="Generate a README.md file"
    )
    args = parser.parse_args()

    scraper = repo_scraper(
        args.owner,
        args.repo,
        args.branch,
        allowed_file_extensions,
        excluded_folders,
        allowed_filenames,
    )

    repository_data = scraper.scrape_repository()

    filename_json = f"{args.owner}-{args.repo}_tree.json"
    json_filepath = f"data/results_json/{filename_json}"

    loading_spinner.stop()

    save_to_file(json_filepath, repository_data)

    if args.generate_readme:
        filename_readme = f"{args.owner}-{args.repo}.md"
        output_dir = f"data/results_md/{filename_readme}"
        json_to_md(json_filepath, output_dir)

    else:
        print("No README.md file will be generated.")

except Exception as e:
    print(f"An magical error occurred: {str(e)}")
