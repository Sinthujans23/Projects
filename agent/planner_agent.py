from ai_service import client

def planner_agent(text):
    prompt = f"""
    Break this into topics and create a study plan:

    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a study planner."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content