# LLM上下文注入能力測試

  這是一個基於 OpenRouter API 的 LLM 問答系統，目的是為了測試各LLM上下文注入的問題解析能力，程式預設會載入一份依據2024年世界棒球12強賽為基礎來編造的「2024魔球比賽紀錄.md」用來測試LLM，會把棒球改成"魔球"是為了避免LLM可能有學習過當時的比賽資訊，而導致LLM用自身所學的資訊來回覆。

## 功能特色
- 透過 OpenRouter API 連接多種大型語言模型
- 可針對載入的`MD檔`問答查詢
- 保存對話歷史實現上下文理解
- 簡單易用的命令行界面

## 安裝與設定

1. 確保已安裝 Python 3.8+
2. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```
3. 在 `main.py` 中設定您的 OpenRouter API 金鑰：
   ```python
   OPENROUTER_API_KEY = "請填入OpenRouter API金鑰"
   ```

## 使用說明

1. 執行程式：
   ```bash
   python main.py
   ```
2. 程式會自動載入 `2024魔球比賽紀錄.md` 檔案
3. 輸入您的問題，系統會根據比賽紀錄回答
4. 輸入 `q` 退出程式

## 檔案結構
- `main.py` - 主程式碼
- `requirements.txt` - Python 依賴套件列表
- `2024魔球比賽紀錄.md` - 比賽紀錄資料

## 支援的 LLM 模型
預設使用 `deepseek/deepseek-chat-v3-0324:free`，可在 `main.py`修改 `LLM_MODULE` 變數切換其他模型。  
例如：
- meta-llama/llama-3.3-70b-instruct:free
- qwen/qwen-2.5-72b-instruct:free

## 如果您有自己想驗證的MD檔
可以在 `main.py`修改 `MD_FULL_PATH` 變數來使用自己的MD來使用自己的MD

## 注意事項
- 請妥善保管您的 API 金鑰
- 免費模型可能有使用限制
- 確保MD檔案存在且格式正確
