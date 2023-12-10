import re

# Function to find all words 'Poland' in the text
def find_poland(text):
    return re.findall(r'\bPoland\b', text)

# Function to find country names (Poland, Germany, and France)
def find_countries(text):
    return re.findall(r'\b(?:Poland|Germany|France)\b', text)

# Function to find punctuation marks (dots and commas)
def find_punctuation(text):
    return re.findall(r'[.,]', text)

# Function to find numbers representing a year (four-digit numbers)
def find_years(text):
    return re.findall(r'\b\d{4}\b', text)

# Function to find capital letters
def find_capital_letters(text):
    return re.findall(r'\b[A-Z]\b', text)

# Function to find vowels
def find_vowels(text):
    return re.findall(r'[aeiouAEIOU]', text)

# Function to find words with exactly five letters
def find_words_with_five_letters(text):
    return re.findall(r'\b\w{5}\b', text)

# Function to find words with at least five letters
def find_words_with_at_least_five_letters(text):
    return re.findall(r'\b\w{5,}\b', text)

# Function to find words starting with capital letters
def find_words_starting_with_capital(text):
    return re.findall(r'\b[A-Z]\w*\b', text)

# Open the 'hello.txt' file in read mode
with open('hello.txt', 'r') as file:
    # Read the content of the file
    file_content = file.read()

    # a. All words 'Poland'
    print("a. All words 'Poland':", find_poland(file_content))

    # b. Country names (Poland, Germany, and France)
    print("b. Country names:", find_countries(file_content))

    # c. Punctuation marks (dots and commas)
    print("c. Punctuation marks:", find_punctuation(file_content))

    # d. Numbers representing a year (four-digit numbers)
    print("d. Numbers representing a year:", find_years(file_content))

    # e. Capital letters
    print("e. Capital letters:", find_capital_letters(file_content))

    # f. Vowels
    print("f. Vowels:", find_vowels(file_content))

    # g. Words with exactly five letters
    print("g. Words with exactly five letters:", find_words_with_five_letters(file_content))

    # h. Words with at least five letters
    print("h. Words with at least five letters:", find_words_with_at_least_five_letters(file_content))

    # i. Words starting with capital letters
    print("i. Words starting with capital letters:", find_words_starting_with_capital(file_content))