from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_summary(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful tutor."},
            {"role": "user", "content": f"Summarize this:\n{text}"}
        ]
    )
    return response.choices[0].message.content