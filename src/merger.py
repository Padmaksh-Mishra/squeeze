import os
from .utils import fetch_repository_files, skip_lines

class Merger:
    def __init__(self, repo_url: str):
        self.repo_url = repo_url

    def merge_files(self, probability: float = 0.0, code_only: bool = False) -> str:
        """
        Merges all files from the repository into a single string.
        Each file's content is prefixed with its relative path.
        Lines are probabilistically skipped based on the provided probability.

        :param probability: Probability of skipping a line (e.g., 0.01 skips ~1 in 100 lines).
        :param code_only: If True, only include files with recognized code extensions.
        :return: Merged file content as a string.
        """
        files = fetch_repository_files(self.repo_url, code_only=code_only)
        merged_content = []

        for file_path in files:
            # Convert to a relative path if needed
            relative_path = os.path.relpath(file_path)
            merged_content.append(f"{relative_path}\n")
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                lines = file.readlines()
                if probability > 0:
                    lines = skip_lines(lines, probability)
                merged_content.extend(lines)
        return ''.join(merged_content)