# Copyright 2020,2021 Sony Corporation.
# Copyright 2021,2022 Sony Group Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gym
import numpy as np

from nnabla_rl.logger import logger


class Float32ObservationEnv(gym.ObservationWrapper):

    def __init__(self, env):
        super(Float32ObservationEnv, self).__init__(env)
        self.dtype = np.float32
        self.observation_space.dtype = np.dtype(np.float32)

    def observation(self, observation):
        if isinstance(observation, tuple):
            return tuple(map(self.dtype, observation))
        else:
            return self.dtype(observation)


class Float32RewardEnv(gym.RewardWrapper):
    def __init__(self, env):
        super(Float32RewardEnv, self).__init__(env)
        self.dtype = np.float32

    def reward(self, reward):
        return self.dtype(reward)


class Float32ActionEnv(gym.ActionWrapper):

    def __init__(self, env):
        super(Float32ActionEnv, self).__init__(env)
        self.dtype = np.float32

    def action(self, action):
        return self.dtype(action)

    def reverse_action(self, action):
        return self.env.action_space.dtype(action)


class Int32ActionEnv(gym.ActionWrapper):

    def __init__(self, env):
        super(Int32ActionEnv, self).__init__(env)
        self.dtype = np.int32

    def action(self, action):
        if isinstance(action, np.ndarray):
            action = action[0]
        return self.dtype(action)

    def reverse_action(self, action):
        return self.env.action_space.dtype(action)


class NumpyFloat32Env(gym.Wrapper):
    def __init__(self, env):
        env = Float32ObservationEnv(env)
        env = Float32RewardEnv(env)
        if isinstance(env.action_space, gym.spaces.Discrete):
            env = Int32ActionEnv(env)
        else:
            env = Float32ActionEnv(env)

        super(NumpyFloat32Env, self).__init__(env)


class ScreenRenderEnv(gym.Wrapper):
    def __init__(self, env):
        super(ScreenRenderEnv, self).__init__(env)
        self._env_name = env.unwrapped.spec.id

    def step(self, action):
        self.env.render()
        return self.env.step(action)

    def reset(self):
        if 'Bullet' in self._env_name:
            self.env.render()
            state = self.env.reset()
        else:
            state = self.env.reset()
            self.env.render()
        return state


class PrintEpisodeResultEnv(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        self._episode_rewards = []
        self._episode_num = 0

    def step(self, action):
        s_next, reward, done, info = self.env.step(action)
        self._episode_rewards.append(reward)
        if done:
            self._episode_num += 1
            episode_steps = len(self._episode_rewards)
            episode_return = np.sum(self._episode_rewards)
            logger.info(f'Episode #{self._episode_num} finished.')
            logger.info(f'Episode steps: {episode_steps}. Total return: {episode_return}.')
            self._episode_rewards.clear()
        return s_next, reward, done, info

    def reset(self):
        self._episode_rewards.clear()
        return self.env.reset()
