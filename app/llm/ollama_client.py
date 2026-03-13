import requests
import json


class OllamaClient:

    def __init__(self, model="llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        return response.json()["response"]
        result = data.get("response", "").strip()

        # Fix Ollama weird outputs like 'response'
        if result.lower() in ["response", "'response'", '"response"']:
            return "No meaningful response generated."

        return result

    def stream_generate(self, prompt: str):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True
        }

        response = requests.post(self.url, json=payload, stream=True)

        for line in response.iter_lines():

            if line:

                data = json.loads(line.decode("utf-8"))

                if "response" in data:
                    yield data["response"]