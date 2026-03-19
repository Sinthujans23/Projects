def evaluator_agent(question, user_answer):
    prompt = f"""
    Question: {question}
    Answer: {user_answer}

    Check if correct and explain.
    """