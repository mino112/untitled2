function generatePrompt() {
  const context = document.getElementById('context').value;
  const purpose = document.getElementById('purpose').value;
  let prompt = '';

  if (context === '') {
    prompt = '먼저 프롬프트에 사용할 맥락을 입력하세요.';
  } else {
    switch(purpose) {
      case 'info':
        prompt = `다음과 같은 정보를 제공해주세요: ${context}`;
        break;
      case 'inquiry':
        prompt = `다음 상황에 대해 질문을 해보세요: ${context}`;
        break;
      case 'feedback':
        prompt = `다음에 대한 피드백을 제공해주세요: ${context}`;
        break;
      default:
        prompt = '프롬프트를 생성할 수 없습니다. 다시 시도해주세요.';
    }
  }

  document.getElementById('generatedPrompt').innerText = prompt;

  // 생성된 프롬프트를 서버에 전송하여 ChatGPT 응답 받기 (선택 사항)
  if (prompt !== '') {
    sendPromptToServer(prompt);
  }
}

// 서버로 생성된 프롬프트를 보내는 함수
async function sendPromptToServer(prompt) {
  try {
    const response = await fetch('/api/generate-prompt', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt: prompt }),
    });

    const data = await response.json();
    document.getElementById('chatGPTResponse').innerText = `ChatGPT 응답: ${data.response}`;
  } catch (error) {
    console.error('오류가 발생했습니다:', error);
    document.getElementById('chatGPTResponse').innerText = '오류가 발생했습니다. 다시 시도해 주세요.';
  }
}

