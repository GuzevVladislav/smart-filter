from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_string(input_str):
    match = re.search(r'(?<=watch\?v=).*?(?=_channel|$)', input_str)
    if match:
        return match.group(0)
    else:
        return None
def get_transcript(video_id, language='ru'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        return transcript
    except Exception as e:
        print(f"Не удалось получить субтитры: {e}")
        return None
    
def getSub(videoUrl):
    video_id = extract_string(videoUrl)
    return get_transcript(video_id)