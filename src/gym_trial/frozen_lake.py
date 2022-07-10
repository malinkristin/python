import gym
import numpy as np

# env = gym.make("FrozenLake-v1", is_slippery=False) # version without the .33 chance of slipping
env = gym.make("FrozenLake-v1")
observation = env.reset()

state_table = np.zeros((16, 4))
train_episodes = 20000
alpha = 0.8
gamma = 0.9

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

# Training
for _ in range(train_episodes):
    state = env.reset()
    success = False

    while not success:
        # uncomment to watch the agent move on the board as it trains (will take much longer)
        # env.render()

        # actions are left, down, right, up - 0,1,2,3 respectively
        # action with the highest value will be taken here
        if np.max(state_table[state]) > 0:
            action = np.argmax(state_table[state])

        # if all action values are 0, a random action will be taken
        else:
            action = env.action_space.sample()

        # take the action and move into that direction
        new_state, success, reward, info = env.step(action)
        # take the new_state and update the table with the taken action and possible reward

        state_table[state, action] = state_table[state, action] + \
                                alpha * (reward + gamma * np.max(state_table[new_state]) - state_table[state, action])

        # update to the next state
        state = new_state

print('Reward table after training:')
print(state_table)

test_episodes = 20
success_rate_count = 0

# Testing
for _ in range(test_episodes):
    state = env.reset()
    done = False

    # Until the agent gets stuck or reaches the goal, keep training it
    while not done:
        env.render()

        if np.max(state_table[state]) > 0:
            action = np.argmax(state_table[state])
        else:
            action = env.action_space.sample()

        new_state, reward, done, info = env.step(action)

        # Update our current state
        state = new_state

        # When we get a reward, it means we solved the game
        success_rate_count += reward

print(f"Success rate = {success_rate_count / test_episodes * 100}%")
env.reset()
env.close()
