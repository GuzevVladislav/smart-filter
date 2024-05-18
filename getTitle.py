import requests
from bs4 import BeautifulSoup

def getTitle(video_url):
    def get_youtube_video_page(video_url):
        try:
            response = requests.get(video_url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Не удалось получить доступ к странице видео. Код ошибки: {response.status_code}")
                return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None

    def extract_metadata_from_page(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Извлечение названия видео
        title_element = soup.find('meta', {'name': 'title'})
        video_title = title_element['content'] if title_element else 'Название видео не найдено'
        # Извлечение описания видео
        description_element = soup.find('meta', {'name': 'description'})
        video_description = description_element['content'] if description_element else 'Описание видео не найдено'
        
        return video_title, video_description
    return extract_metadata_from_page(get_youtube_video_page(video_url))