import codecs
import unicodedata
import os
import re
import csv
from transliterate import translit

vocab = "PE абвгдеёжзийклмнопрстуфхцчшщъыьэюя.-?"
strings = 'Он замахнулся. Не надо заорал Жора. Я всё скажу Не трогайте её'
data = r"C:\Users\inven\Voice_cloner-myChanges\LJ"
#print(codecs.decode(vocab))
def load_vocab():
    char2idx = {char: idx for idx, char in enumerate(vocab)}
    idx2char = {idx: char for idx, char in enumerate(vocab)}
    print('char2idx',char2idx)
    print('idx2char',idx2char)
    return char2idx, idx2char
#for lette in strings:
    #print(unicodedata.name(lette))
    #print(unicodedata.name(lette))

def text_normalize(vocab):
    text = ''.join(char for char in unicodedata.normalize('NFC', vocab)
                   if unicodedata.category(char) != 'Mn')# Strip accents

    text = text.lower()
    text = re.sub("[^{}]".format(vocab), " ", text)
    text = re.sub("[ ]+", " ", text)
    print('text',text)
    return text
#text_normalize(vocab)

with open(r'C:\Users\inven\ru_RU\by_book\male\nikolaev\argentinetz\metadata.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='|')
    rows = [row for row in reader]
    #print(reader)
    for i in range(len(rows)):
        #print(rows[i])
        for j in range(len(rows[i])):
            if j==0: continue
            else: print(translit(rows[i][j],reversed=True))

    #translit(row, reversed=True)
    #print(len(rows))
