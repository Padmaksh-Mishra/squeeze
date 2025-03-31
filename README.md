# Repo Merger

## Overview
Repo Merger is a Python application designed to merge all files from a specified GitHub repository into a single file. This is particularly useful for processing code with language models, as it provides context by including the relative paths of each file.

## Features
- Merges all files from a GitHub repository into one file.
- Includes the relative path of each file at the beginning of its content.
- Implements a probability meter to skip lines, reducing the overall length of the merged file.

## Installation
To get started with Repo Merger, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd repo-merger
pip install -r requirements.txt
```

## Usage
To run the application, execute the following command:

```bash
python src/main.py <github-repo-url>
```

Replace `<github-repo-url>` with the URL of the GitHub repository you wish to merge.

## Functionality
- **Fetching Repository Files**: The application fetches the list of files from the specified GitHub repository.
- **Merging Files**: It merges the contents of all files, prepending each file's relative path.
- **Probability Meter**: The application can skip lines based on a specified probability to manage the size of the output.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.# squeeze
