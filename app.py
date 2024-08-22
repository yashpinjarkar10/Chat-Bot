from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')
    chatbot_response = generate_chatbot_response(user_input)
    return jsonify({'response': chatbot_response})

