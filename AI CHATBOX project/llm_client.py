import httpx
import asyncio

class LLMClient:
    def __init__(self, base_url="http://192.168.20.1:1234/v1", api_key="sk-lm-CczGBGas:gEr37reWg6pvpwIIKwZR"):
        self.base_url = base_url
        self.api_key = api_key

    async def chat(self, messages, model="openai/gpt-oss-20b"):
        url = f"{self.base_url}/chat/completions"

        payload = {
            "model": model,
            "messages": messages,
            "temperature": 0.3
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        async with httpx.AsyncClient(timeout=60) as client:
            res = await client.post(url, json=payload, headers=headers)
            res.raise_for_status()
            data = res.json()

        return data["choices"][0]["message"]["content"]

# Example usage
async def main():
    client = LLMClient()
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the difference between AI and ML."}
    ]
    response = await client.chat(messages)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
