import json


class JsonFile:
    """
    Class for working with json files
    """
    @staticmethod
    def load(filename):
        with open(filename, 'r') as file:
            return json.load(file)

    @staticmethod
    def create_file(filename):
        with open(filename, 'w') as file:
            json.dump({}, file, ensure_ascii=False)

    @staticmethod
    def load_word_translated_to_file( filename: str, word: dict) -> None:
        with open(filename, 'r') as file:
            data = json.load(file)
            data[word['id']] = word
        with open(filename, 'w') as file:
            json.dump(data, file, ensure_ascii=False)

    @staticmethod
    def load_not_translated_word(filename: str, word: dict) -> None:
        with open(filename, 'r') as file:
            data = json.load(file)
            data[list(word.keys())[0]] = list(word.values())[0]
        with open(filename, 'w') as file:
            json.dump(data, file, ensure_ascii=False)
