#Формируем формат времени час:мин:сек из секунд
import math
def timeFormat(time):
    seconds =  math.floor(time % 60)
    minute = math.floor(((time -seconds) / 60)%60)
    hours = math.floor((time - seconds - minute) / 3600)
    return (f"{hours}:{minute}:{seconds}")
