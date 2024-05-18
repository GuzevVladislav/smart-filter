import re

# Примерный список корней нецензурных слов на русском языке
bad_word_roots = [
    "бляд", "хуй", "пизд", "еб", "сука", "нахуй", "нахер","ебан", "ебаш", "ебнут", "муд", "пидор", "гандон","ахуе"
]

def analyse(text):
    def contains_profanity(text):
        # Создаем регулярное выражение из списка корней нецензурных слов
        pattern = re.compile(r'\b(' + '|'.join(bad_word_roots) + r')[\w]*\b', re.IGNORECASE)
        
        # Ищем совпадения в тексте
        if pattern.search(text):
            return True
        return False


    if contains_profanity(text):
        return("Видео содержит нецензурные слова")
    else:
        return("Видео не содержит нецензурных слов")