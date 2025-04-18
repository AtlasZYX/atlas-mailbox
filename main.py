from flask import Flask, request, jsonify

app = Flask(__name__)
lesson_queue = []

@app.route('/')
def home():
    return "Atlas Mailbox Online"

@app.route('/inbox', methods=['POST'])
def receive_lesson():
    data = request.get_json()
    if data:
        lesson_queue.append(data)
        return jsonify({"message": "Lesson received"}), 200
    return jsonify({"error": "Invalid data"}), 400

@app.route('/inbox', methods=['GET'])
def send_lesson():
    if lesson_queue:
        return jsonify(lesson_queue.pop(0)), 200
    return jsonify({"message": "No lessons"}), 204

if __name__ == '__main__':
    app.run()
