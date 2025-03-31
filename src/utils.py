import os
import tempfile
import subprocess
import random

def is_text_file(file_path: str, blocksize: int = 1024) -> bool:
    """
    Heuristically determines if a file is text (human-readable) by scanning its first block
    for null bytes.
    """
    try:
        with open(file_path, 'rb') as file:
            chunk = file.read(blocksize)
            return b'\0' not in chunk
    except Exception:
        return False

def fetch_repository_files(repo_url: str, code_only: bool = False):
    # Clone the repository into a temporary directory
    temp_dir = tempfile.mkdtemp()
    subprocess.run(
        ["git", "clone", repo_url, temp_dir],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    # Define keywords to skip auto-generated files
    skip_keywords = ['readme', 'gradle', 'package']

    # Allowed code file extensions (lowercase)
    allowed_extensions = {
        '.py', '.java', '.js', '.jsx', '.ts', '.tsx',
        '.cpp', '.c', '.h', '.hpp', '.cs', '.go',
        '.rb', '.php', '.swift', '.kt', '.kts', '.scala',
        '.rs', '.pl'
    }

    files = []
    for root, dirs, filenames in os.walk(temp_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        for f in filenames:
            lower_name = f.lower()
            # Skip files if any skip keyword is found.
            if any(keyword in lower_name for keyword in skip_keywords):
                continue
            # If filtering to code-only files, check extension.
            if code_only:
                ext = os.path.splitext(f)[1].lower()
                if ext not in allowed_extensions:
                    continue
            file_path = os.path.join(root, f)
            if is_text_file(file_path):
                files.append(file_path)
    return files

def skip_lines(lines: list, probability: float):
    # Returns a new list of lines with some lines skipped based on the given probability.
    return [line for i, line in enumerate(lines) if random.random() > probability]