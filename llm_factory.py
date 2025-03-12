import ollama

class LLM:

    def __init__(self, model:str) -> None:
        client = ollama.Client()
        response = client.generate(model=model, prompt='Who are you? which model are you?')
        print(response['response'])