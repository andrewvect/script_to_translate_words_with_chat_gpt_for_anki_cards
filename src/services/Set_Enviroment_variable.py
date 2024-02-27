import os

from dotenv import dotenv_values


def set_openai_api_key_to_environment():
    env_vars = dotenv_values(".env")
    if "OPENAI_API_KEY" not in env_vars:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    os.environ["OPENAI_API_KEY"] = env_vars["OPENAI_API_KEY"]

