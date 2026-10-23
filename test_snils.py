import unittest
from Snils import is_valid_snils_syntax, find_snils_in_text


class TestSnilsRegex(unittest.TestCase):

    def test_valid_snils_standard(self):
        """Проверка стандартного формата XXX-XXX-XXX YY"""
        sample_1 = "112-233-445 95"
        sample_2 = "000-000-000 00"
        sample_3 = "999-888-777 66"
        self.assertTrue(is_valid_snils_syntax(sample_1))
        self.assertTrue(is_valid_snils_syntax(sample_2))
        self.assertTrue(is_valid_snils_syntax(sample_3))

    def test_valid_snils_hyphen_separator(self):
        """Проверка допустимого формата с дефисом перед контрольным числом"""
        sample_hyphen = "112-233-445-95"
        self.assertTrue(is_valid_snils_syntax(sample_hyphen))

    def test_invalid_snils_wrong_digit_count(self):
        """Неверное количество цифр в блоках"""
        self.assertFalse(is_valid_snils_syntax("12-233-445 95"))
        self.assertFalse(is_valid_snils_syntax("1122-233-445 95"))
        self.assertFalse(is_valid_snils_syntax("112-233-445 9"))
        self.assertFalse(is_valid_snils_syntax("112-233-445 955"))

    def test_invalid_snils_wrong_separators(self):
        """Неверные разделители"""
        self.assertFalse(is_valid_snils_syntax("11223344595"))
        self.assertFalse(is_valid_snils_syntax("112.233.445 95"))
        self.assertFalse(is_valid_snils_syntax("112/233/445 95"))
        self.assertFalse(is_valid_snils_syntax("112-233-445_95"))

    def test_invalid_snils_letters_and_types(self):
        """Наличие букв, пустых строк или некорректных типов данных"""
        self.assertFalse(is_valid_snils_syntax("112-233-44A 95"))
        self.assertFalse(is_valid_snils_syntax(""))
        self.assertFalse(is_valid_snils_syntax(None))

    def test_find_snils_in_text(self):
        """Поиск нескольких СНИЛС в тексте"""
        text = "Данные: 112-233-445 95 и 123-456-789-01. Ошибка: 1112-233-445 95."
        expected = ["112-233-445 95", "123-456-789-01"]
        self.assertEqual(find_snils_in_text(text), expected)


if __name__ == '__main__':
    unittest.main()