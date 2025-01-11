"""
## Краткое содержание
В данном задании вы разработаете класс `TxtFileHandler` для работы с текстовыми файлами. Этот класс должен предоставлять методы для чтения, записи и добавления данных в TXT файлы.

### Технологии: 🦾
- Python
- ООП (Объектно-Ориентированное Программирование)
- Работа с файлами
- `with` statement
- Аннотация типов

## Задание 👷‍♂️

### Классы и их функциональность

1.  **TxtFileHandler**
    *   Методы:
        *   `read_file(filepath: str) -> str`: Метод для чтения данных из TXT файла. Метод должен открывать файл по указанному пути, считывать все его содержимое и возвращать в виде строки.
        *   `write_file(filepath: str, *data: str) -> None`: Метод для записи данных в TXT файл. Метод должен открывать файл по указанному пути в режиме записи (`"w"`) и записывать переданную строку(ки) `data` в файл. Если файл существует, он должен быть перезаписан.
        *   `append_file(filepath: str, *data: str) -> None`: Метод для дописывания данных в TXT файл. Метод должен открывать файл по указанному пути в режиме добавления (`"a"`) и добавлять переданную строку(ки) `data` в конец файла.
    *   **Обработка ошибок:**
        *   Метод `read_file` должен корректно обрабатывать ситуацию, когда файл не существует. В таком случае, он должен возвращать пустую строку (`""`).
        *   Все методы должны корректно обрабатывать исключения, которые могут возникнуть при работе с файлами (например, `FileNotFoundError`, `PermissionError`).

"""


# class TxtFileHandler:
#     """
#     Класс для работы с TXT документами.
#     Может читать, писать и добавлять записи в существующие документы
#     """

#     @staticmethod
#     def read_file(filepath: str, encoding="utf-8") -> str:
#         """
#         Метод который позволяет читать TXT документы
#         :param filepath: принемает путь к файлу
#         :return: возвращает строку содержимое файла
#         """
#         with open(filepath, "r", encoding=encoding) as file:
#             data = file.read()

#         return data

#     @staticmethod
#     def write_file(filepath: str, *data: str, encoding="utf-8") -> None:
#         """
#         Метод который пишет в файл с флагом W - перезапись
#         :param filepath: принемает путь к файлу
#         """
#         with open(filepath, "w", encoding=encoding) as file:
#             for line in data:
#                 file.write(line + "\n")

#     @staticmethod
#     def append_file(filepath: str, *data: str, encoding="utf-8") -> None:
#         """
#         Метод который пишет в файл с флагом A - добавить в конец файла
#         :param filepath: принемает путь к файлу
#         """
#         with open(filepath, "a", encoding=encoding) as file:
#             for line in data:
#                 file.write(line + "\n")


# file_path = "lesson_16/text.txt"
# txt_handler = TxtFileHandler()

# txt_handler.write_file(file_path, "Привет", "Мир!")


class TxtFileHandler:
    """
    Класс для работы с TXT документами.
    Может читать, писать и добавлять записи в существующие документы
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_file(self, encoding="utf-8") -> str | None:
        """
        Метод который позволяет читать TXT документы
        :param filepath: принимает путь к файлу
        :return: возвращает строку содержимого файла или None в случае ошибки
        """
        try:
            with open(self.file_path, "r", encoding=encoding) as file:
                data = file.read()
            return data
        
        except FileNotFoundError:
            print(f"Ошибка: Файл '{self.file_path}' не найден.")
            return None
        
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return None

    def write_file(self, *data: str, encoding="utf-8") -> None:
        """
        Метод который пишет в файл с флагом W - перезапись
        :param filepath: принимает путь к файлу
        """
        try:
            with open(self.file_path, "w", encoding=encoding) as file:
                for line in data:
                    file.write(line + "\n")
        
        except Exception as e:
            print(f"Произошла ошибка при записи в файл: {e}")

    def append_file(self, *data: str, encoding="utf-8") -> None:
        """
        Метод который пишет в файл с флагом A - добавить в конец файла
        :param filepath: принимает путь к файлу
        """
        try:
            with open(self.file_path, "a", encoding=encoding) as file:
                for line in data:
                    file.write(line + "\n")
        except Exception as e:
            print(f"Произошла ошибка при добавлении в файл: {e}")



file_path = "lesson_16/text.txt"
txt_handler = TxtFileHandler(file_path)

txt_handler.append_file("Ещё", "Строки")