from flask import Flask, render_template, request, jsonify
import asyncio
from agents import Agent, Runner

# ✅ 佐渡島アシスタントの設定
plants_tutor_agent = Agent(
    name="Ume",
    handoff_description="佐渡島の植物に関する専門エージェント",
    instructions="植物に関する質問に答えてください。佐渡弁で回答してください。例えば「〇〇だっちゃ」「〇〇してぇの」などの表現を使ってください。",
)

geography_tutor_agent = Agent(
    name="Hiro",
    handoff_description="佐渡島の地理に関する専門エージェント",
    instructions="地理に関する質問に答えてください。佐渡弁で回答してください。例えば「〇〇だっちゃ」「〇〇してぇの」などの表現を使ってください。",
)

famous_people_agent = Agent(
    name="Sado Celebrities",
    handoff_description="佐渡島出身の有名人に関するエージェント",
    instructions="佐渡島出身の著名人について説明してください。佐渡弁で回答してください。例えば「〇〇だっちゃ」「〇〇してぇの」などの表現を使ってください。",
)

# ✅ 質問を振り分けるトリアージエージェント
triage_agent = Agent(
    name="Sado Assistant",
    instructions="佐渡島に関する質問に答えてください。回答は佐渡弁で行ってください。",
    handoffs=[plants_tutor_agent, geography_tutor_agent, famous_people_agent],
)

app = Flask(__name__)

# ✅ 非同期でエージェントを実行する関数
async def get_response(user_input):
    result = await Runner.run(triage_agent, user_input)
    return result.final_output

@app.route("/")
def home():
    return render_template("index.html")  # ✅ HTMLを表示

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")  # ✅ ユーザーの入力を受け取る
    response = asyncio.run(get_response(user_input))  # ✅ 非同期でエージェントを実行
    return jsonify({"response": response})  # ✅ JSONでレスポンスを返す

if __name__ == "__main__":
    app.run(debug=True)  # ✅ Webサーバーを起動