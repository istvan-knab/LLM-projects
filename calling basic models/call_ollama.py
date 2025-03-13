import ollama
import requests

class OllamaLocal:

    def __init__(self, model:str) -> None:
        self.model = model
        self.client = ollama.Client()
        response = self.client.generate(model=model, prompt="'Say Hello")
        print(response['response'])

    def respond(self, prompt:str) -> None:
        action = self.client.generate(model=self.model,prompt=prompt)
        return action['response']

class OllamaAPI:
    def __init__(self) -> None:
        self.url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3.3",
            "prompt": "Hello, how are you?",
            "stream": False
        }

        response = requests.post("http://localhost:11434/api/generate", json=payload)
        print(response.status_code, response.json())

    def respond(self, prompt:str) -> None:
        payload = {
            "model": "llama3",  # Change model name if using another one
            "prompt": prompt,
            "stream": False  # Set to True for streamed responses
        }
        response = requests.post(self.url, json=payload)
        print(response.status_code, response.json())
        return response.json()["response"]




