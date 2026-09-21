import string


OUTPUT_FILE = "fileAnalysis.txt"


def read_words(filename):
    """Read a text file and return cleaned, lowercase words."""
    with open(filename, "r") as file:
        words = file.read().lower().split()

    return [word.strip(string.punctuation) for word in words if word.strip(string.punctuation)]


def write_list_to_file(filename, data):
    """Write each item in a list to a separate line."""
    with open(filename, "w") as file:
        for item in data:
            file.write(str(item) + "\n")


def unique_words(words):
    """Return unique words while preserving their original order."""
    unique = []

    for word in words:
        if word not in unique:
            unique.append(word)

    return unique


def common_words(list1, list2):
    """Return words that appear in both lists."""
    common = []

    for word in list1:
        if word in list2 and word not in common:
            common.append(word)

    return common


def words_in_one_not_in_other(list1, list2):
    """Return words found in the first list but not the second."""
    return [word for word in list1 if word not in list2]


def word_frequency(words):
    """Create a dictionary containing the frequency of each word."""
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def print_word_frequency(words):
    frequency = word_frequency(words)

    print("Word\tCount")
    print("-" * 24)

    for word, count in sorted(frequency.items()):
        print(f"{word}\t{count}")


def analyze_files(file1, file2):
    words1 = read_words(file1)
    words2 = read_words(file2)

    unique1 = unique_words(words1)
    unique2 = unique_words(words2)

    union = unique1 + [word for word in unique2 if word not in unique1]
    common = common_words(unique1, unique2)
    diff1 = words_in_one_not_in_other(unique1, unique2)
    diff2 = words_in_one_not_in_other(unique2, unique1)
    symmetric_diff = diff1 + diff2

    report = [
        "Unique words in file 1:",
        *unique1,
        "",
        "Unique words in file 2:",
        *unique2,
        "",
        "Words found in either file:",
        *union,
        "",
        "Words in both files:",
        *common,
        "",
        "Words only in file 1:",
        *diff1,
        "",
        "Words only in file 2:",
        *diff2,
        "",
        "Words in either file but not both:",
        *symmetric_diff,
    ]

    write_list_to_file(OUTPUT_FILE, report)

    print("\nFrequency table for file 1:")
    print_word_frequency(words1)

    print("\nFrequency table for file 2:")
    print_word_frequency(words2)

    print(f"\nAnalysis saved to {OUTPUT_FILE}.")


def main():
    print("Text File Analyzer")
    file1 = input("Enter the name of the first input file: ").strip()
    file2 = input("Enter the name of the second input file: ").strip()

    try:
        analyze_files(file1, file2)
    except FileNotFoundError as error:
        print(f"File not found: {error.filename}")
    except OSError as error:
        print(f"Unable to read or write a file: {error}")


if __name__ == "__main__":
    main()
