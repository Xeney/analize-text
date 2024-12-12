import unittest
from prettytable import PrettyTable
from analize_text import AnalizeText

class TestAnalizeText(unittest.TestCase):

    def setUp(self):
        self.text = "На свете много чудес,\nи они могут происходить на каждом шагу."
        self.analyzer = AnalizeText(self.text)

    def test_characters_count(self):
        expected_count = len(self.text)
        self.assertEqual(self.analyzer.characters_count, expected_count)

    def test_words_count(self):
        expected_count = len(self.text.split())
        self.assertEqual(self.analyzer.words_count, expected_count)

    def test_lines_count(self):
        expected_count = self.text.count('\n') + 1  # +1 для последней строки
        self.assertEqual(self.analyzer.lines_count, expected_count)

    def test_letter_frequency(self):
        expected_frequency = {}
        for char in self.text.lower():
            if char.isalpha():
                expected_frequency[char] = expected_frequency.get(char, 0) + 1

        self.assertEqual(self.analyzer.letter_frequency, expected_frequency)

    def test_table_output(self):
        # Тестирование вывода в таблице - можно проверить, что таблица правильно создается
        # Обратите внимание, что здесь мы просто проверяем, создается ли таблица
        table = PrettyTable()
        table.field_names = ["Буква", "Частота"]
        
        for letter, freq in self.analyzer.letter_frequency.items():
            table.add_row([letter, freq])

        self.assertTrue(isinstance(table, PrettyTable))  # Проверка, что объект таблицы создан
        self.assertGreater(len(table.rows), 0)  # Проверка, что в таблице есть строки

if __name__ == "__main__":
    unittest.main()
