import json
from call_ollama import*

def use_local() -> None:
    with open('../config.json', 'r') as f:
        config = json.load(f)
    model = OllamaLocal(config['model'])

    while True:
        print(model.respond(input("What do you do?")))

def use_api() -> None:
    with open('../config.json', 'r') as f:
        config = json.load(f)
    model = OllamaAPI()
    while True:
        print(model.respond(input("What do you do?")))

if __name__ == "__main__":
    use_local()