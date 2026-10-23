import re
import requests

# Регулярное выражение для поиска синтаксически корректного СНИЛС в тексте
SNILS_REGEX = r'\b\d{3}-\d{3}-\d{3}[ -]\d{2}\b'

# Регулярное выражение для строгой проверки всей строки целиком
SNILS_FULL_REGEX = r'^\d{3}-\d{3}-\d{3}[ -]\d{2}$'


def is_valid_snils_syntax(snils_str: str) -> bool:
    """Проверяет, является ли переданная строка синтаксически корректным СНИЛС."""
    if not isinstance(snils_str, str):
        return False
    return bool(re.fullmatch(SNILS_FULL_REGEX, snils_str.strip()))


def find_snils_in_text(text: str) -> list[str]:
    """Находит все синтаксически корректные СНИЛС в произвольном тексте."""
    if not isinstance(text, str):
        return []
    return re.findall(SNILS_REGEX, text)


def find_snils_in_file(filepath: str) -> list[str]:
    """Ищет СНИЛС в локальном текстовом файле."""
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return find_snils_in_text(content)


def find_snils_in_url(url: str, timeout: int = 10) -> list[str]:
    """Загружает веб-страницу по URL и ищет на ней СНИЛС."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return find_snils_in_text(response.text)