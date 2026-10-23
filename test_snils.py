import unittest
import os
from unittest.mock import patch, MagicMock
from Snils import (
    is_valid_snils_syntax,
    find_snils_in_text,
    find_snils_in_file,
    find_snils_in_url
)


class TestSnilsRegex(unittest.TestCase):

    def test_valid_snils_standard(self):
        """Проверка стандартного формата XXX-XXX-XXX YY"""
        self.assertTrue(is_valid_snils_syntax("112-233-445 95"))
        self.assertTrue(is_valid_snils_syntax("000-000-000 00"))
        self.assertTrue(is_valid_snils_syntax("999-888-777 66"))

    def test_valid_snils_hyphen_separator(self):
        """Проверка допустимого формата с дефисом перед контрольным числом"""
        self.assertTrue(is_valid_snils_syntax("112-233-445-95"))

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

    def test_find_snils_in_file(self):
        """Проверка чтения и поиска из временного тестового файла"""
        temp_filename = "temp_test_snils.txt"
        with open(temp_filename, "w", encoding="utf-8") as f:
            f.write("Документ №1. СНИЛС сотрудника: 555-666-777 88.\nКонец документа.")
        try:
            result = find_snils_in_file(temp_filename)
            self.assertEqual(result, ["555-666-777 88"])
        finally:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

    @patch('Snils.requests.get')
    def test_find_snils_in_url(self, mock_get):
        """Проверка поиска по веб-странице с имитацией HTTP-ответа"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Тестовый СНИЛС: 321-654-987 00</body></html>"
        mock_get.return_value = mock_response

        result = find_snils_in_url("https://example.com/snils")
        self.assertEqual(result, ["321-654-987 00"])


if __name__ == '__main__':
    unittest.main()