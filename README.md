## Text Cleaning Script
This script is designed to clean text data from multiple .txt files located in a specified directory. The cleaned text is then saved to a new directory. The script performs the following operations on the text:

1. Removes extra spaces and newline characters.
2. Converts text to lowercase.
3. Removes punctuation.
4. Tokenizes the text.
5. Removes English stopwords.
# Requirements
Python 3.x
NLTK library
# Installation
Before running the script, ensure you have the required libraries installed. You can install NLTK using pip:

| Package | Command |
|---------|---------|
| NLTK    | `pip install nltk` |

# Notes
The script processes each file line by line, so it is suitable for large files.
The cleaned text is saved in the same filename as the original but in a different directory (cleaned_data).
# License
This project is licensed under the MIT License - see the LICENSE file for details.
