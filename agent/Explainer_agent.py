def explainer_agent(topic, text):
    prompt = f"""
    Explain this topic simply with examples:

    Topic: {topic}
    Content: {text}
    """

    ...