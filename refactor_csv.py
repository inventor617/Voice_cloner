import csv
import re
import os
import time
import wave

#удаление файлов длительностью больше 10 секунд
folder_path = r"C:\Users\inven\ru_RU\by_book\male\nikolaev\argentinetz\wavs"
deleted_files = []

for filename in os.listdir(folder_path):
    if not filename.endswith(".wav"):
        continue

    file_path = os.path.join(folder_path, filename)
    with wave.open(file_path, "r") as wave_file:
        duration = wave_file.getnframes() / wave_file.getframerate()
    if duration > 10:
        print(file_path)
        os.remove(file_path)
        deleted_files.append(filename)


with open("deleted_files.txt", "w") as file:
    file.write("\n".join(deleted_files))

# Считываем имена удаленных файлов из файла и удаляем расширение
def read_del():
    with open('deleted_files.txt', 'r') as f:
        deleted_files = [line.strip() for line in f.readlines()]
        for num,line in enumerate(deleted_files):
            line = line.replace('.wav','')
            deleted_files[num] =line
    return deleted_files

deleted_files = read_del()

# Открываем исходный файл CSV для чтения
with open(r'C:\Users\inven\ru_RU\by_book\male\nikolaev\argentinetz\metadata.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='|')
    rows = [row for row in reader if row[0] not in deleted_files]
    #print(rows)
    #print(len(rows))

for j in range(len(rows)):
    for i in range(len(rows[j])):
        rows[j][i] = re.sub(r'[^\w\s.\?\-]', '', rows[j][i])
        rows[j][i] = re.sub(r'\s{2,}', ' ', rows[j][i])
        if i/2==1:
            rows[j][i]= rows[j][i] + ';;;'
print(rows)

# Перезаписываем исходный файл CSV без удаленных строк
with open('LJ/transcript.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerows(rows)
