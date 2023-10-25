
from flask import Flask, request, jsonify
from new_service_recommendation import lottoSocialUserDataAi, prompt, humanMessage

app = Flask(__name__)

@app.post('/')
def endpoint():
    response = lottoSocialUserDataAi(prompt, humanMessage)
    print(response)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
