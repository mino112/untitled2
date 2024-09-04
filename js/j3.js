// 목표를 선택하면 목표 세부사항을 보여줍니다.
function selectGoal(goal) {
  document.getElementById('selectedGoal').innerText = `내 목표는 ${goal}입니다.`;
  document.getElementById('goalDetails').style.display = 'block';
}

// ChatGPT에 목표를 보내는 함수
async function sendToChatGPT() {
  const message = document.getElementById('selfIntroduction').value;

  try {
    // 서버에 POST 요청을 보냅니다.
    const response = await fetch('/submit-goal', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ goal: message }),  // JSON 형식으로 데이터 전송
    });

    // 서버로부터 받은 응답을 JSON으로 파싱합니다.
    const data = await response.json();

    // ChatGPT의 응답을 화면에 표시합니다.
    document.getElementById('chatGPTResponse').innerText = `ChatGPT 응답: ${data.response}`;
  } catch (error) {
    console.error('오류가 발생했습니다:', error);
    document.getElementById('chatGPTResponse').innerText = '오류가 발생했습니다. 다시 시도해 주세요.';
  }
}

