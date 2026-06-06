from openai import OpenAI


from scraper import fetch_website_contents

# Define our system prompt
system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
Respond in Persian language
"""

# Define our user prompt
user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""


def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]


OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key="ollama"
)


def summarize(url):
    website = fetch_website_contents(url)

    response = ollama.chat.completions.create(
        model="gemma3:1b",
        messages=messages_for(website)
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    url = input("Enter website URL: ")
    summary = summarize(url)
    print("\nGenerating summary...\n")
    print(summary)