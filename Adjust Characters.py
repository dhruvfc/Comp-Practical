def adjust_textfile(fname):
    limit = int(input("Enter character limit per line: "))
    try:
        with open(fname, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"{fname} not found. Creating it with sample content.")
        sample_text = [
            "This is a sample text file created because the file was not found.\n",
            "You can add your own lines, later if needed.\n"
            "Each line will be checked against the character limit.\n"
        ]
        with open(fname, "w") as f:
            f.writelines(sample_text)
        lines = sample_text
    adjusted_content = []
    for lcount, line in enumerate(lines, start=1):
        line = line.rstrip("\n")
        excess = max(0, len(line), limit)
        print(f"Line {lcount}: Excess characters = {excess}")
        for i in range(0, len(line), limit):
            adjusted_content.append(line[i:i+limit])
    print("\n\t Adjusted Content")
    for new_line in adjusted_content:
        print(new_line)
adjust_textfile("sample.txt")
