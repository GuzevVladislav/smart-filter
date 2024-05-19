from flask import Flask, request, send_from_directory
import getTitle 
import getSubtitles
import analyseWordsTitle
import analyseWordsSub
from flask import jsonify
import classif

app = Flask(__name__)

@app.route('/')
def serve_index():  
    return send_from_directory('.', 'index.html')

@app.route('/api/data', methods=['POST'])
def handle_data():
    data = request.json
    if (data['age']):
        temp =  getTitle.getTitle(data['link'])
        temp1 = getSubtitles.getSub(data['link'])

        
        str = "".join(temp)
        resp1 = analyseWordsTitle.contains_profanity(str)
            
        if (resp1):
            response = {"response": "Название или описание содержит неприемлемый контент", "status": True, "non-lexicon": True}
            return jsonify(response)
        
        resp2, ans = analyseWordsSub.analyse(temp1)
        
        if (ans):
            response = {"response": resp2, "status": False, "non-lexicon":True}
            return jsonify(response)
        response = {"response": "Видео не содержит негативного контента", "status": False, "non-lexicon":False}
        return jsonify(response)
    else:
        show = classif.analyse(data['link'])
        if show:
            response = {"response": "Видео не содержит ненормативной лексики", "video": "видео содержит сцены курения", "status": False, "non-lexicon":False}
        else:
            response = {"response": "Видео не содержит ненормативной лексики", "video": "видео не содержит сцены курения", "status": False, "non-lexicon":False}
        return jsonify(response)

    

if __name__ == "__main__":
    app.run(port=8000)