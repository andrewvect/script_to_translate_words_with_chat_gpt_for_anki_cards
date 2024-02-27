from unittest import TestCase
from ..services.JsonHandler import JsonFile

class TestJsonFile(TestCase):

    def test_can_upload_translated_word_into_file(self):
        file = JsonFile()
        file.create_file("test_file.json")

        dictionary = {'id': 2, 'serbian_word': 'mislili', 'russian_word': 'думали', 'examples': [
            {'serbian': 'Oni su mislili da je to istina.', 'russian': 'Они думали, что это правда.'}]}

        dictionary2 = {'id': 4, 'serbian_word': 'išao', 'russian_word': 'шёл',
                       'examples': [{'serbian': 'Ja sam išao u prodavnicu.', 'russian': 'Я пошел в магазин.'}]}

        file.load_word_translated_to_file("test_file.json", dictionary)
        file.load_word_translated_to_file("test_file.json", dictionary2)

        self.assertEqual(file.load("test_file.json"), {"2": dictionary, "4": dictionary2})

        # Clean up
        import os
        os.remove("test_file.json")


    def test_can_upload_not_translated_word_into_file(self):
        file = JsonFile()
        file.create_file("test_file.json")

        dictionary = {'2': 'mislili'}

        dictionary2 = {'4': 'išao'}

        file.load_not_translated_word("test_file.json", dictionary)
        file.load_not_translated_word("test_file.json", dictionary2)

        self.assertEqual(file.load("test_file.json"), {"2": 'mislili', "4": 'išao'})

        # Clean up
        import os
        os.remove("test_file.json")
