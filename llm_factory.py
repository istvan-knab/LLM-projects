import ollama

class LLM:

    def __init__(self, model:str) -> None:
        client = ollama.Client()
        response = client.generate(model=model, prompt='Say my name if you are alive, I am Istvan Gellert Knab,'
                                                       ' generate me a personal info card in console')
        print(response['response'])