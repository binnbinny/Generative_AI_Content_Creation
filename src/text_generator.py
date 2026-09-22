import requests


class TextGenerator:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8080"

    def generate(self, prompt):

        response = requests.post(
            f"{self.base_url}/v1/chat/completions",
            json={
                "model": "Qwen2.5-1.5B-Instruct-GGUF:Q4_K_M",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 500
            },
            timeout=300
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]


if __name__ == "__main__":

    generator = TextGenerator()

    while True:

        prompt = input("\nEnter your prompt (or type exit): ")

        if prompt.lower() == "exit":
            break

        print("\n===== GENERATED CONTENT =====")

        result = generator.generate(prompt)

        print(result)