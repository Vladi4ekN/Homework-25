import os
import time


directory = (os.getcwd())

for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:

        file_path = os.path.join(dirpath, filename)

        mtime = os.path.getmtime(file_path)
        mtime_readable = time.ctime(mtime)

        size = os.path.getsize(file_path)

        parent_dir = os.path.dirname(file_path)

        print(f"Файл: {file_path}")
        print(f"  Родительская директория: {parent_dir}")
        print(f"  Последнее изменение: {mtime_readable}")
        print(f"  Размер: {size} байт")
        print("-" * 40)
