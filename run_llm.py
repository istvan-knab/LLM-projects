import json
from llm_factory import LLM
import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map

if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)

    env = gym.make('FrozenLake-v1', desc=generate_random_map(size=8))
    model = LLM(config['model'], env)


    state = env.reset()
    done = False
    while not done:
        action = model.step(state)
        state, reward, terminated, truncated, info = env.step(action)

