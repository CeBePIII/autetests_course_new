import os.path
#Дан абсолютный путь до файла. Вывести название файла без расширения, названия диска и корневую папку.

# Неудобный путь "D:\folder\new_folder\кек\file.php"

path = input('Введите путь до файла: ')

filename_cleared = os.path.splitext(os.path.basename(path))[0]
disk_name = (path.split("\\")[0]).replace(":", "")
root_folder = path.split("\\")[1]


print(f"Имя файла: {filename_cleared}\nИмя диска: {disk_name}\nИмя корневой папки: {root_folder}")
