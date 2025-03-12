import ollama

class LLM:

    def __init__(self, model:str, env) -> None:
        self.model = model
        self.client = ollama.Client()
        response = self.client.generate(model=model, prompt=f'Please consider the problem of the environment{env}, '
                                                            f'you will have to find the best way, the url of description'
                                                            f' is the following:https://gymnasium.farama.org/environments/toy_text/frozen_lake/')
        print(response['response'])

    def step(self, state):
        prompt='You have to use a valid action from the action space. I need a single integer in the response'
        action = self.client.generate(model=self.model,prompt=prompt)
        return action['response']