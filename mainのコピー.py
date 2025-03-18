import asyncio
from agents import Agent, Runner

# ✅ 1. 植物に関するエージェント
plants_tutor_agent = Agent(
    name="Ume",
    handoff_description="佐渡島の植物に関する専門エージェント",
    instructions="植物に関する質問に答えてください。佐渡島の植物について明確に説明し、佐渡弁で回答してください。",
)

# ✅ 2. 地理に関するエージェント
geography_tutor_agent = Agent(
    name="Hiro",
    handoff_description="佐渡島の地理に関する専門エージェント",
    instructions="地理に関する質問に答えてください。地名の由来や佐渡島内の位置について説明し、佐渡弁で回答してください。",
)

# ✅ 3. 質問を振り分けるトリアージエージェント
triage_agent = Agent(
    name="Triage Agent",
    instructions="ユーザーの質問の内容に基づいて、適切なエージェントを選択してください。回答は佐渡弁で行ってください。",
    handoffs=[plants_tutor_agent, geography_tutor_agent],
)

# ✅ 4. 実行関数
async def main():
    result = await Runner.run(triage_agent, "佐渡島には何種類の植物がありますか？")
    print("植物エージェントの応答:", result.final_output)

    result = await Runner.run(triage_agent, "佐渡島の地形の特徴は？")
    print("地理エージェントの応答:", result.final_output)

# ✅ 5. 実行
if __name__ == "__main__":
    asyncio.run(main())

