import os
import time

# Укажите директорию, которую хотите обойти
directory = (os.getcwd())

# Обход каталога
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        # Формируем полный путь к файлу
        file_path = os.path.join(dirpath, filename)

        # Получаем время последнего изменения файла
        mtime = os.path.getmtime(file_path)
        mtime_readable = time.ctime(mtime)  # Преобразуем в читаемый формат

        # Получаем размер файла
        size = os.path.getsize(file_path)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(file_path)

        # Выводим информацию о файле
        print(f"Файл: {file_path}")
        print(f"  Родительская директория: {parent_dir}")
        print(f"  Последнее изменение: {mtime_readable}")
        print(f"  Размер: {size} байт")
        print("-" * 40)
