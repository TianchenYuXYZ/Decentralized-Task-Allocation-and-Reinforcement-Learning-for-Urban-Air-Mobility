import tensorflow as tf
import numpy as np
import os
import pickle
from DDPG2.DDPG import DDPG_agent
from env.EnvHeightControl import EnvHeightControl
import time

tf.set_random_seed(22)
np.set_printoptions(precision=3, suppress=True)
PATH = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(PATH, "data")
config = tf.ConfigProto(allow_soft_placement=True)
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

env = EnvHeightControl()
state_shape = 1
action_bound = 1
action_dim = 1
agent = DDPG_agent(sess, state_shape, action_bound, action_dim,minibatch_size = 32)
sess.run(tf.global_variables_initializer())
saver = tf.train.Saver(max_to_keep = 100)
if not agent.load(saver, DIR):
	sess.run(tf.global_variables_initializer())
	if not os.path.exists(DIR):
		os.mkdir(DIR)
else:
	print ("coninnue------------------")
episode_count, success, episode_reward, step_count = 0, 0, 0, 0
treward = []
state = env.reset()
tsucc = []
tstep = []
tres = []

while True:

    action = agent.act(state)
    next_state, reward, done, info = env.step(action)
    episode_reward += reward
    agent.observe(state, action, reward, next_state, done)
    agent.train(times = 1)
    state = next_state
    step_count += 1
    print ("action: {}".format(action).ljust(20," "),"abso height: {:.2f}".format(state[1][0]*50).ljust(20," "), "reward: {:.5f}.".format(reward).ljust(20," "),"steps: {}".format(step_count).ljust(20," "),end = "\r")

    if done:

        if info == "success":
            success += 1
        print (" "*80,end = "\r")
        print("episode {} finish, reward: {:.5f}, total success: {} result: {} step: {}".format(episode_count, episode_reward, success, info, step_count).ljust(80," "))
        treward.append(episode_reward)
        tsucc.append(success)
        tstep.append(step_count)
        tres.append(info)
        episode_reward = 0
        step_count = 0
        episode_count += 1
        if episode_count % 50 == 0:
            time_stape = time.time()
            nDir = os.path.join(PATH, "data" + "/{}/".format(str(episode_count)+str(time_stape)))
            if not os.path.exists(nDir):
                os.mkdir(nDir)
            agent.save(saver,nDir)
            #agent.save(saver,filename + "/{}/".format(str(episode_count)))

        #if episode_count >= 100:
        #    break
        state = env.reset()