import asyncio
import os

from openai import AsyncOpenAI

from script_to_translate_words_with_chat_gpt_for_anki_cards.src.services.ChatGptTranslator import ChatGptTranslator
from script_to_translate_words_with_chat_gpt_for_anki_cards.src.services.Set_Enviroment_variable import \
    set_openai_api_key_to_environment

if __name__ == '__main__':
    set_openai_api_key_to_environment()
    client = AsyncOpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    translator = ChatGptTranslator(client, "words.txt")

    asyncio.run(translator.run_script())
