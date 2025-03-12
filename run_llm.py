import json
from llm_factory import LLM

if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)
    model = LLM(config['model'])