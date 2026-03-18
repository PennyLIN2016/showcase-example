class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_prompt(self, prompt):
        import openai

        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'] if response.choices else None