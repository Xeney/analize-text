from prettytable import PrettyTable

class AnalizeText():

    def __init__(self, text:str):
        self.text = text
        self.characters_count = len(text)
        self.words_count = len(text.split())
        self.lines_count = text.count('\n') + 1
        self.letter_frequency = {}

        for char in self.text.lower():
            if char.isalpha():
                self.letter_frequency[char] = self.letter_frequency.get(char, 0) + 1

    def table_output(self):
        table = PrettyTable()
        table.field_names = ["Буква", "Частота"]
        print(f"\nКоличество символов: {self.characters_count}")
        print(f"Количество слов: {self.words_count}")
        print(f"Количество строк: {self.lines_count}")
        
        for letter, freq in self.letter_frequency.items():
            table.add_row([letter, freq])
        
        print("\nЧастота букв:\n")
        print(table)

    
