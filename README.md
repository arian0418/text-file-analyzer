# Text File Analyzer

A Python command-line program that compares two text files and analyzes the words they contain.

## Features

- Reads and cleans words from two text files
- Converts words to lowercase and removes surrounding punctuation
- Finds unique words in each file
- Finds words shared by both files
- Finds words that appear in only one file
- Creates a combined list of words from both files
- Calculates word-frequency tables
- Writes comparison results to `fileAnalysis.txt`
- Handles missing input files

## Technologies

- Python 3
- File I/O
- Lists and dictionaries
- Python `string` module

## How to Run

1. Clone or download this repository.
2. Place two text files in the project folder.
3. Open a terminal in the project folder.
4. Run:

```bash
python text_file_analyzer.py
```

5. Enter the names of the two files when prompted.

## Example

```text
Text File Analyzer
Enter the name of the first input file: file1.txt
Enter the name of the second input file: file2.txt

Frequency table for file 1:
Word    Count
------------------------
hello   2
world   1
```

After the analysis is complete, detailed comparison results are saved in `fileAnalysis.txt`.

## Project Structure

```text
text-file-analyzer/
├── text_file_analyzer.py
├── README.md
└── .gitignore
```

## About

This project demonstrates Python fundamentals including file processing, functions, lists, dictionaries, loops, string manipulation, word-frequency counting, and comparison of data from multiple files.
