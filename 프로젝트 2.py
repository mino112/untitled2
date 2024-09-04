from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, this is a Flask app!'

@app.route('/submit-goal', methods=['POST'])
def submit_goal():
  data = request.get_json()
  goal = data.get('goal', '')

  # 여기에 ChatGPT와의 상호작용 코드를 추가할 수 있습니다.
  # 예를 들어, OpenAI API를 호출하여 답변을 얻는 방식으로 구현할 수 있습니다.
  response = f"Your goal: {goal} has been received!"

  return jsonify({'response': response})

if __name__ == '__main__':
  app.run(debug=True)

