# lm_studio_tool.py
import os
from openai import OpenAI
import requests

class LMStudioClient:
    def __init__(self, base_url="http://192.168.1.76:1234/v1", api_key=None):
        api_key = api_key or os.getenv("sk-lm-x8k28bXn:EwQrZiAvKjLXx1YSMIdq", "lm-studio")
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key
        )

    def generate(self, system_prompt, user_prompt, model="openai/gpt-oss-20b"):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return response.choices[0].message.content

        except requests.exceptions.Timeout:
            return "[ERROR] LM Studio timeout"

        except Exception as e:
            return f"[ERROR] {str(e)}"
