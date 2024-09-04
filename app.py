from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# OpenAI API 키 설정
openai.api_key = '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'  # 실제 API 키로 교체하세요.

@app.route('/')
def index():
  return render_template('index.html')  # 메인 페이지 렌더링

@app.route('/2.html')
def prompt_select():
  return render_template('2.html')  # 프롬프트 선택 페이지 렌더링

@app.route('/3.html')
def student_page():
  return render_template('3.html')  # 학업에 어려움을 겪는 학생 페이지 렌더링

@app.route('/개발자.html')
def developer_page():
  return render_template('개발자.html')  # 개발자 페이지 렌더링

@app.route('/대학생.html')
def college_student_page():
  return render_template('대학생.html')  # 대학생 페이지 렌더링

@app.route('/아티스트.html')
def artist_page():
  return render_template('아티스트.html')  # 아티스트 페이지 렌더링

@app.route('/직장인.html')
def office_worker_page():
  return render_template('직장인.html')  # 직장인 페이지 렌더링

@app.route('/submit-goal', methods=['POST'])
def submit_goal():
  try:
    data = request.json
    user_goal = data.get('goal', '')

    if not user_goal:
      return jsonify({'error': 'No goal provided'}), 400  # 400 Bad Request

    # ChatGPT API에 요청을 보내는 부분
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=user_goal,
      max_tokens=150
    )

    # 응답 데이터 추출
    chatgpt_response = response.choices[0].text.strip()

    return jsonify({'response': chatgpt_response})
  except Exception as e:
    print(f"Error occurred: {e}")
    return jsonify({'error': 'An error occurred on the server.'}), 500  # 500 Internal Server Error

@app.route('/api/generate-prompt', methods=['POST'])
def generate_prompt():
  try:
    data = request.json
    prompt = data.get('prompt', '')

    if not prompt:
      return jsonify({'error': 'No prompt provided'}), 400  # 400 Bad Request

    # ChatGPT API에 요청을 보내는 부분
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=150
    )

    # 응답 데이터 추출
    chatgpt_response = response.choices[0].text.strip()

    return jsonify({'response': chatgpt_response})
  except Exception as e:
    print(f"Error occurred: {e}")
    return jsonify({'error': 'An error occurred on the server.'}), 500  # 500 Internal Server Error

if __name__ == '__main__':
  app.run(debug=True)
