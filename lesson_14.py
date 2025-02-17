"""
Урок 14
16.12.2024

Python: Разбор HW. Модули, импорты и работа с файлами. Урок: 14

1. Разбор домашнего задания: +
    - Проверка функционального погодного приложения
    - Особенности упаковки в exe через PyInstaller

2. Модульная система Python: +
    - Создание и импорт модулей
    - Конструкция if __name__ == '__main__'
    - Относительные и абсолютные импорты
    - Пакеты и подмодули

3. Работа с текстовыми файлами:
    - Открытие и закрытие файлов
    - Контекстный менеджер with
    - Методы чтения и записи
    - Режимы работы с файлами (r, w, a)

4. Работа с JSON:
    - Сериализация и десериализация
    - Методы dumps() и loads()
    - Запись и чтение JSON файлов
    - Практические примеры работы с JSON

Практика:
- Создание модульной структуры проекта
- Реализация записи логов в txt файл
- Сохранение настроек приложения в JSON
- Работа с конфигурационными файлами
"""

# Работа с TXT документами
"""
Флаги открытия файла:
r - read открытие файла только для чтения - откроет файл если файл существует и упадет с ошибкой если файла нет
w - write открытие файла только для записи - создат файл если его нет, перезапишет полностью файл если он есть
a - append открытие файла для добавления данных в конец файла - создат файл если его нет, дозаписывает в конец файла
b - binary открытие файла в двоичном режиме
+
"""
# Путь к файлу относительно корня проекта
txt_file = "lesson_14.txt"

# Открытие файла для дозаписи
# file = open(txt_file, "a", encoding="utf-8")

# Запись в файл
# file.write("Hello world!\n")

# Закрытие файла
# file.close()

# Открытие файла для чтения
# file = open(txt_file, "r", encoding="utf-8")

# Получаем спиоск строк
# lines = file.readlines()

# Распчатаем
# print(lines)

# Получить одну строку
# line = file.readline()
# print(line.strip())

# line = file.readline()
# print(line, end="")

# line = file.readline()
# print(line)

# Закрытие файла
# file.close()


# Контекстный менеджер with

with open(txt_file, "r", encoding="utf-8") as file:
    # Получить список строк
    lines = file.readlines()


print(lines)

# PRACTICE - функция для записи/дозаписи в txt файл
"""
Напишите функцию
def write_to_file(file_name: str, *data: str, mode: str = "a", encoding: str = "utf-8") -> None:
    ...

которая принимает название файла, данные для записи и режим работы с файлом.

data - коллеция строк, которые нужно записать в файл
Пишите это в цикле for line in data:
"""


def write_to_file(file_name: str, *data: str, 
                  mode: str = "a", encoding: str = "utf-8") -> None:
    """
    Записывает данные в txt файл либо в режиме дозаписи, либо в режиме перезаписи

    :param file_name: str - название файла
    :param data: str - данные для записи
    :param mode: str - режим работы с файлом
    :param encoding: str - кодировка файла
    :return: None
    """
    
    with open(file_name, mode, encoding=encoding) as file:
        for line in data:
            file.write(line + "\n")


data = ["Шёл Никифор", "через реку", "видит в реке рак"]

write_to_file("lesson_14.txt", *data)
