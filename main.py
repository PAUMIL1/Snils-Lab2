import sys
from Snils import (
    is_valid_snils_syntax,
    find_snils_in_text,
    find_snils_in_file,
    find_snils_in_url
)


def main():
    while True:
        print("\n=== Поиск и проверка СНИЛС ===")
        print("1. Проверить один СНИЛС / Найти СНИЛС в введенном тексте")
        print("2. Найти все СНИЛС в текстовом файле")
        print("3. Найти все СНИЛС на веб-странице по URL")
        print("0. Выход")

        choice = input("Выберите действие (0-3): ").strip()

        if choice == '1':
            user_input = input("Введите СНИЛС или текст для поиска: ")
            if is_valid_snils_syntax(user_input):
                print(f"[+] Строка '{user_input.strip()}' является синтаксически корректным СНИЛС.")
            else:
                found = find_snils_in_text(user_input)
                if found:
                    print(f"[+] Найдено СНИЛС в тексте ({len(found)} шт.): {', '.join(found)}")
                else:
                    print("[-] Синтаксически корректных СНИЛС не обнаружено.")

        elif choice == '2':
            filepath = input("Введите путь к файлу (например, sample.txt): ").strip()
            try:
                found = find_snils_in_file(filepath)
                if found:
                    print(f"[+] Найдено в файле ({len(found)} шт.):")
                    for item in found:
                        print(f"  - {item}")
                else:
                    print("[-] В файле СНИЛС не найдены.")
            except FileNotFoundError:
                print(f"[Ошибка] Файл '{filepath}' не найден.")
            except Exception as e:
                print(f"[Ошибка при чтении файла]: {e}")

        elif choice == '3':
            url = input("Введите URL страницы (с http:// или https://): ").strip()
            try:
                found = find_snils_in_url(url)
                if found:
                    print(f"[+] Найдено на странице ({len(found)} шт.):")
                    for item in set(found):
                        print(f"  - {item}")
                else:
                    print("[-] На странице СНИЛС не найдены.")
            except Exception as e:
                print(f"[Ошибка при загрузке URL]: {e}")

        elif choice == '0':
            print("Завершение работы.")
            sys.exit(0)
        else:
            print("[!] Неверный ввод, попробуйте снова.")


if __name__ == '__main__':
    main()