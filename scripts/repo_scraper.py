import requests
import json
import os


class repo_scraper:
    def __init__(
        self,
        owner,
        repo,
        branch="main",
        allowed_file_extensions=None,
        excluded_folders=None,
        allowed_filenames=None,
    ):
        self.owner = owner
        self.repo = repo
        self.branch = branch
        self.api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=*"
        self.raw_base_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}"
        self.allowed_file_extensions = allowed_file_extensions or []
        self.excluded_folders = excluded_folders or []
        self.allowed_filenames = allowed_filenames or []

    def scrape(self):
        response = requests.get(self.api_url)
        response.raise_for_status()
        data = response.json()

        for item in data["tree"]:
            if item["type"] == "blob" and self.is_valid_file(item["path"]):
                raw_url = self.convert_to_raw_url(item["url"], item["path"])
                item["content"] = self.fetch_file_content(raw_url)

        return data

    def is_valid_file(self, file_path):
        for excluded_folder in self.excluded_folders:
            if f"/{excluded_folder}/" in file_path or file_path.startswith(f"{excluded_folder}/"):
                return False

        if os.path.basename(file_path) in self.allowed_filenames:
            return True

        file_extension = os.path.splitext(file_path)[1]
        return file_extension in self.allowed_file_extensions


    def convert_to_raw_url(self, api_url, file_path):
        return f"{self.raw_base_url}/{file_path}"

    def fetch_file_content(self, raw_url):
        try:
            content_response = requests.get(raw_url)
            content_response.raise_for_status()
            return content_response.text
        except requests.HTTPError as e:
            print(f"Failed to fetch {raw_url}: {e}")
            return "Error fetching content."

    def scrape_repository(self):
        data = self.scrape()
        return data
