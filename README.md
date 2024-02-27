Script that translate words with chatGpt and create 3 sentences with it.
It's can be cosy when you need to create anki cards with words.

you will get translated words in json format like this

```json
{
  "0": {
    "id": 0,
    "content": {
      "word": "",
      "translation": "",
      "examples usage in sentenses": [
        {
          "sentence": "",
          "translation": ""
        },
        {
          "sentence": "",
          "translation": ""
        },
        {
          "sentence": "",
          "translation": ""
        }
      ]
    }
  },
}
```

Usage:
1. add your ChatGpt api key in file .env as OPENAI_API_KEY
2. add file words.txt with words (each word in new line) in main directory
3. run script python main.py

get your translated words with sentences in json format in main directory
translated_words.json

if word didn't translated or there was error while process, it will be in file
not_translated_words.json
