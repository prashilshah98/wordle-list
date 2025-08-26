# wordle-list

This repository contains:

- **A text file of 5-letter words** (one word per line)  
- **A Python script to validate these words** using the [Free Dictionary API](https://dictionaryapi.dev/).  

The goal is to maintain a clean, valid list of English 5-letter words, which can be useful for:
- Wordle clones
- Word games
- Natural language projects  

---

## 📂 Repository Contents

- `words.txt` → Original list of 5-letter words  
- `validate_words.py` → Python script to check the validity of words and filter valid ones into a new file  

---

## ✅ Features

✔ Checks if each word:
- Exists in English (via dictionary API)
- Is valid (has definitions)
- Is 5 letters long  

✔ Outputs:
- `valid_words.txt` → All valid English 5-letter words  
- Optionally, log invalid words for review  

---

## ▶ Usage

### 1. Use the raw word list directly  
You can download or reference the raw list of words here:  
https://raw.githubusercontent.com/prashilshah98/wordle-list/refs/heads/main/words.txt

### 2. Validate the word list with Python
Clone the repo and run the validator:

`git clone https://github.com/prashilshah98/wordle-list.git`
`cd wordle-list`

## Install dependencies:
`pip install requests`

## Run the validator:
`python validate_words.py words.txt valid_words.txt --delay 0.5`

words.txt → input file (one word per line)
valid_words.txt → output file for valid words
--delay → optional delay in seconds between API calls (default 0.5)

### API Used:
https://dictionaryapi.dev/
