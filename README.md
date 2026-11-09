# Text File Analyzer

A simple command-line Python tool that analyzes a text file and reports basic statistics: word count, sentence count, and the 10 most frequent words.

## Features

- Reads any UTF-8 text file (works with English and Persian text)
- Strips punctuation and normalizes text to lowercase
- Counts total words and sentences
- Shows the top 10 most frequent words
- Handles missing files gracefully

## Requirements

- Python 3.8+
- No external libraries (uses only the standard library)

## Usage

```bash
python text_analyzer.py
```

When prompted, enter the path to your text file:
You can try the included `sample.txt`.

```
Enter file path: sample.txt
```

## Example Output

```
Enter file path: sample.txt
Number of words : 135
Number of sentences : 10
Top 10 Most Frequent Words:
the : 15
is : 7
a : 5
data : 5
model : 4
and : 4
of : 3
by : 3
step : 3
learning : 2
```

## How It Works

The code is split into small, single-purpose functions:

| Function | Purpose |
|---|---|
| `read_file()` | Reads the file with UTF-8 encoding |
| `list_words()` | Removes punctuation (regex), lowercases, splits into words |
| `count_sentences()` | Splits on `. ! ? ؟` and counts non-empty parts |
| `show_top_words()` | Counts frequencies with a dictionary and prints the top 10 |

## Known Limitations

- Sentence detection is simple: abbreviations like "Dr." or decimal numbers may be counted as sentence endings.
- No stop-word filtering, so common words ("the", "و", "که") appear at the top.

## Author

Ayda Karimzadeh

- GitHub: [Ayda-Karimzadeh](https://github.com/Ayda-Karimzadeh)
- LinkedIn: [ayda-karimzadeh](https://linkedin.com/in/ayda-karimzadeh)