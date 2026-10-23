import re
import requests

# Предварительно скомпилированные регулярные выражения для поиска и валидации СНИЛС
SNILS_REGEX = re.compile(r'\b\d{3}-\d{3}-\d{3}[ -]\d{2}\b')
SNILS_FULL_REGEX = re.compile(r'^\d{3}-\d{3}-\d{3}[ -]\d{2}$')

DEFAULT_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}


def is_valid_snils_syntax(snils_str: str) -> bool:
    """Проверяет, является ли переданная строка синтаксически корректным СНИЛС."""
    if not isinstance(snils_str, str):
        return False
    return bool(SNILS_FULL_REGEX.fullmatch(snils_str.strip()))


def find_snils_in_text(text: str) -> list[str]:
    """Находит все синтаксически корректные СНИЛС в произвольном тексте."""
    if not isinstance(text, str):
        return []
    return SNILS_REGEX.findall(text)


def find_snils_in_file(filepath: str) -> list[str]:
    """Ищет СНИЛС в локальном текстовом файле."""
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return find_snils_in_text(content)


def find_snils_in_url(url: str, timeout: int = 10) -> list[str]:
    """Загружает веб-страницу по URL и ищет на ней СНИЛС."""
    response = requests.get(url, headers=DEFAULT_HEADERS, timeout=timeout)
    response.raise_for_status()
    return find_snils_in_text(response.text)