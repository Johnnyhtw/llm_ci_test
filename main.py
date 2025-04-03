import os
import requests
from openai import OpenAI
from datetime import datetime

# 參數設定
OPENROUTER_API_KEY = "請填入OpenRouter API金鑰"  # 請填入OpenRouter API金鑰
LLM_MODULE = "deepseek/deepseek-chat-v3-0324:free" # 請填入LLM名稱，e.g.：meta-llama/llama-3.3-70b-instruct:free、qwen/qwen-2.5-72b-instruct:free
MD_FULL_PATH = "./2024魔球比賽紀錄.md" # 請填入md檔路徑+檔名


# 驗證API金鑰有效性
def verify_api_key(api_key):
    try:
        response = requests.get(
            "https://openrouter.ai/api/v1/auth/key",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        if response.status_code == 200:
            return True, "API密鑰驗證成功"
        return False, f"驗證失敗: {response.json().get('error', {}).get('message', '未知錯誤')}"
    except Exception as e:
        return False, f"驗證異常: {str(e)}"

# 初始化客戶端並驗證
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

is_valid, message = verify_api_key(OPENROUTER_API_KEY)
if not is_valid:
    print(f"錯誤: {message}")
    exit(1)
print(f"狀態: {message}")

# 讀取MD檔案內容
with open(MD_FULL_PATH, "r", encoding="utf-8") as f:
    md_content = f.read()

# 顯示基本資訊
file_size = os.path.getsize(MD_FULL_PATH) / 1024
print(f"已載入：{os.path.basename(MD_FULL_PATH)} ({datetime.fromtimestamp(os.path.getmtime(MD_FULL_PATH)).strftime('%Y-%m-%d %H:%M:%S')} | {file_size:.1f}KB)")
print("輸入問題（按q退出）")

# 初始化對話歷史
conversation_history = [
    {"role": "system", "content": f"根據以下比賽紀錄回答問題：\n{md_content}"}
]

# 主迴圈
while True:
    question = input("> ")
    if question.lower() == "q":
        break
    
    try:
        # 新增使用者問題到歷史
        conversation_history.append({"role": "user", "content": question})
        
        # 呼叫OpenRouter API
        response = client.chat.completions.create(
            model=LLM_MODULE,
            messages=conversation_history
        )
        
        # 新增LLM回答到歷史並顯示
        answer = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": answer})
        print(f"[{response.model}] {answer}\n")
        
    except Exception as e:
        print(f"錯誤：{str(e)}")

print("測試結束")
