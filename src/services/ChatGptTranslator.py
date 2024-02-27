import asyncio
import json

from openai import AsyncOpenAI

from script_to_translate_words_with_chat_gpt_for_anki_cards.src.services.JsonHandler import JsonFile
from script_to_translate_words_with_chat_gpt_for_anki_cards.src.services.PromtCreator import Prompt
from script_to_translate_words_with_chat_gpt_for_anki_cards.src.services.logger import logger


class ChatGptTranslator:
    """
    Class for translating words using chat gpt
    """
    count = 0
    file_with_translated_words = "translated_words.json"
    file_with_not_translated_words = "not_translated_words.json"

    def __init__(self, chat_gpt_client: AsyncOpenAI, file_with_words, chunk_size=100, native_language="russian",
                 foreign_language="serbian"):
        self.chat_gpt_client = chat_gpt_client
        self.file_with_words = file_with_words
        self.words = []
        self.json_file = JsonFile()
        self.prompt = Prompt(native_language, foreign_language)
        self.chunk_size = chunk_size

    async def run_script(self):
        self._load_words()
        self.json_file.create_file(self.file_with_translated_words)
        self.json_file.create_file(self.file_with_not_translated_words)
        await self._handle_words()

    def _load_words(self):
        with open(self.file_with_words, 'r') as file:
            self.words = file.readlines()

    async def _handle_words(self):
        split_list = [self.words[i:i + self.chunk_size] for i in range(0, len(self.words), self.chunk_size)]
        for chunk_words in split_list:
            tasks = []
            for word in chunk_words:
                task = asyncio.create_task(self._request_to_chat_gpt_to_translate_word(word))
                tasks.append(task)
            await asyncio.gather(*tasks)

    async def _request_to_chat_gpt_to_translate_word(self, word: str) -> None:

        chat_completion = await self.chat_gpt_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": self.prompt.add_word_in_prompt(word),
                }
            ],
            model="gpt-3.5-turbo",
            response_format={"type": "json_object"},
            timeout=20000
        )

        message = dict(chat_completion.choices[0].message)
        self._handle_response(message['content'], word)

    def _handle_response(self, response: str, word: str) -> None:
        try:
            parsed_content = self._parse_content_from_response(json.loads(response))
            self.count += 1
            print(f"Word {self.count} had been translated successfully.")
            self.json_file.load_word_translated_to_file(self.file_with_translated_words, parsed_content)

        except Exception as e:
            logger.error(f"Error while parsing content for word {word}. Error: {e}, response from open ai: {response}")
            self.json_file.load_not_translated_word(self.file_with_not_translated_words, {self.count: word[:-2]})
            self.count += 1

    def _parse_content_from_response(self, content: dict) -> dict:
        return {"id": self.count, "content": content}
