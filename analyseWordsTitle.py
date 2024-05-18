import re

bad_word_roots = [
    "бляд", "хуй", "пизд", "еб", "сука", "нахуй", "нахер","ебан", "ебаш", "ебнут", "муд", "пидор", "гандон","ахуе", 
    "террор", "националист","нациист","национализм", "национализм","игил", "драка", "смерть", "убийство", "тупиц", "придурки", "придурок", "дурак"
]


def contains_profanity(text = "Павел Воля, Илья Соболев. Россия23', 'Телеграм Россия23: https://t.me/vesti23rossiaВконтакте Россия23: https://vk.com/rossia23Ютуб Шоу Воли: @volyashow https://youtube.com/@UCk43FGJ4ITSs9cUvjCpu1..."):
    # Создаем регулярное выражение из списка корней нецензурных слов
    pattern = re.compile(r'\b(' + '|'.join(bad_word_roots) + r')[\w]*\b', re.IGNORECASE)
    # Ищем совпадения в тексте
    if pattern.search(text):
        return True
    return False




    