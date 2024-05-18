from flask import Flask, request, jsonify, send_from_directory
import getTitle 
import getSubtitles
import analyseWordsTitle
import analyseWordsSub

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/data', methods=['POST'])
def handle_data():
    data = request.json
    print(f"Received data: {data}")
    temp =  getTitle.getTitle(data['link'])
    temp1 = getSubtitles.getSub(data['link'])
    str = "".join(temp)
    resp1 = analyseWordsTitle.analyse(str)
        

    resp2, ans = analyseWordsSub.analyse(temp1)
    
    if (ans):
        response = {"response": resp2, "status": True, "non-lexicon":True}
        return jsonify(response)
    response = {"response":resp1, "status": False, "non-lexicon":False}
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=8000)