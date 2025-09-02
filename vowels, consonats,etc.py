def count_characters(filename):
    vowels = consonants = digits = spaces = special = 0
    try:
        with open(filename, "r") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"{filename} not found. Creating it with Sample Content.")
        sample_text = "This is a sample file with 2 lines. \nCheck vowels 123 and spaces!"
        with open(filename, "w") as f:
            f.write(sample_text)
        data = sample_text
    for ch in data:
        if ch.lower() in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1
        print(f"Number of vowels are {vowels}")
        print(f"Number of consonants are {consonants}")
        print(f"Number of digits are {digits}")
        print(f"Number of spaces are {spaces}")
        print(f"Number of special characters are {special}")
count_characters("sample.txt")
        
