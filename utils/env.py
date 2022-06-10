import gym
import sys

sys.path.append('/Users/srahmoun/Documents/Thesis/dio/')

import gym_minigrid


def make_env(env_key, seed=None):
    env = gym.make(env_key)
    env.seed(seed)
    return env
