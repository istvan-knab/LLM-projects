import ollama

class LLM:

    def __init__(self, model:str) -> None:
        client = ollama.Client()
        response = client.generate(model=model, prompt='How many parameters do you have?')
        print(response['response'])