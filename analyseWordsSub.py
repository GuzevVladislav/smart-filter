import re
import time_1 

# Примерный список корней нецензурных слов на русском языке
bad_word_roots = [
    "бляд", "хуй", "пизд", "еб", "сука", "нахуй", "нахер","ебан", "ебаш", "ебнут", "муд", "пидор", "гандон","ахуе"
]


def analyse(tuple):
    def contains_profanity(text):
        # Создаем регулярное выражение из списка корней нецензурных слов
        pattern = re.compile(r'\b(' + '|'.join(bad_word_roots) + r')[\w]*\b', re.IGNORECASE)
        # Ищем совпадения в тексте
        if pattern.search(text):
            return True
        return False
        
    response = []
    for el in tuple:
        if contains_profanity(el["text"]):
            response.append([time_1.timeFormat(el['start']), "-", el["text"]])
    if response:
        return response, True
    return "d", False


