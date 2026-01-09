from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = prompt =  f"""
You are a working professional posting on LinkedIn after a real-life realization.

Strict rules:
- NO preamble
- NO motivational lecture
- NO textbook explanations
- NO repetition
- Do NOT use generic self-help language

Writing style:
- Sound thoughtful and experienced
- Write like a human, not a coach
- Keep sentences crisp
- Use pauses (line breaks)
- Avoid overexplaining

Tone:
- Calm
- Honest
- Practical
- LinkedIn-native

Post constraints:
Topic: {tag}
Length: {length_str}
Language: {language}

Write the post directly.
"""

    # prompt = prompt.format(post_topic=tag, post_length=length_str, post_language=language)

    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: # Use max two samples
            break

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health"))