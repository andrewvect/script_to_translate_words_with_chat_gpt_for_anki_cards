Script that translate words with chatGpt and create 3 sentences with it.
It's can be cosy when you need to create anki cards with words.

Usage:
1. add your ChatGpt api key in file .env
2. add file words.txt in main directory
You can update promt in file src/services/PromtCreator.py
3. run script python main.py

get your translated words with sentences in json format in main directory
translated_words.json

if word didn't translated or there was error while process it will be in file
not_translated_words.json
