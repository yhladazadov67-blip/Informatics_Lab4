# File: Informatics_Lab3_Task1.py
# Author = Азадов Ыхлас
# Group = 3132
# Date = 12.12.2025

"""
Вариант 0 (ИСУ % 7 = 0).
Проверка, является ли строка хайку.
Разделитель строк — символ '/'.
Количество слогов считаем равным количеству гласных.
"""

import re

VOWELS_RE = re.compile(r"[аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY]")

def count_vowels(line: str) -> int:
    return len(VOWELS_RE.findall(line))

def is_haiku(text: str) -> str:
    parts = [p.strip() for p in text.split('/')]
    if len(parts) != 3:
        return "Не хайку. Должно быть 3 строки."

    counts = [count_vowels(p) for p in parts]
    if counts == [5, 7, 5]:
        return "Хайку!"
    return "Не хайку."

# Минимум 5 тестов
TESTS = [
    ("Вечер за окном. / Еще один день прожит. / Жизнь скоротечна...", "Хайку!"),
    ("Просто текст", "Не хайку. Должно быть 3 строки."),
    ("Как вишня расцвела! / Она с коня согнала / И князя-гордеца.", "Не хайку."),
    ("а е и о у / а е и о у ы э / а е и о у", "Хайку!"),
    ("один / два / три / четыре", "Не хайку. Должно быть 3 строки."),
]

if __name__ == "__main__":
    s = input().strip()
    print(is_haiku(s))