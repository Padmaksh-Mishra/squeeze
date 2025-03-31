# Squeeze

Squeeze is a free and open source application that merges all code files from a GitHub repository into a single, human-readable file. Each file’s content is prefixed with its relative path, and it supports probabilistically skipping lines to reduce output size for LLM processing.

## Features

- **Repository Merging:** Clones a GitHub repository and stitches together all code files.
- **File Tagging:** Each file is prefixed with its relative path.
- **Probabilistic Line Skipping:** Reduce text length by skipping lines based on a configurable probability.
- **Code-Only Mode:** Use the `--code-only` flag to include only recognized code files (e.g., `.py`, `.java`, `.cpp`, etc.), filtering out non-code and auto-generated files.
- **FOSS:** This project is free and open source. Contributions and ideas are welcome!

## How to Use

1. **Install Dependencies**

   Make sure you have Python installed (tested with Python 3.11). Install required dependencies:

       pip install -r requirements.txt

2. **Run the Application**

   The entry point is in `src/main.py`. To merge files from a repository, run:

       python -m src.main <repository_url> <skip_probability (0-1000)> [--code-only]

   - Replace `<repository_url>` with the URL of the GitHub repository.
   - `<skip_probability>` is an integer from 0 to 1000; for instance, 10 means approximately 10 out of 1000 lines will be skipped.
   - Add the `--code-only` flag to process only recognized code file types and skip non-code files.

3. **Output**

   The merged content is saved to `merged_output.txt` in the project root.

## Contributing

This project is FOSS and welcomes your contributions!

- **Share Your Ideas:** Whether it's a bug fix, new feature, or performance improvement, we invite you to share your ideas.
- **Open Issues & Pull Requests:** Feel free to open issues or submit pull requests.
- **Community Discussions:** Join our discussions to help shape the future of Squeeze.


## Contact

For ideas, questions, or feedback, please open an issue or reach out via our repository discussions.

Happy coding!