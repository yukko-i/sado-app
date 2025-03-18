from flask import Flask, render_template, request, jsonify
import asyncio
from agents import Runner

app = Flask(__name__)

# ✅ 非同期でエージェントを実行する関数
async def get_response(user_input):
    result = await Runner.run(triage_agent, user_input)
    return result.final_output

@app.route("/")
def home():
    return render_template("index.html")  # ✅ HTMLファイルを表示

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")  # ✅ ユーザーの入力を受け取る
    response = asyncio.run(get_response(user_input))  # ✅ 非同期でエージェントを実行
    return jsonify({"response": response})  # ✅ JSONでレスポンスを返す

if __name__ == "__main__":
    app.run(debug=True)  # ✅ Webサーバーを起動