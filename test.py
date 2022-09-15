import gym
import d4rl # Import required to register environments

# Create the environment
env = gym.make('antmaze-umaze-v0')

# d4rl abides by the OpenAI gym interface
env.reset()
for i in range(1000):
	env.step(env.action_space.sample())
	env.render()
