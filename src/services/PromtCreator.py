class Prompt:
    """
    Class for creating prompt for chat gpt
    """
    prompt = ""

    def __init__(self, native_language: str, foreign_language):
        self.native_language = native_language
        self.foreign_language = foreign_language

    def add_word_in_prompt(self, word: str):
        self.prompt = f"""
        
        i want to learn new {self.foreign_language} words, translate the {self.foreign_language} word in curly brackets into {self.native_language}
        language, create 3 sentences with this word and translate it into {self.native_language}.
        
        {word}
        
        i want to get the answer in json format like this:
        {{
        "word": "",
            "translation": "",
            "examples usage in sentenses": [
            {{sentence: "", translation: ""}},
            {{sentence: "", translation: ""}},
            {{sentence: "", translation: ""}},
                
            ]
        }}
        """
        return self.prompt
