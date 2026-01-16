def study_help_prompt(context, topic, task):
    prompt = f"""
    you are a study helper

    Context:
    {context}

    Topic:
    {topic}

    Task:
    {task}
"""
    return prompt

prompt = study_help_prompt(
    context = "examinations coming",
    topic = "math",
    task = "explain the whole of calculus in a way that anyone can remember"
)

print(prompt)