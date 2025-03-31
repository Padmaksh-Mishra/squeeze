def main():
    import sys
    # Accept an optional flag "--code-only"
    argv = sys.argv[1:]
    if len(argv) not in [2, 3]:
        print("Usage: python -m src.main <github_repository_url> <skip_probability (1-1000)> [--code-only]")
        sys.exit(1)

    repo_url = argv[0]

    try:
        prob_value = int(argv[1])
    except ValueError:
        print("The skip probability must be an integer between 0 and 1000.")
        sys.exit(1)

    if not (0 <= prob_value <= 1000):
        print("The skip probability must be an integer between 0 and 1000.")
        sys.exit(1)

    # Convert the integer to a probability value.
    skip_probability = prob_value / 1000

    # Check if the optional '--code-only' flag is provided.
    code_only = (len(argv) == 3 and argv[2] == "--code-only")

    from src.merger import Merger
    merger = Merger(repo_url)
    merged_content = merger.merge_files(probability=skip_probability, code_only=code_only)

    output_file = "merged_output.txt"
    with open(output_file, "w") as f:
        f.write(merged_content)

    print(f"Merged content written to {output_file}")

if __name__ == "__main__":
    main()