import re
import time_1 

# Примерный список корней слов 
bad_word_roots = [
    "бля", "хуй", "пизд", "еб", "сука", "нахуй", "нахер","ебан", "ебаш", "ебнут", "муд", "пидор", "гандон","ахуе", 
    "террор", "националист","нациист","национализм", "национализм","игил", "драка", "смерть", "убийство", "тупиц", "придурки", "придурок", "дурак"
]
def contains_profanity(text):
        # Создаем регулярное выражение из списка корней нецензурных слов
        pattern = re.compile(r'\b(' + '|'.join(bad_word_roots) + r')[\w]*\b', re.IGNORECASE)
        # Ищем совпадения в тексте

        if pattern.search(text):
            
            return True
        return False

def analyse(tuple):
    response = []
    for el in tuple:
        if contains_profanity(el["text"]):
            pattern = re.compile(r'\b(' + '|'.join(bad_word_roots) + r')[\w]*\b', re.IGNORECASE)
            text = re.sub(pattern, "***", el["text"])
            response.append([time_1.timeFormat(el['start']), "-", text])
    if response:
        return response, True
    return "d", False